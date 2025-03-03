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

from PySide6.QtWidgets import QMessageBox
from Components.core.speaker import Speaker

class VoiceTab():
    def __init__(self):
        pass
    def setup_voice_tab(self):
        self.ui.change_lang_comboBox.setItemData(0, "ru")
        self.ui.change_lang_comboBox.setItemData(1, "en")
        self.ui.volume_slider.valueChanged.connect(lambda: self.update_label(self.ui.volume_slider, self.ui.voice_volume_label))
        self.ui.voice_volume_label.valueChanged.connect(self.ui.volume_slider.setValue)
        self.factor = 100
        self.ui.speed_slider.setMaximum(200)
        self.ui.speed_slider.valueChanged.connect(self.update_spinbox)
        self.ui.speed_slider.valueChanged.connect(self.update_spinbox)
        self.ui.voice_speed_label.valueChanged.connect(self.update_slider)
        self.ui.save_voice_settings_btn.clicked.connect(self.save_text_alerts)
        self.ui.test_msg_textbox_button.clicked.connect(self.play_test)
    
    def save_text_alerts(self):
        self.data_sound["pitch"] = str(self.ui.voice_speed_label.value())
        self.data_sound["scale"] = str(self.ui.volume_slider.value())
        self.data_sound["len_msg"] = str(self.ui.len_change_spinBox.value())
        self.data_sound["lang"] = str(self.ui.change_lang_comboBox.currentData())
        self.save_json(self.JSON_FILE_SOUND, {"settings": self.data_sound})
        QMessageBox.information(self, "Успех", "Настройки сохранены!")
    
    def play_test(self):
        scale = self.ui.volume_slider.value()
        pitch = self.ui.speed_slider.value() / 100
        lang = self.ui.change_lang_comboBox.currentData()
        text = self.ui.test_msg_textbox.toPlainText()
        
        Speaker(lang=lang, scale=scale, pitch=pitch, audio_path=str(self.path(self.LOCAL_PATH, "data", "sounds", "temp", "test_voice.mp3"))).play_sound(text)
        
    def update_voice_settings(self):
        """Загружает настройки и обновляет UI"""
        self.ui.volume_slider.setValue(int(self.data_sound["scale"]))
        self.ui.speed_slider.setValue(int(float(self.data_sound["pitch"])* 100))
        self.ui.len_change_spinBox.setValue(int(self.data_sound["len_msg"]))
        if self.data_sound["lang"] == "ru": 
            self.ui.change_lang_comboBox.setCurrentIndex(0)
        else: self.ui.change_lang_comboBox.setCurrentIndex(1)
        self.save_json(self.JSON_FILE_SOUND, {"settings": self.data_sound})