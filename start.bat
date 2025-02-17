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

:: ����� �ணࠬ��
echo ����� �ணࠬ��...
python src/main.py
pause