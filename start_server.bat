@echo off
echo ================================================
echo NEURA - AI-Powered Fraud Detection System
echo ================================================
echo.

echo 1. Training enhanced ML models with Kaggle datasets...
if not exist "ml-model\model_enhanced.pkl" (
    echo Training enhanced models...
    cd ml-model
    python train_enhanced.py
    cd ..
) else (
    echo ✅ Enhanced ML models found
)

echo.
echo 2. Starting backend server...
echo Server will be available at: http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.

cd backend
python main.py