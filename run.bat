@echo off
title Pixel Art AI Studio - Server
chcp 65001 >nul
cls

echo ========================================================
echo          👾 PIXEL ART AI STUDIO - BACKEND SERVER
echo ========================================================
echo.

cd /d "%~dp0"

if not exist "venv\Scripts\activate.bat" (
    echo [LOI] Khong tim thay moi truong ao 'venv'!
    echo Vui long mo terminal chay: python -m venv venv ^&^& pip install -r requirements.txt
    pause
    exit /b
)

echo [*] Dang kich hoat moi truong ao (venv)...
call venv\Scripts\activate.bat

echo [*] Dang mo trinh duyet web...
start "" http://127.0.0.1:8000

echo [*] Dang khoi chay FastAPI Backend tai http://127.0.0.1:8000 ...
echo [*] Nhan Ctrl + C de dung server bat cu luc nao.
echo.
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload

pause
