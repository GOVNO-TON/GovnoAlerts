@echo off
:: ���室 � ��४��� �஥��
cd /d %~dp0

:: �஢�ઠ ������ Python 3.12
py -3.12 --version >nul 2>&1

if %errorlevel% neq 0 (
  echo Python 3.12 �� ������.
  echo ��⠭���� Python 3.12:
  echo 1. ���砩� ��⠭��騪 � https://www.python.org/downloads/release/python-3129/
  echo 2. ��������, �� �� ��ࠫ� ���� "Add Python to PATH" �� ��⠭����.
  echo 3. ��१������ ��� �ਯ� ��᫥ ��⠭����.
  
  pause
  exit /b 1
)

:: �஢�ઠ ����⢮����� ����㠫쭮�� ���㦥���
if not exist "venv" (
  echo �������� ����㠫쭮�� ���㦥���...
  py -3.12 -m venv venv
  call venv\Scripts\activate.bat
  echo ��⠭���� ����ᨬ��⥩...
  pip install -r requirements.txt
) else (
  echo ��⨢��� ����㠫쭮�� ���㦥���...
  call venv\Scripts\activate.bat
)

:: �஢�ઠ � ��⠭���� FFmpeg
setlocal EnableDelayedExpansion

set "folderPath=%~dp0venv\Scripts"
set "ffmpegUrl=https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-lgpl.zip"
set "zipFile=ffmpeg.zip"
set "extractedFolder=%folderPath%\ffmpeg-master-latest-win64-lgpl"
set "requiredFiles=ffmpeg.exe ffprobe.exe ffplay.exe"

cd /d "%folderPath%" || (echo �訡��: ���������� ��३� � ����� %folderPath%. && pause && exit /b 1)

:: �஢�ઠ ������ 䠩���
set "missingFiles=0"
echo �஢�ઠ ��⠭���� FFmpeg � ���⠫쭮� ���㦥���
for %%f in (%requiredFiles%) do (
    if not exist "%%f" (
        echo ���� %%f ���������.
        set "missingFiles=1"
    )
)

:: �᫨ �� 䠩�� �� ����, ���室�� � ������ �ணࠬ��
if !missingFiles!==0 (
    echo �� ����室��� 䠩�� FFmpeg �������.
) else (
    echo ������� 䠩�� FFmpeg ����������. ��稭��� ����㧪� � ��⠭����...

    :: ���稢���� FFmpeg � �ண��ᮬ
    echo ���稢���� FFmpeg...
    powershell -Command "$url = '%ffmpegUrl%'; $output = '%zipFile%'; $webClient = New-Object System.Net.WebClient; $total = [System.Net.WebRequest]::Create($url).GetResponse().ContentLength; $job = Start-Job -ScriptBlock { param($url, $output) $client = New-Object System.Net.WebClient; $client.DownloadFile($url, $output) } -ArgumentList $url, $output; while ($job.State -eq 'Running') { if (Test-Path $output) { $size = (Get-Item $output).Length; $percent = [math]::Min(($size / $total * 100), 100); Write-Progress -Activity '����㧪� 䠩��' -Status ('{0} KB ����㦥��' -f ($size / 1KB)) -PercentComplete $percent }; Start-Sleep -Milliseconds 500 }; Receive-Job $job; Remove-Job $job"
    :: �஢�ઠ �ᯥ譮�� ᪠稢����
    if not exist "!zipFile!" (
        echo �訡��: �� 㤠���� ᪠��� FFmpeg.
        pause
        exit /b 1
    )

    :: ��ᯠ����� ��娢�
    echo ��ᯠ����� ��娢�...
    powershell -Command "Expand-Archive -Path '!zipFile!' -DestinationPath '!folderPath!' -Force"

    :: �������� ��娢�
    del "!zipFile!"

    :: ��६�饭�� 䠩��� �� ����� bin
    if exist "!extractedFolder!" (
        echo ��६�饭�� 䠩��� �� ����� bin...
        move "!extractedFolder!\bin\*" "!folderPath!"
        rmdir /s /q "!extractedFolder!"
    ) else (
        echo �訡��: ����� !extractedFolder! �� �������.
        pause
        exit /b 1
    )

    :: �஢�ઠ ������ 䠩��� ��᫥ ��६�饭��
    set "missingFiles=0"
    for %%f in (!requiredFiles!) do (
        if not exist "%%f" (
            echo �訡��: ���� %%f �� ������ ��᫥ ��६�饭��.
            set "missingFiles=1"
        )
    )

    :: �����襭�� �஢�ન FFmpeg
    if !missingFiles!==0 (
        echo FFmpeg �ᯥ譮 ��⠭�����.
    ) else (
        echo �訡��: �� �� 䠩�� FFmpeg �������.
        pause
        exit /b 1
    )
)

cd /d %~dp0
:: ����� �ணࠬ��
echo ����� �ணࠬ��...
python src/main.py
pause