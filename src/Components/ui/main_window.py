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

import sys
import os

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox

if os.name == "nt": 
    from Components.ui.settings_windows import Ui_MainWindow
else: 
    from Components.ui.settings_mac import Ui_MainWindow

from Components.ui.tabs.tab_main import MainTab
from Components.ui.tabs.tab_voice import VoiceTab
from Components.ui.tabs.tab_alerts import AlertsTab
from Components.ui.tabs.tab_wallet import WalletTab
from Components.ui.tabs.tab_filter import FilterTab
from Components.core.initialization import InitBlock
from Components.core.wallet import Wallet
from Components.ui.ui_handlers import Handlers

class MainApp(QtWidgets.QMainWindow, InitBlock, Handlers, MainTab, AlertsTab, WalletTab, VoiceTab, FilterTab):
    def __init__(self):
        super().__init__()
        #загрузка ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_tab_main()
        self.setup_alerts_tab()
        self.setup_voice_tab()
        self.setup_wallet_tab()
        self.setup_filter_tab()
        
        self.obs_wallet = Wallet(self.data_wallet["wallet_raw"], self.data_constants["jetton_master"], self.data_wallet["api_key"], self.data_constants["api_url"], db_path=self.path(self.LOCAL_PATH, self.data_constants["db_path"]), update_ui=self.update_table_view)

        # Блок линков
        self.tg_link_1 = "https://t.me/LanArch1"
        self.tg_link_2 = "https://t.me/cathome"
        self.make_label_clickable(self.ui.telegram_link_1, self.tg_link_1)
        self.make_label_clickable(self.ui.telegram_link_2, self.tg_link_2)
        
        self.check_license()
        
        # Обновляем элементы
        self.update_table_view()
        self.update_list_widget()
        self.update_voice_settings()
        self.update_wallet_settings()
        self.init_filter()

    def run_wallet_monitor(self):
        """Мониторинг кошелька, вызываемый таймером"""
        transactions = self.obs_wallet.get_transactions()
        if not transactions:
            print(f"Транзакций нет, жду {self.data_constants['sleep_interval']} секунд...")
        else:
            print("Найдена новая транзакция!")
        
    def closeEvent(self, event):
        """Обработка закрытия приложения"""
        close = QMessageBox.question(self,
                                     "Закрыть приложение?",
                                     "Вы уверенны?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            available_files = self.get_available_files()
            gifs_files = self.get_folder_files(self.path(self.LOCAL_PATH, "data", "gifs"))
            sounds_files = self.get_folder_files(self.path(self.LOCAL_PATH, "data", "sounds"))
            self.delete_files(gifs_files, available_files=available_files)
            self.delete_files(sounds_files, available_files=available_files)
            event.accept()
        else:
            event.ignore()
            
    def get_available_files(self):
        available_files = []
        for i in self.data:
            for k in list(self.data[i]["PATH"].values()):
                if k != '':
                    if k.split(".")[-1] == "gif":
                        available_files.append(str(self.path(self.LOCAL_PATH, "data", "gifs", k)))
                    elif k.split(".")[-1] == "mp3":
                        available_files.append(str(self.path(self.LOCAL_PATH, "data", "sounds", k)))
        return available_files
    
    def get_folder_files(self, path):
        folder_files = []
        for entry in path.iterdir():
            if entry.is_file():
                if entry.name.split('.')[-1] == "gif":
                    folder_files.append(str(self.path(self.LOCAL_PATH, "data", "gifs", entry.name)))
                elif entry.name.split('.')[-1] == "mp3":
                    folder_files.append(str(self.path(self.LOCAL_PATH, "data", "sounds", entry.name)))
        return folder_files

    def delete_files(self, path_to_files,  available_files):
        for i in path_to_files:
            if i not in available_files:
                os.remove(i)
