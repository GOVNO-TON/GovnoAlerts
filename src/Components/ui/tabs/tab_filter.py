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

from Components.core.filter import Filter
from Components.core.wallet import Wallet
class FilterTab:
    def __init__(self):
        pass
    
    def setup_filter_tab(self):
        self.ui.filter_comboBox.setItemData(0, "ignored")
        self.ui.filter_comboBox.setItemData(1, "censored")
        self.ui.filter_comboBox.setItemData(2, "approved")
        self.ui.filter_comboBox.currentIndexChanged.connect(self.update_link_filter)
        self.ui.test_filter_user_textedit.textChanged.connect(self.retranslate_test)
        self.ui.filter_save_btn.clicked.connect(self.save_filtered_words)
        
    def save_filtered_words(self):
        words = re.sub(r"[\n\t\r]+", " ", self.ui.filter_textEdit.toPlainText()).split(' ')
        words = [item for item in words if item.strip()]
        self.data_filter["BAD_WORDS"] = words
        self.save_json(self.JSON_FILE_FILTER, {"filter_settings": self.data_filter})
        self.obs_wallet = Wallet(self.data_wallet["wallet_raw"], self.data_constants["jetton_master"], self.data_wallet["api_key"], self.data_constants["api_url"], db_path=self.path(self.LOCAL_PATH, self.data_constants["db_path"]), update_ui=self.update_table_view)
        self.retranslate_test()

    def update_link_filter(self):
        self.data_filter["url_filter"] = str(self.ui.filter_comboBox.currentData())
        self.save_json(self.JSON_FILE_FILTER, {"filter_settings": self.data_filter})
    
    def init_filter(self):
        if self.data_filter["url_filter"] == "ignored": 
            self.ui.filter_comboBox.setCurrentIndex(0)
        elif self.data_filter["url_filter"] == "censored":
            self.ui.filter_comboBox.setCurrentIndex(1) 
        elif self.data_filter["url_filter"] == "approved":
            self.ui.filter_comboBox.setCurrentIndex(2)
             
        self.ui.filter_textEdit.setPlainText(' '.join(self.data_filter["BAD_WORDS"]).strip())
        self.save_json(self.JSON_FILE_FILTER, {"filter_settings": self.data_filter})
        
    def retranslate_test(self):
        text = self.ui.test_filter_user_textedit.toPlainText()
        filtred_text = Filter(self.data_filter["BAD_WORDS"]).text_filtration(text=text)
        
        self.ui.test_result_textEdit.setPlainText(filtred_text)

    