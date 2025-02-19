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
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import QUrl, Qt, QTimer
from PySide6.QtGui import QDesktopServices

if os.name == "nt": 
    from Components.ui.settings_windows import Ui_MainWindow
else: 
    from Components.ui.settings_mac import Ui_MainWindow

from Components.ui.tabs.tab_main import MainTab
from Components.ui.tabs.tab_voice import VoiceTab
from Components.ui.tabs.tab_alerts import AlertsTab
from Components.ui.tabs.tab_wallet import WalletTab
from Components.core.initialization import InitBlock

from Components.core.wallet import Wallet

class MainApp(QtWidgets.QMainWindow, InitBlock, MainTab, AlertsTab, WalletTab, VoiceTab):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.change_lang_comboBox.setItemData(0, "ru")
        self.ui.change_lang_comboBox.setItemData(1, "en")

        header = self.ui.donate_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)  # Фиксированный размер столбцов

        self.obs_wallet = Wallet(self.data_wallet["wallet_raw"], self.data_constants["jetton_master"], self.data_wallet["api_key"], self.data_constants["api_url"], db_path=self.path(self.LOCAL_PATH, self.data_constants["db_path"]), update_ui=self.update_table_view)

        # Старт/стоп кнопки
        self.is_running = False
        self.ui.Start_btn.clicked.connect(self.toggle)

        self.timer = QTimer(self)  
        self.timer.timeout.connect(self.enable_button) 

        # Блок линков
        self.tg_link_1 = "https://t.me/LanArch1"
        self.tg_link_2 = "https://t.me/cathome"

        self.make_label_clickable(self.ui.telegram_link_1, self.tg_link_1)
        self.make_label_clickable(self.ui.telegram_link_2, self.tg_link_2)
        self.make_label_clickable(self.ui.wallet_faq_label, "https://t.me/toncenter")

        self.check_license()
        
        self.ui.alert_settings_canvas.setVisible(False)  # Скрываем меню настроек шаблонов

        self.update_tab_main()
        self.copy_to_clickboard(self.ui.server_ip_label)
        self.copy_to_clickboard(self.ui.copy_ip_btn, text=self.ui.server_ip_label.text())

        # Подключаем кнопки к методам text alerts
        self.ui.shema_add_button.clicked.connect(self.add_template)
        self.ui.shema_del_button.clicked.connect(self.remove_template)
        self.ui.save_shema_button.clicked.connect(self.save_template)

        self.ui.shema_listbox.itemClicked.connect(self.load_template)

        # Кнопки в меню настройки кошелька
        self.ui.wallet_api_key_button.clicked.connect(self.save_wallet_api_key)
        self.ui.wallet_addr_button.clicked.connect(self.save_wallet_raw_adr)

        # Добавляем кнопки "Обзор" для выбора файлов text alerts
        self.ui.search_file_gif_btn.clicked.connect(lambda: self.select_file(self.ui.alert_gif_textbox, "GIF файлы (*.gif)"))
        self.ui.search_path_audio_btn.clicked.connect(lambda: self.select_file(self.ui.allert_sound_path_textbox, "MP3 файлы (*.mp3)"))

        # Связываем ползунки с обновлением значений в QLabel text alerts
        self.ui.text_duration_slider.valueChanged.connect(lambda: self.update_label(self.ui.text_duration_slider, self.ui.text_duration_label_2))
        self.ui.volume_alert_slider.valueChanged.connect(lambda: self.update_label(self.ui.volume_alert_slider, self.ui.volume_allert_counter_label))

        self.ui.text_duration_label_2.valueChanged.connect(self.ui.text_duration_slider.setValue)
        self.ui.volume_allert_counter_label.valueChanged.connect(self.ui.volume_alert_slider.setValue)  

        # text alerts
        self.ui.text_duration_slider.setRange(0, 999)
        self.ui.text_duration_slider.setSingleStep(1)
        self.ui.volume_alert_slider.setRange(0, 400)
        self.ui.volume_alert_slider.setSingleStep(1)
        # alerts voice
        self.ui.volume_slider.valueChanged.connect(lambda: self.update_label(self.ui.volume_slider, self.ui.voice_volume_label))

        self.ui.voice_volume_label.valueChanged.connect(self.ui.volume_slider.setValue)

        self.factor = 100
        self.ui.speed_slider.setMaximum(200)
        self.ui.speed_slider.valueChanged.connect(self.update_spinbox)
        self.ui.voice_speed_label.valueChanged.connect(self.update_slider)

        self.ui.save_voice_settings_btn.clicked.connect(self.save_text_alerts)
        self.ui.test_msg_textbox_button.clicked.connect(self.play_test)
        # Обновляем элементы
        self.update_table_view()
        self.update_list_widget()
        self.update_voice_settings()
        self.update_wallet_settings()
        
    def run_wallet_monitor(self):
        """Мониторинг кошелька, вызываемый таймером"""
        transactions = self.obs_wallet.get_transactions()
        if not transactions:
            print(f"Транзакций нет, жду {self.data_constants['sleep_interval']} секунд...")
        else:
            print("Найдена новая транзакция!")
        # asyncio.new_event_loop().run_until_complete(self.obs_wallet.monitor_wallet(self.obs_wallet))

    def select_file(self, plain_text_edit, extension):
        """Открывает диалог выбора файла и записывает путь в QPlainTextEdit."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", f"{extension}")
        if file_path:
            plain_text_edit.setPlainText(file_path)

    def update_label(self, slider, label, flag=False, float=False):
        """Обновляет значение в QLabel при изменении ползунка."""
        print("залупа", label.objectName(), slider.value())
        if flag:
            label.setValue(int(slider.value() / 100))
        else:
            label.setValue(int(slider.value()))
            print(label.objectName(), slider.value())
        
        if float:
            label.setValue(slider.value() * 100)

    def make_label_clickable(self, label, url):
        """Добавляет к QLabel обработку клика"""
        label.setStyleSheet("color: blue; text-decoration: underline;")
        label.setCursor(Qt.CursorShape.PointingHandCursor)
        label.mousePressEvent = lambda event: self.open_link(url)

    def open_link(self, url):
        """Открывает ссылку в браузере"""
        QDesktopServices.openUrl(QUrl(url))

    def update_spinbox(self, value):
        """Обновление QDoubleSpinBox при изменении QSlider"""
        self.ui.voice_speed_label.setValue(value / self.factor)

    def update_slider(self, value):
        """Обновление QSlider при изменении QDoubleSpinBox"""
        self.ui.speed_slider.setValue(int(value * self.factor))
        
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
                
    
        
        
# Запуск приложения
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())