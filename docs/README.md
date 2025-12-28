# NEURA - AI-Powered Fraud & Phishing Detection

**Think Smart. Stay Safe.**

NEURA is a comprehensive fraud and phishing detection system that protects users from SMS scams, phishing emails, malicious URLs, and fraudulent phone calls using Machine Learning and NLP.

## 🏗️ Project Structure

```
NEURA/
├── mobile-app/          # Android mobile application (Kotlin)
├── backend/            # FastAPI backend server (Python)
├── ml-model/           # Machine Learning models and training
└── docs/               # Documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Android Studio (for mobile app)
- Firebase account (for database)
- Java JDK 11+

### 1. Backend Setup

```bash
cd backend
pip install -r requirements.txt

# Train the ML model first
cd ../ml-model
pip install -r requirements.txt
python train.py

# Start the backend server
cd ../backend
python main.py
```

The API will be available at `http://localhost:8000`

### 2. Mobile App Setup

1. Open Android Studio
2. Open the `mobile-app` folder
3. Sync Gradle files
4. Configure Firebase:
   - Create a Firebase project
   - Download `google-services.json` and place it in `mobile-app/app/`
5. Update API URL in `ApiService.kt`:
   - For emulator: `http://10.0.2.2:8000/`
   - For physical device: `http://YOUR_COMPUTER_IP:8000/`
6. Build and run the app

### 3. ML Model Training

The ML model is pre-trained, but you can retrain it:

```bash
cd ml-model
python train.py
```

This will generate:
- `model.pkl` - Trained Random Forest model
- `vectorizer.pkl` - TF-IDF vectorizer
- `model_lr.pkl` - Logistic Regression model (backup)

## 📱 Features

### Mobile App
- **Home Dashboard**: Risk level, recent threats, quick scan options
- **Manual Scanning**: Test SMS, calls, emails, and URLs
- **Automatic SMS Scanning**: Real-time SMS fraud detection
- **History**: View all past scans
- **Settings**: Configure app preferences

### Backend API
- `/scan/sms` - Scan SMS for fraud
- `/scan/call` - Check phone number
- `/scan/email` - Detect phishing emails
- `/scan/url` - Analyze URLs for malicious content

### ML Models
- **Random Forest Classifier** (Primary)
- **Logistic Regression** (Backup)
- **TF-IDF Vectorization** for text analysis
- **Rule-based fallback** when ML model unavailable

## 🔧 Configuration

### Backend API URL

Update in `mobile-app/app/src/main/java/com/neura/frauddetection/network/ApiService.kt`:

```kotlin
private const val BASE_URL = "http://YOUR_IP:8000/"
```

### Firebase Setup

1. Create Firebase project at https://console.firebase.google.com
2. Enable Firestore Database
3. Download `google-services.json`
4. Place in `mobile-app/app/` directory

## 📊 API Documentation

See [API_Documentation.md](./API_Documentation.md) for detailed API endpoints.

## 🧪 Testing

### Test SMS
```json
POST /scan/sms
{
  "text": "URGENT: Your account will be suspended. Click here to verify",
  "phone_number": "+1234567890"
}
```

### Test URL
```json
POST /scan/url
{
  "url": "http://suspicious-site.com/verify"
}
```

## 🛡️ Security

- Input validation on all endpoints
- Secure API communication
- Android permissions properly requested
- Firebase security rules (configure in Firebase Console)

## 📈 Future Enhancements

- Real-time threat intelligence integration
- Advanced NLP models (BERT, GPT-based)
- Community reporting system
- Multi-language support
- Enhanced phone number database
- URL reputation checking
- Email header analysis
- Behavioral analysis

## 🐛 Troubleshooting

### Backend not connecting
- Check if backend is running on port 8000
- Verify firewall settings
- For physical device, ensure phone and computer are on same network

### ML model not loading
- Ensure `model.pkl` and `vectorizer.pkl` exist in `ml-model/` directory
- Run `python train.py` to generate models
- Check file paths in `fraud_detector.py`

### Firebase errors
- Verify `google-services.json` is in correct location
- Check Firebase project configuration
- Ensure Firestore is enabled

## 📄 License

This project is created for hackathon demonstration purposes.

## 👥 Contributors

NEURA Team - Hackathon 2024

---

**NEURA - Think Smart. Stay Safe.**


