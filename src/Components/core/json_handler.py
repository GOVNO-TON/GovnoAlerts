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

import json
from pathlib import Path

class JsonHandler:
    def __init__(self):
        self.LOCAL_PATH = Path(__file__).resolve().parent.parent.parent.parent
        self.JSON_FILE_TEMPLATES = str(Path(self.LOCAL_PATH, "config", "alerts_templates.json"))
        self.JSON_FILE_SOUND = str(Path(self.LOCAL_PATH, "config", "text_alerts_settings.json"))
        self.JSON_FILE_WALLET = str(Path(self.LOCAL_PATH, "config", "wallet_settings.json"))
        self.JSON_FILE_CONSTANTS = str(Path(self.LOCAL_PATH, "config", "constant_values.json"))
        self.JSON_FILE_FILTER = str(Path(self.LOCAL_PATH, "config", "blacklist.json"))

    def load_json(self, f_name, template):
        """Загружает JSON-файл с настройками."""
        try:
            with open(f_name, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return template  # Если файла нет, создаём пустую структуру

    def save_json(self, f_name, data):
        """Сохраняет данные в JSON-файл."""
        with open(f_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    