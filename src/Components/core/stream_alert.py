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

import threading
import time
import os
import uuid

from flask import Flask, render_template, request, jsonify, send_from_directory

class Server:
    
    def __init__(self, server_path, server_ip, server_port):
        
        self.app = Flask(__name__, template_folder=os.path.join(server_path, "widget"))
        self.server_path = server_path
        self.server_ip = server_ip
        self.server_port = server_port
        self.__donations = []  # Хранилище донатов
        
        os.makedirs(os.path.join(server_path, "widget"), exist_ok=True)
        os.makedirs(os.path.join(server_path, "widget", "fonts"), exist_ok=True)
        os.makedirs(os.path.join(server_path, "sounds"), exist_ok=True)
        os.makedirs(os.path.join(server_path, "gifs"), exist_ok=True)

        # Регистрация маршрутов
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/donate', 'donate', self.donate, methods=['POST'])
        self.app.add_url_rule('/get_donations', 'get_donations', self.get_donations)
        self.app.add_url_rule('/fonts/<path:filename>', 'serve_font', self.serve_font)
        self.app.add_url_rule('/sounds/<path:filename>', 'serve_sound', self.serve_sound)
        self.app.add_url_rule('/gifs/<path:filename>', 'serve_gif', self.serve_gif)

    def clear_donations(self):
        """Функция очистки донатов после показа."""
        while True:
            time.sleep(10)  # Интервал очистки
            if len(self.__donations) > 1:
                self.__donations.pop(0)

    def index(self):
        return render_template('index.html')

    def donate(self):
        data = request.json
        if not all(k in data for k in ['name', 'message', 'sound1', 'sound2', 'gif']):
            return jsonify({"error": "Missing required fields"}), 400

        donation_data = {
            'id': str(uuid.uuid4()),
            'name': data['name'],
            'message': data['message'],
            'sound1': f"/sounds/{data['sound1']}",
            'sound2': f"/sounds/temp/{data['sound2']}" if data['sound2'] != "-" else "-",
            'gif': f"/gifs/{data['gif']}",
            'duration': data.get('duration', 5000)
        }
        self.__donations.append(donation_data)
        return jsonify({"status": "success"})

    def get_donations(self):
        return jsonify(self.__donations)

    def serve_sound(self, filename):
        return send_from_directory(os.path.join(self.server_path, 'sounds'), filename)

    def serve_gif(self, filename):
        return send_from_directory(os.path.join(self.server_path, 'gifs'), filename)
    
    def serve_font(self, filename):
        return send_from_directory(os.path.join(self.server_path, 'widget', 'fonts'), filename)

    def run_server(self):
        threading.Thread(target=self.clear_donations, daemon=True).start()
        self.app.run(host=self.server_ip, port=int(self.server_port))



if __name__ == '__main__':
    server_instance = Server(server_path="static/", server_ip="127.0.0.1", server_port=5455)
    server_instance.run_server()
