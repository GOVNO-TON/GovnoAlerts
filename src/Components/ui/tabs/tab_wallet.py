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

from PyQt5.QtWidgets import QMessageBox
from Components.core.wallet import Wallet

class WalletTab:
    def __init__(self):
        pass

    def save_wallet_api_key(self):
        text = str(self.ui.wallet_api_key_textbox.toPlainText())
        if text != "":
            self.data_wallet["api_key"] = text.replace(' ', '')
            self.save_json(self.JSON_FILE_WALLET, {"wallet_settings": self.data_wallet})
            self.obs_wallet = Wallet(self.data_wallet["wallet_raw"], self.data_constants["jetton_master"], self.data_wallet["api_key"], self.data_constants["api_url"], db_path=self.path(self.LOCAL_PATH, self.data_constants["db_path"]), update_ui=self.update_table_view)
            QMessageBox.information(self, "Успех", "Настройки сохранены!")
        else:
            QMessageBox.warning(self, "Ошибка", "Поле не может быть пустым")
            return

    def save_wallet_raw_adr(self):
        text = str(self.ui.wallet_addr_textbox.toPlainText())
        if text != "":
            self.data_wallet["wallet_raw"] = text.replace(' ', '')
            self.save_json(self.JSON_FILE_WALLET, {"wallet_settings": self.data_wallet})
            self.obs_wallet = Wallet(self.data_wallet["wallet_raw"], self.data_constants["jetton_master"], self.data_wallet["api_key"], self.data_constants["api_url"], db_path=self.path(self.LOCAL_PATH, self.data_constants["db_path"]), update_ui=self.update_table_view)
            QMessageBox.information(self, "Успех", "Настройки сохранены!")
        else:
            QMessageBox.warning(self, "Ошибка", "Поле не может быть пустым")
            return
        
    def update_wallet_settings(self):
        """Загружает настройки и обновляет UI"""
        self.ui.wallet_api_key_textbox.setPlainText(self.data_wallet["api_key"])
        self.ui.wallet_addr_textbox.setPlainText(self.data_wallet["wallet_raw"])
        self.save_json(self.JSON_FILE_WALLET, {"wallet_settings": self.data_wallet})
