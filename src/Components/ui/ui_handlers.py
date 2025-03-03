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

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QFileDialog

class Handlers:
    def __init__(self):
        pass
    
    def make_label_clickable(self, label, url):
        """Добавляет к QLabel обработку клика"""
        label.setStyleSheet("color: blue; text-decoration: underline;")
        label.setCursor(Qt.CursorShape.PointingHandCursor)
        label.mousePressEvent = lambda event: self.open_link(url)
    
    def open_link(self, url):
        """Открывает ссылку в браузере"""
        QDesktopServices.openUrl(QUrl(url))
    
    def select_file(self, plain_text_edit, extension):
        """Открывает диалог выбора файла и записывает путь в QPlainTextEdit."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", f"{extension}")
        if file_path:
            plain_text_edit.setPlainText(file_path)
    
    def update_label(self, slider, label, flag=False, float=False):
        """Обновляет значение в QLabel при изменении ползунка."""
        if flag:
            label.setValue(int(slider.value() / 100))
        else:
            label.setValue(int(slider.value()))
        
        if float:
            label.setValue(slider.value() * 100)
    
    def update_spinbox(self, value):
        """Обновление QDoubleSpinBox при изменении QSlider"""
        self.ui.voice_speed_label.setValue(value / self.factor)

    def update_slider(self, value):
        """Обновление QSlider при изменении QDoubleSpinBox"""
        self.ui.speed_slider.setValue(int(value * self.factor))