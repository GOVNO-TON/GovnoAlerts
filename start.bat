@echo off
:: Переход в директорию проекта
cd /d %~dp0

:: Проверка наличия Python 3.12
py -3.12 --version >nul 2>&1

if %errorlevel% neq 0 (
  echo Python 3.12 не найден.
  echo Установите Python 3.12:
  echo 1. Скачайте установщик с https://www.python.org/downloads/release/python-3129/
  echo 2. Убедитесь, что вы выбрали опцию "Add Python to PATH" при установке.
  echo 3. Перезапустите этот скрипт после установки.
  
  pause
  exit /b 1
)

:: Проверка существования виртуального окружения
if not exist "venv" (
  echo Создание виртуального окружения...
  py -3.12 -m venv venv
  call venv\Scripts\activate.bat
  echo Установка зависимостей...
  pip install -r requirements.txt
) else (
  echo Активация виртуального окружения...
  call venv\Scripts\activate.bat
)

:: Запуск программы
echo Запуск программы...
python src/main.py
pause