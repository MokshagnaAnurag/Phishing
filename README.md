# NEURA - AI-Powered Fraud & Phishing Detection

**Think Smart. Stay Safe.**

A complete end-to-end fraud and phishing detection system that protects users from SMS scams, phishing emails, malicious URLs, and fraudulent phone calls using Machine Learning and NLP.

## 🎯 Project Overview

NEURA is a hackathon-ready, production-quality application consisting of:

- **Android Mobile App** (Kotlin) - User interface and real-time scanning
- **FastAPI Backend** (Python) - REST API server with ML integration
- **Machine Learning Engine** - Random Forest and Logistic Regression models
- **Firebase Firestore** - Cloud database for scan history

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Android Studio (Arctic Fox or later)
- Firebase account
- Java JDK 11+

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd NEURA
   ```

2. **Setup Backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Train ML Model**
   ```bash
   cd ../ml-model
   pip install -r requirements.txt
   python train.py
   ```

4. **Start Backend Server**
   ```bash
   cd ../backend
   python main.py
   ```
   Server runs on `http://localhost:8000`

5. **Setup Mobile App**
   - Open `mobile-app` in Android Studio
   - Sync Gradle files
   - Configure Firebase (see [docs/README.md](./docs/README.md))
   - Update API URL in `ApiService.kt` if needed
   - Build and run

## 📱 Features

### Mobile App
- ✅ Home dashboard with risk level indicator
- ✅ Manual scanning for SMS, calls, emails, URLs
- ✅ Automatic SMS scanning (with permission)
- ✅ Scan history with Firebase integration
- ✅ Settings and configuration
- ✅ Modern, clean UI with Material Design

### Backend API
- ✅ `/scan/sms` - SMS fraud detection
- ✅ `/scan/call` - Phone number verification
- ✅ `/scan/email` - Email phishing detection
- ✅ `/scan/url` - URL malicious content analysis
- ✅ Health check endpoint
- ✅ CORS enabled for mobile app

### Machine Learning
- ✅ Random Forest Classifier (primary model)
- ✅ Logistic Regression (backup model)
- ✅ TF-IDF vectorization
- ✅ Text preprocessing and feature extraction
- ✅ Rule-based fallback detection

## 📂 Project Structure

```
NEURA/
├── mobile-app/              # Android application
│   ├── app/
│   │   ├── src/main/
│   │   │   ├── java/com/neura/frauddetection/
│   │   │   │   ├── activities/    # App screens
│   │   │   │   ├── adapters/     # RecyclerView adapters
│   │   │   │   ├── models/       # Data models
│   │   │   │   ├── network/      # API service
│   │   │   │   └── utils/        # Utilities
│   │   │   └── res/              # Resources
│   │   └── build.gradle
│   └── build.gradle
│
├── backend/                 # FastAPI server
│   ├── main.py             # API server entry point
│   ├── ml/
│   │   └── fraud_detector.py  # ML integration
│   └── requirements.txt
│
├── ml-model/               # ML training
│   ├── train.py           # Training script
│   ├── preprocess.py      # Preprocessing utilities
│   ├── dataset.csv        # Sample dataset
│   └── requirements.txt
│
└── docs/                   # Documentation
    ├── README.md
    ├── API_Documentation.md
    └── Architecture.md
```

## 🧪 Testing

### Test the API

```bash
# Health check
curl http://localhost:8000/health

# Scan SMS
curl -X POST http://localhost:8000/scan/sms \
  -H "Content-Type: application/json" \
  -d '{"text": "URGENT: Your account will be suspended"}'

# Scan URL
curl -X POST http://localhost:8000/scan/url \
  -H "Content-Type: application/json" \
  -d '{"url": "http://example.com"}'
```

### Test the Mobile App

1. Launch the app on emulator or device
2. Grant SMS permissions when prompted
3. Use "Quick Scan" buttons to test different scan types
4. Check "History" to view past scans

## 📊 API Documentation

See [docs/API_Documentation.md](./docs/API_Documentation.md) for complete API reference.

## 🏗️ Architecture

See [docs/Architecture.md](./docs/Architecture.md) for detailed system architecture.

## 🔧 Configuration

### Backend API URL

Update in `mobile-app/app/src/main/java/com/neura/frauddetection/network/ApiService.kt`:

- **Emulator**: `http://10.0.2.2:8000/`
- **Physical Device**: `http://YOUR_COMPUTER_IP:8000/`

### Firebase Setup

1. Create project at https://console.firebase.google.com
2. Enable Firestore Database
3. Download `google-services.json`
4. Place in `mobile-app/app/` directory
5. Add Firebase SDK (already in build.gradle)

## 🛡️ Security Features

- Input validation on all endpoints
- Secure API communication
- Android permissions properly requested
- Firebase security (configure rules in console)

## 📈 Future Enhancements

- Real-time threat intelligence
- Advanced NLP models (BERT, GPT)
- Community reporting system
- Multi-language support
- Enhanced phone number database
- URL reputation checking
- Behavioral analysis
- Push notifications

## 🐛 Troubleshooting

**Backend not connecting:**
- Ensure backend is running on port 8000
- Check firewall settings
- Verify network connectivity

**ML model errors:**
- Run `python train.py` in `ml-model/` directory
- Check that `model.pkl` and `vectorizer.pkl` exist

**Firebase errors:**
- Verify `google-services.json` is in correct location
- Check Firebase project configuration
- Ensure Firestore is enabled

## 📄 License

Created for hackathon demonstration purposes.

## 👥 Team

NEURA Team - Hackathon 2024

---

**NEURA - Think Smart. Stay Safe.**

For detailed documentation, see the [docs](./docs/) directory.


