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

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from Components.core.wallet import Wallet

import os
import shutil


class AlertsTab:
    def __init__(self):
        pass
    def add_template(self):
        """Добавляет новый шаблон."""
        text, ok = QtWidgets.QInputDialog.getText(self, "Добавить шаблон", "Введите название:")
        if ok and text:
            if text in self.data:
                QMessageBox.warning(self, "Ошибка", "Шаблон с таким именем уже существует!")
                self.ui.alert_settings_canvas.setVisible(False)
                self.update_list_widget()
            else:
                self.data[text] = {
                    "enabled": True,
                    "ALERT_SETTINGS": {"scale": "100","duration": "10", "price": "0.0"},
                    "PATH": {"gif_path": "", "audio_path": ""},
                }
                self.save_json(self.JSON_FILE_TEMPLATES, {"templates": self.data})
                self.update_list_widget()
        elif text == '':
            self.ui.alert_settings_canvas.setVisible(False)
            QMessageBox.warning(self, "Ошибка", "Название не может быть пустым")

    def remove_template(self):
        """Удаляет выбранный шаблон."""
        selected_item = self.ui.shema_listbox.currentItem()
        ret = QMessageBox.question(self, "", "Вы действительно хотите удалить шаблон?")
        if ret == QMessageBox.Yes:
            if selected_item:
                template_name = selected_item.text()
                #Удаляем файлики
                path_to_gif = self.data[template_name]["PATH"]["gif_path"]
                path_to_audio = self.data[template_name]["PATH"]["audio_path"]
                
                self.delete_file(path_to_gif, path_to_audio)


                #Удаляем шаблон в структуре
                del self.data[template_name]
                self.save_json(self.JSON_FILE_TEMPLATES, {"templates": self.data})
                self.update_list_widget()
                self.obs_wallet = Wallet(self.data_wallet["wallet_raw"], self.data_constants["jetton_master"], self.data_wallet["api_key"], self.data_constants["api_url"], db_path=self.path(self.LOCAL_PATH, self.data_constants["db_path"]), update_ui=self.update_table_view)
                self.ui.alert_settings_canvas.setVisible(False)
            else:
                QMessageBox.warning(self, "Ошибка", "Выберите шаблон для удаления!")
                self.ui.alert_settings_canvas.setVisible(False)
        else: return

    def load_template(self):
        """Загружает данные шаблона при выборе."""
        selected_item = self.ui.shema_listbox.currentItem()
        if selected_item:
            self.ui.alert_settings_canvas.setVisible(True)
            template_name = selected_item.text()
            template_data = self.data.get(template_name, {})

            self.ui.name_shema_textbox.setPlainText(template_name)

            self.ui.text_duration_slider.setValue(int(template_data["ALERT_SETTINGS"]["duration"]))
            self.ui.volume_alert_slider.setValue(int(template_data["ALERT_SETTINGS"]["scale"]))
            self.ui.alert_min_trigger_price_box.setValue(float(template_data["ALERT_SETTINGS"]["price"]))

            self.ui.alert_gif_textbox.setPlainText(str(template_data["PATH"]["gif_path"]))
            self.ui.allert_sound_path_textbox.setPlainText(str(template_data["PATH"]["audio_path"]))

            self.ui.checkBox.setChecked(template_data.get("enabled", False))
            
        else:
            self.ui.alert_settings_canvas.setVisible(False)

    def save_template(self):
        """Сохраняет изменения в шаблоне."""
        selected_item = self.ui.shema_listbox.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Ошибка", "Выберите шаблон!")
            return

        template_name = selected_item.text()


        self.data[template_name]["enabled"] = self.ui.checkBox.isChecked()

        path_to_gif = self.ui.alert_gif_textbox.toPlainText()
        path_to_audio = self.ui.allert_sound_path_textbox.toPlainText()

        if path_to_audio == "" or path_to_gif == "":
            QMessageBox.warning(self, "Ошибка", "Не выбран файл Gif или Audio")
            return

        else:
            new_file_path_to_gif = self.copy_file(path_to_gif, self.path(self.LOCAL_PATH, "data", "gifs"), template_name=template_name)
            
            new_file_path_to_audio = self.copy_file(path_to_audio, self.path(self.LOCAL_PATH, "data", "sounds"), template_name=template_name)
            if os.name == "nt":
                
                self.data[template_name]["PATH"]["audio_path"] = new_file_path_to_audio.split("\\")[-1]
                self.data[template_name]["PATH"]["gif_path"] = new_file_path_to_gif.split("\\")[-1]
            else:
                self.data[template_name]["PATH"]["audio_path"] = new_file_path_to_audio.split("/")[-1]
                self.data[template_name]["PATH"]["gif_path"] = new_file_path_to_gif.split("/")[-1]                
            self.data[template_name]["ALERT_SETTINGS"]["duration"] = str(self.ui.text_duration_slider.value())
            self.data[template_name]["ALERT_SETTINGS"]["scale"] = str(self.ui.volume_alert_slider.value())
            self.data[template_name]["ALERT_SETTINGS"]["price"] = str(self.ui.alert_min_trigger_price_box.value())

            #Изменения названия шаблона
            self.data[self.ui.name_shema_textbox.toPlainText()] = self.data.pop(template_name)
            selected_item.setText(self.ui.name_shema_textbox.toPlainText())
            self.save_json(self.JSON_FILE_TEMPLATES, {"templates": self.data})
            self.update_template_style(selected_item)
            self.obs_wallet = Wallet(self.data_wallet["wallet_raw"], self.data_constants["jetton_master"], self.data_wallet["api_key"], self.data_constants["api_url"], db_path=self.path(self.LOCAL_PATH, self.data_constants["db_path"]), update_ui=self.update_table_view)
            QMessageBox.information(self, "Сохранено", "Настройки обновлены!")

    def copy_file(self, file_path, destination_folder, template_name):
        """Копирует файл в указанную папку и возвращает новый путь."""
        try:
            ext1 = os.path.splitext(file_path)[-1]
            if ext1 == ".mp3" and self.data[template_name]["PATH"]["audio_path"] == file_path:
                return file_path
            if ext1 == ".gif" and self.data[template_name]["PATH"]["gif_path"] == file_path:
                return file_path
            
            if not file_path:
                return ""

            # Убеждаемся, что папка назначения существует
            os.makedirs(destination_folder, exist_ok=True)
            # Получаем имя файла без пути
            file_name = os.path.basename(file_path)
            # Создаем путь для нового файла
            new_file_path = os.path.join(destination_folder, file_name)

            # Проверяем, существует ли уже файл с таким именем, и переименовываем
            counter = 1
            while os.path.exists(new_file_path):
                name, ext = os.path.splitext(file_name)
                new_file_path = os.path.join(destination_folder, f"{name}_{counter}{ext}")
                counter += 1
            # Копируем файл
            if new_file_path.split(".")[-1] == "mp3":
                if not os.path.exists(str(self.path(self.LOCAL_PATH, "data", "sounds", new_file_path.split("/")[-1]))):
                    shutil.copy(file_path, new_file_path) 

            elif new_file_path.split(".")[-1] == "gif":
                if not os.path.exists(str(self.path(self.LOCAL_PATH, "data", "gifs", new_file_path.split("/")[-1]))):
                    shutil.copy(file_path, new_file_path)

            return new_file_path  # Возвращаем новый путь файла
        except Exception as err:
            return 
    
    def delete_file(self, path_to_gif, path_to_audio):
        """Удаляем список файлов"""
        try:
            os.remove(str(self.path(self.LOCAL_PATH, "data", "gifs", path_to_gif)))
            os.remove(str(self.path(self.LOCAL_PATH, "data", "sounds", path_to_audio)))
            QMessageBox.information(self, "Успех", "Шаблон был удалён.")
        except:
            QMessageBox.warning(self, "Ошибка", "Шаблон не был сохранён.")
            self.ui.alert_settings_canvas.setVisible(False)
            return

    def update_template_style(self, selected_item = "_"):
        """Обновляет стиль названия шаблона в списке при переключении чекбокса"""
        if selected_item == "_":
            selected_item = self.ui.shema_listbox.currentItem()

        if not selected_item:
            return

        template_name = selected_item.text()
        is_enabled = self.data[template_name]["enabled"]
        # is_enabled = self.ui.checkBox.isChecked()  # Получаем состояние чекбокса

        if is_enabled:
            # Делаем текст зелёным и добавляем иконку "включено"
            selected_item.setForeground(Qt.GlobalColor.green)
            selected_item.setText(template_name)
        else:
            # Делаем текст серым и убираем иконку
            selected_item.setForeground(Qt.GlobalColor.gray)

        # Сохраняем состояние в данных
        self.data[template_name]["enabled"] = is_enabled
        self.save_json(self.JSON_FILE_TEMPLATES, {"templates": self.data})

    def update_list_widget(self):
        """Обновляет список шаблонов."""
        self.ui.shema_listbox.clear()
        for template_name in self.data:
            self.ui.shema_listbox.addItem(template_name)
        self.update_condition_template()
    
    def update_condition_template(self):
        for i in range(self.ui.shema_listbox.count()):
            self.update_template_style(self.ui.shema_listbox.item(i))
        