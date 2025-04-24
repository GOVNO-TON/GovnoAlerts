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

import os
import shutil
import logging

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from Components.core.wallet import Wallet

class AlertsTab:
    def __init__(self):
        pass

    def setup_alerts_tab(self):
        """Инициализация UI элементов вкладки алертов."""
        self.ui.alert_settings_canvas.setVisible(False)
        
        # Подключение сигналов
        self.ui.shema_add_button.clicked.connect(self.add_template)
        self.ui.shema_del_button.clicked.connect(self.remove_template)
        self.ui.save_shema_button.clicked.connect(self.save_template)
        self.ui.shema_listbox.itemClicked.connect(self.load_template)
        
        self.ui.search_file_gif_btn.clicked.connect(
            lambda: self.select_file(self.ui.alert_gif_textbox, "GIF файлы (*.gif)"))
        self.ui.search_path_audio_btn.clicked.connect(
            lambda: self.select_file(self.ui.allert_sound_path_textbox, "MP3 файлы (*.mp3)"))
        
        # Настройка слайдеров
        self.ui.text_duration_slider.setRange(0, 999)
        self.ui.text_duration_slider.setSingleStep(1)
        self.ui.volume_alert_slider.setRange(0, 400)
        self.ui.volume_alert_slider.setSingleStep(1)
        
        # Подключение обновления лейблов
        self.ui.text_duration_slider.valueChanged.connect(
            lambda: self.update_label(self.ui.text_duration_slider, self.ui.text_duration_label_2))
        self.ui.volume_alert_slider.valueChanged.connect(
            lambda: self.update_label(self.ui.volume_alert_slider, self.ui.volume_allert_counter_label))
        
        self.ui.text_duration_label_2.valueChanged.connect(self.ui.text_duration_slider.setValue)
        self.ui.volume_allert_counter_label.valueChanged.connect(self.ui.volume_alert_slider.setValue)

    # Основные методы работы с шаблонами
    def add_template(self):
        """Добавляет новый шаблон."""
        text, ok = QtWidgets.QInputDialog.getText(self, "Добавить шаблон", "Введите название:")
        
        if not ok:
            return
            
        if not text:
            self.ui.alert_settings_canvas.setVisible(False)
            QMessageBox.warning(self, "Ошибка", "Название не может быть пустым")
            return
            
        if text in self.data:
            QMessageBox.warning(self, "Ошибка", "Шаблон с таким именем уже существует!")
            self.ui.alert_settings_canvas.setVisible(False)
            self.update_list_widget()
            self.ui.shema_listbox.setFocus()
            return
            
        # Создаем новый шаблон
        self.data[text] = {
            "enabled": True,
            "ALERT_SETTINGS": {
                "scale": "100",
                "duration": "10", 
                "price": "0.0"
            },
            "PATH": {
                "gif_path": "", 
                "audio_path": ""
            },
        }
        
        self.save_json(self.JSON_FILE_TEMPLATES, {"templates": self.data})
        self.update_list_widget()
        
        # Выделяем новый шаблон
        items = self.ui.shema_listbox.findItems(text, Qt.MatchFlag.MatchExactly)
        if items:
            item = items[0]
            self.ui.shema_listbox.setCurrentItem(item)
            self.ui.shema_listbox.setFocus()
            self.load_template()

    def remove_template(self):
        """Удаляет выбранный шаблон."""
        selected_item = self.ui.shema_listbox.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Ошибка", "Выберите шаблон для удаления!")
            self.ui.alert_settings_canvas.setVisible(False)
            return
            
        ret = QMessageBox.question(self, "", "Вы действительно хотите удалить шаблон?")
        if ret != QMessageBox.StandardButton.Yes:
            return
            
        template_name = selected_item.text()
        
        # Удаляем связанные файлы
        try:
            self._delete_template_files(template_name)
        except Exception as e:
            logging.error(f"Ошибка при удалении файлов шаблона: {str(e)}")
            QMessageBox.warning(self, "Ошибка", "Не удалось удалить файлы шаблона")
            
        # Удаляем шаблон из данных
        if template_name in self.data:
            del self.data[template_name]
            self.save_json(self.JSON_FILE_TEMPLATES, {"templates": self.data})
            
        self.update_list_widget()
        self.ui.alert_settings_canvas.setVisible(False)
        
        # Обновляем кошелек
        self._update_wallet()

    def load_template(self):
        """Загружает данные шаблона при выборе."""
        selected_item = self.ui.shema_listbox.currentItem()
        if not selected_item:
            self.ui.alert_settings_canvas.setVisible(False)
            return
            
        self.ui.alert_settings_canvas.setVisible(True)
        template_name = selected_item.text()
        template_data = self.data.get(template_name, {})
        
        # Заполняем UI данными из шаблона
        self.ui.name_shema_textbox.setPlainText(template_name)
        self.ui.checkBox.setChecked(template_data.get("enabled", False))
        
        # Настройки алерта
        alert_settings = template_data.get("ALERT_SETTINGS", {})
        self.ui.text_duration_slider.setValue(int(alert_settings.get("duration", 10)))
        self.ui.volume_alert_slider.setValue(int(alert_settings.get("scale", 100)))
        self.ui.alert_min_trigger_price_box.setValue(float(alert_settings.get("price", 0.0)))
        
        # Пути к файлам
        paths = template_data.get("PATH", {})
        self.ui.alert_gif_textbox.setPlainText(paths.get("gif_path", ""))
        self.ui.allert_sound_path_textbox.setPlainText(paths.get("audio_path", ""))

    def save_template(self):
        """Сохраняет изменения в шаблоне."""
        try:
            selected_item = self.ui.shema_listbox.currentItem()
            if not selected_item:
                QMessageBox.warning(self, "Ошибка", "Выберите шаблон!")
                return
                
            old_name = selected_item.text()
            new_name = self.ui.name_shema_textbox.toPlainText()
            
            # Проверка имени шаблона
            if not new_name:
                QMessageBox.warning(self, "Ошибка", "Имя шаблона не может быть пустым!")
                return
                
            if new_name in self.data and new_name != old_name:
                QMessageBox.warning(self, "Ошибка", "Шаблон с таким именем уже существует!")
                return
                
            # Проверка файлов
            gif_path = self.ui.alert_gif_textbox.toPlainText()
            audio_path = self.ui.allert_sound_path_textbox.toPlainText()
            
            if not gif_path or not audio_path:
                QMessageBox.warning(self, "Ошибка", "Не выбран файл Gif или Audio")
                return
                
            if not self._validate_files(gif_path, audio_path):
                return
                
            # Копирование файлов
            new_gif_path = self._copy_template_file(gif_path, "gifs", old_name)
            new_audio_path = self._copy_template_file(audio_path, "sounds", old_name)
            
            if not new_gif_path or not new_audio_path:
                QMessageBox.warning(self, "Ошибка", "Не удалось скопировать файлы")
                return
                
            # Обновление данных шаблона
            self._update_template_data(
                old_name,
                new_name,
                new_gif_path,
                new_audio_path
            )
            
            # Обновление UI
            selected_item.setText(new_name)
            self.update_template_style(selected_item)
            
            # Сохранение и обновление кошелька
            self.save_json(self.JSON_FILE_TEMPLATES, {"templates": self.data})
            self._update_wallet()
            
            QMessageBox.information(self, "Сохранено", "Настройки обновлены!")
            
        except Exception as e:
            logging.error(f"Ошибка при сохранении шаблона: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")

    # Вспомогательные методы
    def _validate_files(self, gif_path: str, audio_path: str) -> bool:
        """Проверяет существование файлов."""
        if not os.path.exists(audio_path):
            local_audio = self.path(self.LOCAL_PATH, "data", 'sounds', os.path.basename(audio_path))
            if not os.path.exists(local_audio):
                QMessageBox.warning(self, "Ошибка", "Файл Audio не существует!")
                return False
                
        if not os.path.exists(gif_path):
            local_gif = self.path(self.LOCAL_PATH, "data", 'gifs', os.path.basename(gif_path))
            if not os.path.exists(local_gif):
                QMessageBox.warning(self, "Ошибка", "Файл Gif не существует!")
                return False
                
        return True

    def _copy_template_file(self, src_path: str, dest_folder: str, template_name: str) -> str:
        """Копирует файл шаблона в нужную папку."""
        try:
            if not src_path:
                return ""
                
            # Проверяем, не пытаемся ли скопировать уже существующий файл
            current_path = self.data[template_name]["PATH"].get(
                "audio_path" if dest_folder == "sounds" else "gif_path", "")
            if os.path.basename(src_path) == os.path.basename(current_path):
                return current_path
                
            dest_dir = self.path(self.LOCAL_PATH, "data", dest_folder)
            os.makedirs(dest_dir, exist_ok=True)
            
            file_name = os.path.basename(src_path)
            new_path = os.path.join(dest_dir, file_name)
            
            # Обработка дубликатов
            counter = 1
            while os.path.exists(new_path):
                name, ext = os.path.splitext(file_name)
                new_path = os.path.join(dest_dir, f"{name}_{counter}{ext}")
                counter += 1
                
            shutil.copy(src_path, new_path)
            return os.path.basename(new_path)
            
        except Exception as e:
            logging.error(f"Ошибка копирования файла: {str(e)}")
            return None

    def _delete_template_files(self, template_name: str):
        """Удаляет файлы, связанные с шаблоном."""
        template_data = self.data.get(template_name, {})
        paths = template_data.get("PATH", {})
        
        try:
            if paths.get("gif_path"):
                gif_path = self.path(self.LOCAL_PATH, "data", "gifs", paths["gif_path"])
                if os.path.exists(gif_path):
                    os.remove(gif_path)
                    
            if paths.get("audio_path"):
                audio_path = self.path(self.LOCAL_PATH, "data", "sounds", paths["audio_path"])
                if os.path.exists(audio_path):
                    os.remove(audio_path)
                    
        except Exception as e:
            logging.error(f"Ошибка удаления файлов шаблона {template_name}: {str(e)}")
            raise

    def _update_template_data(self, old_name: str, new_name: str, gif_path: str, audio_path: str):
        """Обновляет данные шаблона."""
        template_data = self.data[old_name]
        
        # Обновляем настройки
        template_data["enabled"] = self.ui.checkBox.isChecked()
        template_data["ALERT_SETTINGS"] = {
            "duration": str(self.ui.text_duration_slider.value()),
            "scale": str(self.ui.volume_alert_slider.value()),
            "price": str(self.ui.alert_min_trigger_price_box.value())
        }
        
        # Обновляем пути
        template_data["PATH"] = {
            "audio_path": audio_path,
            "gif_path": gif_path
        }
        
        # Если изменилось имя, обновляем ключ
        if old_name != new_name:
            self.data[new_name] = template_data
            del self.data[old_name]

    def _update_wallet(self):
        """Обновляет экземпляр кошелька."""
        self.obs_wallet = Wallet(
            self.data_wallet["wallet_raw"],
            self.data_constants["jetton_master"],
            self.data_wallet["api_key"],
            self.data_constants["api_url"],
            db_path=self.path(self.LOCAL_PATH, self.data_constants["db_path"]),
            update_ui=self.update_table_view
        )

    # Методы для работы с UI
    def update_template_style(self, selected_item=None):
        """Обновляет стиль шаблона в списке."""
        if not selected_item:
            selected_item = self.ui.shema_listbox.currentItem()
            
        if not selected_item:
            return
            
        template_name = selected_item.text()
        is_enabled = self.data.get(template_name, {}).get("enabled", False)
        
        color = Qt.GlobalColor.green if is_enabled else Qt.GlobalColor.gray
        selected_item.setForeground(color)

    def update_list_widget(self):
        """Обновляет список шаблонов."""
        self.ui.shema_listbox.clear()
        for template_name in self.data:
            self.ui.shema_listbox.addItem(template_name)
        self._update_all_template_styles()

    def _update_all_template_styles(self):
        """Обновляет стили всех шаблонов в списке."""
        for i in range(self.ui.shema_listbox.count()):
            self.update_template_style(self.ui.shema_listbox.item(i))