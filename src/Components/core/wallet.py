# Copyright 2025 oppj4, cathome1, GOVNO-TON
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import requests
import base64
import sqlite3

from pathlib import Path
from time import sleep
from datetime import datetime
from Components.core.speaker import Speaker
from Components.core.initialization import InitBlock

class Wallet(InitBlock):
    
    def __init__(self, owner_address: str, jetton_master:str, api_key: str,  api_url:str, db_path, update_ui):
        super().__init__()
        self.__owner_address = self.ton_to_raw(owner_address)
        self.__jetton_master = jetton_master
        self.__key = api_key
        self.__url = api_url
        self.__db_path = db_path
        self.thread_flag = False
        self.update_ui = update_ui

    def toogle_thread(self):
        self.thread_flag = not self.thread_flag

    def get_transactions(self):
        try:
            url = f"{self.__url}jetton/transfers"
            params = {
                "owner_address": self.__owner_address,
                "jetton_master": self.__jetton_master,
                "limit": 10,  # Просмотр полседних N транзакций
                "api_key": self.__key
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()["jetton_transfers"]
        except Exception as e:
            print(f"Ошибка при запросе транзакций: {e}")
            return []

    def update_transactions_info(self, transactions):
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT trans_hash FROM donates")
        old_trans = cursor.fetchall()
        if old_trans == None: old_trans = ()
        new_trans = []
        for tx in transactions:
            
            if tx["destination"] == self.__owner_address.upper() and (tx["transaction_hash"],) not in old_trans:
                
                trans = {"out_wallet":self.__get_UQ_adress(tx["source"]), 
                        "amount":float(int(tx["amount"]) / 10 ** 9), 
                        # "message" : self.__decode_message(tx["custom_payload"]),
                        "trans_hash":tx["transaction_hash"],
                        "time": datetime.fromtimestamp(tx["transaction_now"]).strftime("%Y-%m-%d %H:%M:%S") }
                
                if tx["forward_payload"]:
                    trans["message"] = self.__decode_message(tx["forward_payload"])
                else:
                    trans["message"] = self.__decode_message(tx["custom_payload"])
                    
                if 'e-' in str(trans["amount"]):
                    trans["amount"] = f"{trans["amount"]:.9f}"
                cursor.execute("""
                INSERT INTO donates 
                (trans_hash, donate_amount, donater_wallet, message, datatime)
                VALUES 
                (?, ?, ?, ?, ?) 
            """, (trans["trans_hash"], trans["amount"],trans["out_wallet"] ,trans["message"] ,trans["time"]))
                new_trans.append(trans)
        conn.commit()
        conn.close()
        return new_trans

    def __get_UQ_adress(self, raw_adress):
        try:
            url = f"{self.__url}addressBook"
            params = {
                "address": raw_adress,
                "api_key": self.__key
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()[raw_adress]["user_friendly"]
        except Exception as e:
            print(f"Ошибка при запросе User_Friendly адреса: {e}")
            return 0

    def __decode_message(self, base64_message):
        dedust_flag = "te6cckEBAQEABgAACC4c+oIOFKCh"
        if base64_message == None or base64_message == dedust_flag:
            return ""
        try:
            decoded_bytes = base64.b64decode(base64_message)[14:-4].decode("utf8", errors='ignore').replace("\n", " ")
            cleaned_text = re.sub(r'[\x00-\x1F\x7F]', '', decoded_bytes)
            if re.search(r'^\W_', cleaned_text, re.UNICODE):
                return ""
            return cleaned_text
        except Exception as e:
            print(f"Ошибка декодирования сообщения: {e}")
            return base64_message

    def ton_to_raw(self, ton_address: str) -> str:
        if ton_address[:2] == "0:":
            return ton_address
        try:
            # Декодируем user-friendly адрес из base64 (TON использует URL-safe base64 без паддинга)
            decoded = base64.urlsafe_b64decode(ton_address + "===")
            
            # Проверяем корректность длины (должно быть 36 байт: 1 байт версии, 1 байт флагов, 32 байта адреса, 2 байта CRC)
            if len(decoded) != 36:
                return 0
            
            # Берем 32 байта, исключая первые 2 байта (версия и флаги) и последние 2 байта (CRC)
            raw_address ="0:" + decoded[2:-2].hex()
            
            return raw_address
        except Exception as e:
            return 0

    def monitor_wallet(self):
        print("Запуск мониторинга кошелька...")
        transactions = self.get_transactions()
        if not transactions:
            print(f"Транзакций не найдено, жду {self.data_constants["sleep_interval"]} секунд...")
            return int(self.data_constants["sleep_interval"])  # Проверка каждые N секунд
        else:
            jetton_transactions = self.update_transactions_info(transactions)
            if jetton_transactions:
                self.update_ui()
                print(f"Найдено транзакций с Jetton и текстом: {len(jetton_transactions)}")
                for tx in jetton_transactions:
                    template_type = ''
                    print(f"Дата: {tx['time']}")
                    print(f"Отправитель: {tx['out_wallet']}")
                    print(f"Сумма: {tx['amount']} 💎")
                    print(f"Текст сообщения: {tx['message']}")
                    print("-" * 30)
                    if len(self.data) >= 1:
                        for key in self.data.keys():
                            current_price =float(self.data[key]["ALERT_SETTINGS"]["price"])
                            if self.data[key]["enabled"]:
                                if (template_type == '' and 
                                    current_price <= float(tx['amount'])):
                                    template_type = key
                                elif (current_price <= float(tx['amount']) and 
                                    current_price >= float(self.data.get(template_type)["ALERT_SETTINGS"]["price"])):
                                    template_type = key                        
                    if template_type != '':
                        
                        url = f"http://{self.data_constants["server_ip"]}:{self.data_constants["server_port"]}/donate"
                        donater = tx['out_wallet'][:5] + "......" + tx['out_wallet'][-5:]
                        alert_settings = self.data[template_type]["ALERT_SETTINGS"]
                        alert_paths = self.data[template_type]["PATH"]                        
                        cutted_msg = tx['message'][:int(self.data_sound["len_msg"])]
                        
                        data = {
                            "name": donater,
                            "message": cutted_msg,
                            "sound1": alert_paths["audio_path"],
                            # "sound2": "output.mp3", # Сделать обрааботку если донат без войса
                            "gif": alert_paths["gif_path"],
                            "duration": int(alert_settings["duration"]) * 1000
                        }
                        if cutted_msg:
                            voice_alarm = Speaker(lang=self.data_sound["lang"], scale=self.data_sound["scale"], audio_path=Path(self.LOCAL_PATH, self.data_constants["voice_path"]), pitch=self.data_sound["pitch"])
                            voice_duration = voice_alarm.audio_create_and_transform(text=cutted_msg, file_path=Path(self.LOCAL_PATH, self.data_constants["voice_path"]))
                            data["sound2"] = f"{self.data_constants["voice_path"].split('/')[-1][:-4]}_fixed.mp3" #Я покакала
                            
                        else:
                            voice_duration = False
                            data["sound2"] = "-"
                        response = requests.post(url, json=data, headers={"Content-Type": "application/json"})
                        if voice_duration:
                            sleep(voice_duration)    # Задержка чтобы предыдущее сообщение успело воспроизвестись
                        print("---",response.status_code)
                        sleep(int(self.data_constants["sleep_interval"]))
            else:
                print(f"Входящих транзакций не найдено, жду {self.data_constants["sleep_interval"]} секунд...")
                return int(self.data_constants["sleep_interval"])  # Проверка каждые N секунд
            return 1
    