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

from Components.ui.main_window import MainApp
from PySide6 import QtWidgets 
from Components.core.stream_alert import Server
from Components.core.initialization import InitBlock

import sys

class Main(InitBlock):
    def __init__(self):
        super().__init__()
        server = Server(server_ip=self.data_constants["server_ip"], server_port=self.data_constants["server_port"], server_path=self.path(self.LOCAL_PATH, self.data_constants["media_path"]))
        self.th.Thread(target=server.run_server, daemon=True).start()

        app = QtWidgets.QApplication(sys.argv)
        main_window = MainApp()
        main_window.show()
        sys.exit(app.exec_())
        

# Запуск приложения
if __name__ == "__main__":
    Main()
    
