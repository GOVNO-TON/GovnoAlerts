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

import time

from PySide6.QtCore import QThread, QTimer
from PySide6.QtWidgets import QApplication, QHeaderView
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

class Worker(QThread):
    def __init__(self, wallet):
        super().__init__()
        self.wallet = wallet
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            sleep_s = self.wallet.monitor_wallet()
            print(sleep_s, "sleep slave")
            for _ in range(int(sleep_s * 10)):  # Ждём по 0.1 секунды
                if not self.running:
                    return
                time.sleep(0.1)  # Маленькие паузы не блокируют выход

    def stop(self):
        self.running = False
        self.wait()  # Ждём завершения потока


class MainTab():
    def __init__(self):
        self.timer_monitor = QTimer()  # Создаём таймер
        self.timer_monitor.timeout.connect(self.run_wallet_monitor)
        self.worker = None
        
    def toggle(self):
        """Переключение состояния кнопки (Старт/Стоп)"""
        self.is_running = not self.is_running  # Переключаем флаг
        if self.is_running:
            self.ui.Start_btn.setText("Стоп")  # Меняем текст кнопки
            print("Процесс запущен!")
            # Запускаем поток для мониторинга
            self.worker = Worker(self.obs_wallet)
            self.worker.start()
        else:
            self.ui.Start_btn.setText("Старт")
            print("Процесс остановлен!")
            if self.worker:
                self.worker.stop()  # Останавливаем поток

        self.ui.Start_btn.setEnabled(False)
        self.timer.start(2000)  # Запускаем таймер (2000 мс = 2 сек)

    def enable_button(self):
        """Снова активируем кнопку"""
        self.ui.Start_btn.setEnabled(True)
        self.timer.stop()  # Останавливаем таймер

    def copy_to_clickboard(self, label, text="_"):
        clipboard = QApplication.clipboard()
        label.setCursor(Qt.CursorShape.PointingHandCursor)
        if text == "_":
            label.mousePressEvent = lambda event: clipboard.setText(label.text())
        else:
            label.mousePressEvent = lambda event: clipboard.setText(text)

    def update_tab_main(self):
        self.ui.server_ip_label.setText(f"http://{self.data_constants['server_ip']}:{self.data_constants['server_port']}")
    
    def update_table_view(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(str(self.path(self.LOCAL_PATH, 'data', 'database', 'trans.db')))

        # try to open the database
        if not self.db.open():
            raise Exception("Could not open the database")
            

        # this will give you the whole table:
        self.model = QSqlTableModel(self, self.db)   
        query = QSqlQuery()
        query.exec_('SELECT donater_wallet, message, donate_amount, datatime FROM donates ORDER BY datatime DESC')
        self.model.setQuery(query)           
        self.model.select()
        self.ui.donate_table.setModel(self.model)
        QTimer.singleShot(0, self.setupColumns)
        self.db.close()
        QSqlDatabase.removeDatabase("qt_sql_default_connection")
        
    def setupColumns(self):
        # Настраиваем ширину столбцов
        header = self.ui.donate_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)  # Фиксированный размер столбцов

        # Устанавливаем ширину для каждого столбца
        self.ui.donate_table.setColumnWidth(0, 103)  # Ширина первого столбца
        self.ui.donate_table.setColumnWidth(1, 183)  # Ширина второго столбца
        self.ui.donate_table.setColumnWidth(2, 100)  # Ширина третьего столбца
        self.ui.donate_table.setColumnWidth(3, 120)  # Ширина четвёртого столбца