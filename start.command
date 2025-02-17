#!/bin/bash

# Переход в директорию проекта
cd "$(dirname "$0")"

# Проверка наличия Python 3.12
if ! command -v python3.12 &> /dev/null; then
  echo "Python 3.12 не найден."
  echo "Установите Python 3.12 с помощью Homebrew:"
  echo "1. Установите Homebrew, если он ещё не установлен:"
  echo '   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
  echo "2. Установите Python 3.12:"
  echo "   brew install python@3.12"
  echo "3. Добавьте Python 3.12 в PATH:"
  echo '   echo "export PATH=\"/usr/local/opt/python@3.12/bin:\$PATH\"" >> ~/.zshrc'
  echo "4. Перезагрузите терминал и запустите этот скрипт снова."
  exit 1
fi

# Проверка существования виртуального окружения
if [ ! -d "venv" ]; then
  echo "Создание виртуального окружения..."
  python3.12 -m venv venv
  source venv/bin/activate
  echo "Установка зависимостей..."
  pip install -r requirements.txt
else
  echo "Активация виртуального окружения..."
  source venv/bin/activate
fi

# Запуск программы
echo "Запуск программы..."
python src/main.py  # Замени main.py на имя твоего скрипта