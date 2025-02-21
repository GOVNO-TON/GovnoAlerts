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
import pyaudio

from gtts import gTTS
from pydub import AudioSegment
from math import log10

class Speaker:
    def __init__(self, lang:str, scale: str, audio_path:str, pitch: str = "1"):
        self.__lang = lang
        self.__scale = scale
        self.__pitch = pitch
        self.__audio_path = audio_path
    
    def __audio_create(self, text: str, path: str = "_"):
        if path == "_":
            path = self.__audio_path
        tts = gTTS(text, lang=self.__lang)
        if os.name == "nt":
          tts.save(path)  
        else:
            tts.save(path)
        print("Файл 'voice.mp3' сохранён.")

    def audio_create_and_transform(self, text, file_path:str):
        if text:
            self.__audio_create(text=text)
        volume_increase_percent = int(self.__scale)  # Процент увеличения
        volume_increase_factor = 1 + (volume_increase_percent / 100)  # перевод процентов в коэфицент
        if volume_increase_factor:
            volume_increase_db = 20 * log10(volume_increase_factor)  # Переводим в dB
        
        
        audio = AudioSegment.from_file(file_path, format="mp3") 
       
        faster_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * float(self.__pitch))
        }).set_frame_rate(audio.frame_rate).apply_gain(volume_increase_db)
        
        faster_audio.export(f"{str(file_path)[:-4]}_fixed.mp3", format="mp3")
        return round(faster_audio.duration_seconds)
        
    def __playsound_win(self, file_path):
        # Загружаем MP3 файл с помощью pydub
        sound = AudioSegment.from_mp3(file_path)
        sound = sound.set_frame_rate(44100).set_channels(2).set_sample_width(2)
        # Преобразуем звук в байты для PyAudio
        raw_data = sound.raw_data
        # Инициализация PyAudio
        p = pyaudio.PyAudio()
        # Открытие потока воспроизведения
        stream = p.open(format=pyaudio.paInt16,
                        channels=2,
                        rate=44100,
                        output=True)

        # Воспроизведение звука
        stream.write(raw_data)

        # Закрытие потока
        stream.stop_stream()
        stream.close()
        p.terminate()

            
            
        
    # Воспроизведение
    def play_sound(self, text = False):
        if text:
            try:
                self.audio_create_and_transform(text, self.__audio_path)
            except Exception as e:
                print(f"Ошибка при формировании голосового сообщения: {e}")        
                return 0
            if os.name == "nt":
                self.__playsound_win(f"{self.__audio_path[:-4]}_fixed.mp3")  # Для Windows
            else:
                os.system(f"mpg123 {self.__audio_path[:-4]}_fixed.mp3")  # Для Linux/Macos

# if __name__ == "__main__":
#     from pathlib import Path
#     LOCAL_PATH = Path(__file__).resolve().parent.parent.parent.parent
#     test = Speaker("ru", scale=100, audio_path=Path(LOCAL_PATH, "data/sounds/temp/voice.mp3"), pitch=1.2)
#     # test.play_sound(text="тестируем текст", )
#     print(test.audio_create_and_transform(text='НУЖНО СЛИТЬ ЖЕТОНЫ $TONЧТОБЫ КЭШ ЗАЛИТЬ В $GOVNO ПОТОМ', file_path=Path(LOCAL_PATH, "data/sounds/temp/voice.mp3")))