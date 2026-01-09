# NEURA Architecture Documentation

## System Overview

NEURA is a three-tier architecture consisting of:

1. **Mobile Application** (Android/Kotlin)
2. **Backend API Server** (Python/FastAPI)
3. **Machine Learning Engine** (Python/Scikit-learn)

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    Mobile App (Android)                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │  Home    │  │   Scan   │  │  History │             │
│  │ Dashboard│  │ Activity │  │ Activity │             │
│  └──────────┘  └──────────┘  └──────────┘             │
│       │              │              │                   │
│       └──────────────┼──────────────┘                   │
│                      │                                  │
│              ┌───────▼────────┐                        │
│              │   API Service  │                        │
│              │   (Retrofit)   │                        │
│              └───────┬────────┘                        │
└──────────────────────┼──────────────────────────────────┘
                       │ HTTP/REST
                       │
┌──────────────────────▼──────────────────────────────────┐
│              Backend API (FastAPI)                      │
│  ┌──────────────────────────────────────────────┐     │
│  │         API Endpoints                         │     │
│  │  /scan/sms  /scan/call  /scan/email  /scan/url│     │
│  └──────────────────┬─────────────────────────────┘     │
│                     │                                    │
│              ┌──────▼────────┐                          │
│              │ FraudDetector │                          │
│              │   (ML Engine) │                          │
│              └──────┬────────┘                          │
└─────────────────────┼───────────────────────────────────┘
                      │
┌──────────────────────▼──────────────────────────────────┐
│         Machine Learning Module                         │
│  ┌──────────────┐  ┌──────────────┐                    │
│  │   Preprocess │  │  ML Models    │                    │
│  │   (NLP)      │  │  (RF/LR)      │                    │
│  └──────────────┘  └──────────────┘                    │
└─────────────────────────────────────────────────────────┘
                      │
┌──────────────────────▼──────────────────────────────────┐
│              Firebase Firestore                         │
│         (Scan History & Results)                         │
└─────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Mobile Application Layer

**Technology Stack:**
- Kotlin
- Android SDK
- Retrofit (HTTP client)
- Firebase SDK
- Material Design Components

**Key Components:**

- **Activities:**
  - `MainActivity`: Home dashboard
  - `ScanActivity`: Manual scanning interface
  - `HistoryActivity`: Scan history display
  - `SettingsActivity`: App configuration
  - `AlertDetailActivity`: Detailed threat information

- **Network Layer:**
  - `ApiService`: REST API client
  - Handles all backend communication
  - Error handling and retry logic

- **Data Layer:**
  - `FirebaseHelper`: Firestore operations
  - Local caching (optional)

- **Utilities:**
  - `SMSReceiver`: Automatic SMS scanning
  - `PermissionHelper`: Permission management

### 2. Backend API Layer

**Technology Stack:**
- Python 3.8+
- FastAPI framework
- Uvicorn ASGI server
- Pydantic for validation

**Key Components:**

- **API Endpoints:**
  - `/scan/sms`: SMS fraud detection
  - `/scan/call`: Phone number verification
  - `/scan/email`: Email phishing detection
  - `/scan/url`: URL malicious content analysis

- **ML Integration:**
  - `FraudDetector` class
  - Model loading and inference
  - Rule-based fallback

- **Features:**
  - CORS enabled
  - Input validation
  - Error handling
  - Health checks

### 3. Machine Learning Layer

**Technology Stack:**
- Python
- Scikit-learn
- Pandas, NumPy
- Joblib (model serialization)

**Key Components:**

- **Preprocessing:**
  - Text cleaning and normalization
  - URL preprocessing
  - Feature extraction

- **Models:**
  - Random Forest Classifier (primary)
  - Logistic Regression (backup)
  - TF-IDF Vectorization

- **Training:**
  - `train.py`: Model training script
  - `preprocess.py`: Text preprocessing utilities
  - `dataset.csv`: Training data

### 4. Database Layer

**Technology:**
- Firebase Firestore (NoSQL)

**Collections:**
- `scan_history`: Stores all scan results
  - Fields: scanType, isFraud, confidence, riskLevel, message, timestamp

## Data Flow

### SMS Scanning Flow

1. User receives SMS → `SMSReceiver` intercepts
2. SMS text sent to backend `/scan/sms`
3. Backend preprocesses text
4. ML model predicts fraud probability
5. Result returned to mobile app
6. If fraud detected, show alert
7. Save result to Firestore

### Manual Scan Flow

1. User enters data in `ScanActivity`
2. Data sent to appropriate endpoint
3. Backend processes and returns result
4. Result displayed in UI
5. Result saved to Firestore history

## Security Considerations

1. **Input Validation:**
   - All inputs validated on backend
   - SQL injection prevention (using Firestore)
   - XSS prevention

2. **API Security:**
   - HTTPS in production
   - API key authentication (future)
   - Rate limiting (future)

3. **Mobile Security:**
   - Permissions properly requested
   - Secure storage for sensitive data
   - Certificate pinning (future)

## Scalability

### Current Limitations
- Single backend instance
- No load balancing
- No caching layer
- ML model loaded in memory

### Future Improvements
- Multiple backend instances
- Redis caching
- Model serving (TensorFlow Serving)
- Database sharding
- CDN for static assets

## Performance Optimization

1. **ML Model:**
   - Model caching in memory
   - Batch processing capability
   - Model quantization

2. **API:**
   - Async request handling
   - Connection pooling
   - Response caching

3. **Mobile:**
   - Image caching
   - Lazy loading
   - Background processing

## Deployment

### Backend Deployment
- Deploy to cloud (AWS, GCP, Azure)
- Use Docker containers
- Environment variables for configuration
- Load balancer for multiple instances

### Mobile App Deployment
- Build APK/AAB
- Sign with release key
- Publish to Google Play Store
- Firebase configuration for production

## Monitoring & Logging

### Current State
- Basic error logging
- Console output

### Future Enhancements
- Structured logging (JSON)
- Error tracking (Sentry)
- Analytics (Firebase Analytics)
- Performance monitoring

## Testing Strategy

1. **Unit Tests:**
   - ML model accuracy
   - API endpoint logic
   - Utility functions

2. **Integration Tests:**
   - API-ML integration
   - Mobile-Backend integration

3. **End-to-End Tests:**
   - Complete user flows
   - Real device testing

## Future Architecture Enhancements

1. **Microservices:**
   - Separate ML service
   - Notification service
   - Analytics service

2. **Real-time Features:**
   - WebSocket for live updates
   - Push notifications

3. **Advanced ML:**
   - Deep learning models
   - Transfer learning
   - Online learning

---

**Last Updated:** 2024


