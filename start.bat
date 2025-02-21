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

:: Проверка и установка FFmpeg
setlocal EnableDelayedExpansion

set "folderPath=%~dp0venv\Scripts"
set "ffmpegUrl=https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-lgpl.zip"
set "zipFile=ffmpeg.zip"
set "extractedFolder=%folderPath%\ffmpeg-master-latest-win64-lgpl"
set "requiredFiles=ffmpeg.exe ffprobe.exe ffplay.exe"

cd /d "%folderPath%" || (echo Ошибка: Невозможно перейти в папку %folderPath%. && pause && exit /b 1)

:: Проверка наличия файлов
set "missingFiles=0"
echo Проверка установки FFmpeg в виртальном окружении
for %%f in (%requiredFiles%) do (
    if not exist "%%f" (
        echo Файл %%f отсутствует.
        set "missingFiles=1"
    )
)

:: Если все файлы на месте, переходим к запуску программы
if !missingFiles!==0 (
    echo Все необходимые файлы FFmpeg найдены.
) else (
    echo Некоторые файлы FFmpeg отсутствуют. Начинаем загрузку и установку...

    :: Скачивание FFmpeg с прогрессом
    echo Скачивание FFmpeg...
    powershell -Command "$url = '%ffmpegUrl%'; $output = '%zipFile%'; $webClient = New-Object System.Net.WebClient; $total = [System.Net.WebRequest]::Create($url).GetResponse().ContentLength; $job = Start-Job -ScriptBlock { param($url, $output) $client = New-Object System.Net.WebClient; $client.DownloadFile($url, $output) } -ArgumentList $url, $output; while ($job.State -eq 'Running') { if (Test-Path $output) { $size = (Get-Item $output).Length; $percent = [math]::Min(($size / $total * 100), 100); Write-Progress -Activity 'Загрузка файла' -Status ('{0} KB загружено' -f ($size / 1KB)) -PercentComplete $percent }; Start-Sleep -Milliseconds 500 }; Receive-Job $job; Remove-Job $job"
    :: Проверка успешности скачивания
    if not exist "!zipFile!" (
        echo Ошибка: Не удалось скачать FFmpeg.
        pause
        exit /b 1
    )

    :: Распаковка архива
    echo Распаковка архива...
    powershell -Command "Expand-Archive -Path '!zipFile!' -DestinationPath '!folderPath!' -Force"

    :: Удаление архива
    del "!zipFile!"

    :: Перемещение файлов из папки bin
    if exist "!extractedFolder!" (
        echo Перемещение файлов из папки bin...
        move "!extractedFolder!\bin\*" "!folderPath!"
        rmdir /s /q "!extractedFolder!"
    ) else (
        echo Ошибка: Папка !extractedFolder! не найдена.
        pause
        exit /b 1
    )

    :: Проверка наличия файлов после перемещения
    set "missingFiles=0"
    for %%f in (!requiredFiles!) do (
        if not exist "%%f" (
            echo Ошибка: Файл %%f не найден после перемещения.
            set "missingFiles=1"
        )
    )

    :: Завершение проверки FFmpeg
    if !missingFiles!==0 (
        echo FFmpeg успешно установлен.
    ) else (
        echo Ошибка: Не все файлы FFmpeg найдены.
        pause
        exit /b 1
    )
)

cd /d %~dp0
:: Запуск программы
echo Запуск программы...
python src/main.py
pause