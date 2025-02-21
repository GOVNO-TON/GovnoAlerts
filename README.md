# GovnoAlerts — Кроссплатформенное приложение для криптовалютных донатов стримерам

**GovnoAlerts** — это удобное решение для стримеров, которые хотят принимать донаты от своих зрителей в криптовалюте. Проект позволяет легко интегрировать прием криптовалютных платежей в стримы, обеспечивая безопасность, анонимность и поддержку  популярной инновационной криптовалюты.

## Основные возможности

- **Поддержка инновационной криптовалюты**: Работа с криптовалютой [$GOVNO](https://tonviewer.com/EQBlWgKnh_qbFYTXfKgGAQPxkxFsArDOSr9nlARSzydpNPwA) на блокчейне TON.
- **Простая интеграция**: Легко подключите прием донатов к вашему стриму.
- **Анонимность**: Зрители могут отправлять донаты без необходимости регистрации.
- **Мгновенные уведомления**: Получайте уведомления о донатах прямо во время стрима.
- **Прозрачность**: Все транзакции отображаются в приложении.
- **Независимость**: Полное отсутствие комиссий для стримеров. Деньги приходят сразу на ваш кошелёк.

## Установка
0. Для MacOS и Linux может потребоваться PortAudio

MacOS:

``` 
brew install portaudio
```

Ubuntu Linux:

```
sudo apt install portaudio19-dev
```

Чтобы начать использовать GovnoAlerts, выполните следующие шаги:

>### UPDATE
>Для Windows и MacOS были выпущены скрипты автоматической установки и запуска: start.bat и start.command соответственно.
>
>С помощью них можно запускать программу. Первичный запуск скрипта автоматически выполнит установку, а последующие запуски будут открывать программу(не переустанавливать).
>
>Запускать скрипт можно после выполнения шага №2


1. Убедитесь, что у вас установлен Python 3.12. Если нет, скачайте его с [официального сайта](https://www.python.org/downloads/release/python-3129/).

2. Клонируйте репозиторий:
   ```
   git clone https://github.com/GOVNO-TON/GovnoAlerts.git
   cd GovnoAlerts
   ```

3. Создайте виртуальное окружение (рекомендуется):
    Для Windows:
    ```
    py -3.12 -m venv venv
    venv\Scripts\activate
    ```
    Для Linux/MacOS:    
   ```
    python3.12 -m venv venv
    source venv/bin/activate 

    ```
5. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```
6. Запустите проект:

    ```
    python src/main.py
    ```
7. Настройте конфигурацию в настройках программы:
- Укажите API - ключ [TonCenter](https://t.me/toncenter);
- Укажите кошелёк TON на который хотите получать донаты;
- Создайте шаблоны для реакции на донаты
- Укажите длину, громкость и скорость воспроизведения текста.

## Интеграция с OBS
Добавьте браузерный источник:
- Откройте OBS.
- В разделе "Источники" нажмите на "+" и выберите "Браузер".
- Назовите источник, например, "GovnoAlerts Widget".
- Укажите ширину и высоту виджета (например, 400x200).
- Нажмите "ОК".

Настройте источник:
- В поле "URL" вставьте ссылку на ваш виджет - GovnoAlerts http://localhost:5455/;
- Поставьте галочку в пункте "Управление аудио через OBS";
- Нажмите кнопку "Обновить кэш текущей страницы"(Кнопку нужно нажимать каждый раз при повторном запуске OBS и открытой программе)

# Авторы
## Автор идеи v32ode - [Telegram_link](https://t.me/v32ode)
## [Github:Oppj4](https://github.com/oppj4).............[Telegram_link](https://t.me/LanArch1)
## [Github:cathome1](https://github.com/cathome1)......[Telegram_link](https://t.me/cathome)

## Поддержать разработчиков
TON:

**UQBn0pRJvGJHOio-sIIc-Txkj1AJjpOfOI7fGzvo2DmBglVd**

# Лицензия
Этот проект распространяется под лицензией Apache 2.0. Подробнее см. в файле [LICENSE](LICENSE).

© Copyright 2025 oppj4, cathome1, GOVNO-TON

## Лицензии сторонних библиотек

Этот проект использует следующие сторонние библиотеки, каждая из которых распространяется под своей лицензией:

### Библиотеки и их лицензии

- **blinker** — [MIT License](LICENSES/MIT_LICENSE.txt)
- **certifi** — [MPL-2.0 License](LICENSES/MPL_LICENSE.txt)
- **cffi** — [MIT License](LICENSES/MIT_LICENSE.txt)
- **charset-normalizer** — [MIT License](LICENSES/MIT_LICENSE.txt)
- **click** — [BSD-3-Clause License](LICENSES/BSD_LICENSE.txt)
- **colorama** — [BSD-3-Clause License](LICENSES/BSD_LICENSE.txt)
- **cryptography** — [Apache-2.0 License](LICENSES/APACHE_LICENSE.txt)
- **Flask** — [BSD-3-Clause License](LICENSES/BSD_LICENSE.txt)
- **FFmpeg** — [LGPL-3.0-only License](LICENSES/LGPL_LICENSE.txt)
- **gTTS** — [MIT License](LICENSES/MIT_LICENSE.txt)
- **idna** — [BSD-3-Clause License](LICENSES/BSD_LICENSE.txt)
- **itsdangerous** — [BSD-3-Clause License](LICENSES/BSD_LICENSE.txt)
- **Jinja2** — [BSD-3-Clause License](LICENSES/BSD_LICENSE.txt)
- **MarkupSafe** — [BSD-3-Clause License](LICENSES/BSD_LICENSE.txt)
- **PyAudio** — [MIT License](LICENSES/MIT_LICENSE.txt)
- **pycparser** — [BSD-3-Clause License](LICENSES/BSD_LICENSE.txt)
- **pydub** — [MIT License](LICENSES/MIT_LICENSE.txt)
- **PySide6** — [LGPL-3.0-only License](LICENSES/LGPL_LICENSE.txt)
- **PySide6_Addons** — [LGPL-3.0-only License](LICENSES/LGPL_LICENSE.txt)
- **PySide6_Essentials** — [LGPL-3.0-only License](LICENSES/LGPL_LICENSE.txt)
- **requests** — [Apache-2.0 License](LICENSES/APACHE_LICENSE.txt)
- **shiboken6** — [LGPL-3.0-only License](LICENSES/LGPL_LICENSE.txt)
- **urllib3** — [MIT License](LICENSES/MIT_LICENSE.txt)
- **Werkzeug** — [BSD-3-Clause License](LICENSES/BSD_LICENSE.txt)

### Файлы лицензий

Все лицензионные файлы находятся в папке `LICENSES`. Вы можете ознакомиться с полными текстами лицензий по следующим ссылкам:

- [MIT License](LICENSES/MIT_LICENSE.txt)
- [BSD-3-Clause License](LICENSES/BSD_LICENSE.txt)
- [Apache-2.0 License](LICENSES/APACHE_LICENSE.txt)
- [LGPL-3.0-only License](LICENSES/LGPL_LICENSE.txt)
- [MPL-2.0 License](LICENSES/MPL_LICENSE.txt)

### Уведомление об авторских правах

Информация об авторах и правообладателях сторонних библиотек находится в файле [NOTICE](NOTICE).