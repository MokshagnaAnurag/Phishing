@echo off
title NEURA - Fraud Detection System
color 0A

echo.
echo  ███╗   ███╗███████╗██╗   ██╗██████╗  █████╗ 
echo  ████╗ ████║██╔════╝██║   ██║██╔══██╗██╔══██╗
echo  ██╔████╔██║█████╗  ██║   ██║██████╔╝███████║
echo  ██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██╗██╔══██║
echo  ██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║██║  ██║
echo  ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
echo.
echo  AI-Powered Fraud ^& Phishing Detection System
echo  Think Smart. Stay Safe.
echo.
echo ================================================
echo  Choose an option:
echo ================================================
echo  1. Start Backend Server
echo  2. Open Web Test Interface
echo  3. Test API Endpoints
echo  4. Open Mobile App in Android Studio
echo  5. View Documentation
echo  6. Exit
echo ================================================
echo.

set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" (
    echo Starting backend server...
    cd backend
    python main.py
) else if "%choice%"=="2" (
    echo Opening web interface...
    start test_frontend.html
) else if "%choice%"=="3" (
    echo Testing API endpoints...
    python test_backend_fixed.py
    pause
) else if "%choice%"=="4" (
    echo Opening mobile app...
    start "" "mobile-app"
) else if "%choice%"=="5" (
    echo Opening documentation...
    start README.md
) else if "%choice%"=="6" (
    exit
) else (
    echo Invalid choice. Please try again.
    pause
    goto :eof
)