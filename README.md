# NEURA - AI-Powered Fraud & Phishing Detection

**Think Smart. Stay Safe.**

A complete fraud and phishing detection system using Machine Learning and NLP.

## 🚀 Quick Start

### 1. Start Backend Server
```bash
# Double-click to start
start_server.bat

# Or manually
cd backend
python main.py
```
Server runs on `http://localhost:8000`

### 2. Test System
```bash
# Web interface
open test_frontend.html

# API test
python test_backend_fixed.py
```

### 3. Mobile App
- Open `mobile-app` in Android Studio
- Build and run on emulator/device

## 📂 Project Structure

```
NEURA/
├── backend/           # FastAPI server
│   ├── ml/           # ML integration
│   ├── main.py       # API server
│   └── requirements.txt
│
├── mobile-app/       # Android application
│   ├── app/
│   │   ├── src/main/java/com/neura/frauddetection/
│   │   └── build.gradle
│   └── build.gradle
│
├── ml-model/         # Machine Learning
│   ├── train.py      # Training script
│   ├── model.pkl     # Trained model
│   └── dataset.csv   # Training data
│
├── docs/             # Documentation
│
├── start_server.bat  # Quick start script
├── test_frontend.html # Web testing interface
└── test_backend_fixed.py # API test script
```

## 🎯 Features

### Backend API
- `/scan/sms` - SMS fraud detection
- `/scan/call` - Phone number verification  
- `/scan/email` - Email phishing detection
- `/scan/url` - URL malicious content analysis

### Mobile App
- Real-time scanning
- Scan history with Firebase
- Modern Material Design UI
- Automatic SMS monitoring

### Machine Learning
- Random Forest Classifier
- TF-IDF vectorization
- Rule-based fallback detection

## 📊 Test Results
- SMS Fraud Detection: **71.94% confidence**
- URL Malware Detection: **50% confidence**
- All endpoints operational

## 🔧 Configuration

### Mobile App API URL
- **Emulator**: `http://10.0.2.2:8000/` (default)
- **Physical Device**: Update to `http://YOUR_IP:8000/` in `ApiService.kt`

## 📱 Demo Examples
- **Fraud SMS**: "URGENT: Your account will be suspended. Click here to verify!"
- **Suspicious URL**: "http://suspicious-bank-verify.com/login"
- **Phishing Email**: "Verify your account immediately"

## 🛡️ Security Features
- Input validation
- Secure API communication
- Android permissions
- Firebase security

---

**Status**: ✅ Fully Operational | **Last Updated**: 2024