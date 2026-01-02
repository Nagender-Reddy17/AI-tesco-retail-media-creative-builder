@echo off
echo ===============================
echo Tesco AI Creative Builder
echo ===============================

REM Create venv using SAME python that runs the script
py -3.8 -m venv venv

call venv\Scripts\activate

REM VERY IMPORTANT: use python -m pip
python -m pip install --upgrade pip
python -m pip install flask

python app.py

pause
