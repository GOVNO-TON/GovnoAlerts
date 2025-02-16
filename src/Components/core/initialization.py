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

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from Components.core.json_handler import JsonHandler
from Components.core.json_handler import json
from pathlib import Path

from sys import exit as ex

import threading 
import sqlite3

class InitBlock(JsonHandler):
    def __init__(self):
        super().__init__()
        self.path = Path
        self.th = threading

        self.data = self.load_json(self.JSON_FILE_TEMPLATES, {"templates": {}})["templates"]
        self.data_sound = self.load_json(self.JSON_FILE_SOUND, {"settings": {}})["settings"]
        self.data_wallet = self.load_json(self.JSON_FILE_WALLET, {"wallet_settings": {}})["wallet_settings"]
        self.data_constants = self.load_json(self.JSON_FILE_CONSTANTS, {"constants": {}})["constants"]

        if not self.data_wallet:
            self.data_wallet = {
                "api_url" : "https://toncenter.com/api/v3/",
                "api_key" : "",
                "wallet_raw" : ""
            }
            self.save_json(self.JSON_FILE_WALLET, {"wallet_settings":self.data_wallet})

        if not self.data_sound:
            self.data_sound = {
                "lang": "ru",
                "pitch": "100",
                "scale": "-20",
                "len_msg" : "200",
            }
            self.save_json(self.JSON_FILE_SOUND, {"settings": self.data_sound})

        if not self.data_constants:
            self.data_constants = {
                "api_url": "https://toncenter.com/api/v3/",
                "sleep_interval": 60,
                "audio_path": "data/sounds/",
                "voice_path": "data/sounds/temp/voice.mp3",
                "media_path": "data/",
                "server_ip": "127.0.0.1", 
                "server_port": "5455",
                "db_path": "data/database/trans.db",
                "jetton_master": "EQBlWgKnh_qbFYTXfKgGAQPxkxFsArDOSr9nlARSzydpNPwA"
            }
            self.save_json(self.JSON_FILE_CONSTANTS, {"constants": self.data_constants})

        conn = sqlite3.connect(Path(self.LOCAL_PATH, self.data_constants["db_path"]))
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS donates (
                            id INTEGER PRIMARY KEY, 
                            trans_hash TEXT UNIQUE, 
                            donate_amount REAL,
                            donater_wallet TEXT,
                            message TEXT,
                            datatime timestamp
                        )''')
        conn.commit()
        conn.close()
        
        # HTML-шаблон (widget/index.html)
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OBS Donations</title>
    <style>
        @font-face {
            font-family: 'Inter-700';
            src: url('/fonts/Inter-700.woff2') format('woff2');
            font-weight: normal;
            font-style: normal;
        }

        body {
            text-align: center;
            background-color: black;
            color: white;
            font-family: Arial, sans-serif;
        }

        #donation-box {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 24px;
            display: none;
            font-family: 'Inter-600', sans-serif;
        }

        img {
            max-width: 100%;
        }
    </style>
</head>
<body>
    <div id="donation-box"></div>
    <audio id="sound1"></audio>
    <audio id="sound2"></audio>

    <script>
        let lastDonationId = null;

        async function fetchDonations() {
            let response = await fetch('/get_donations');
            let donations = await response.json();

            if (donations.length === 0) return;

            let lastDonation = donations[donations.length - 1];

            if (lastDonationId === lastDonation.id) return;
            lastDonationId = lastDonation.id;

            let donationBox = document.getElementById('donation-box');
            donationBox.innerHTML = `
                <img id="donation-gif" src="${lastDonation.gif}" alt="Donation GIF"><br>
                <strong>${lastDonation.name}</strong><br> 
                ${lastDonation.message}
            `;
            donationBox.style.display = "block";

            let sound1 = document.getElementById('sound1');
            let sound2 = document.getElementById('sound2');

            sound1.src = lastDonation.sound1;
            sound2.src = lastDonation.sound2;

            if (sound2.getAttribute("src") === "-") {
                sound1.play().catch(console.error);
            } else {
                sound1.play().then(() => {
                    sound1.onended = () => sound2.play();
                }).catch(console.error);
            }

            setTimeout(() => {
                donationBox.style.display = "none";
            }, lastDonation.duration);
        }

        setInterval(fetchDonations, 3000);
    </script>
</body>
</html>
    """
        with open(Path(self.LOCAL_PATH, "data", "widget", "index.html"), "w", encoding="utf-8") as file:
            file.write(html_content) 
    def check_license(self):
        with open("src/Components/core/verify/public_key.pem", "rb") as public_key_file:
            public_key = serialization.load_pem_public_key(public_key_file.read())

        with open("src/Components/core/verify/signature.sig", "rb") as sig_file:
            signature = sig_file.read()
            
        with open("src/Components/assets/donate_qr.png", "rb") as f:
            binary_qr = f.read()
        
        data = {
            "w_donate": self.ui.donate_disig_wallet_label.text(),
            "w_jetton": self.data_constants["jetton_master"],  
            "qr_code": binary_qr.hex(),  
            "tg_link_1": self.tg_link_1,
            "tg_link_2": self.tg_link_2,
            "tg_user_1": self.ui.telegram_link_1.text(),
            "tg_user_2": self.ui.telegram_link_2.text()
        }
        json_data = json.dumps(data, sort_keys=True)
        
        try:
            public_key.verify(
                signature,
                json_data.encode(),
                padding.PKCS1v15(),
                hashes.SHA256()
            )

        except Exception as e:
            ex()
            
if __name__ == "__main__":
    obj = InitBlock()
    pass