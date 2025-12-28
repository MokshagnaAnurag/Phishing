# NEURA Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Setup Backend (2 minutes)

**Windows:**
```bash
setup_backend.bat
```

**Linux/Mac:**
```bash
chmod +x setup_backend.sh
./setup_backend.sh
```

**Manual:**
```bash
# Install dependencies
cd backend
pip install -r requirements.txt

# Train ML model
cd ../ml-model
pip install -r requirements.txt
python train.py

# Start server
cd ../backend
python main.py
```

### Step 2: Test Backend (1 minute)

Open browser: http://localhost:8000

Or test with curl:
```bash
curl http://localhost:8000/health
```

### Step 3: Setup Mobile App (2 minutes)

1. **Open Android Studio**
   - File → Open → Select `mobile-app` folder

2. **Configure Firebase** (Optional for demo)
   - Create Firebase project at https://console.firebase.google.com
   - Download `google-services.json`
   - Place in `mobile-app/app/` directory
   - If skipping Firebase, the app will use mock data

3. **Update API URL** (if needed)
   - Open `mobile-app/app/src/main/java/com/neura/frauddetection/network/ApiService.kt`
   - For emulator: `http://10.0.2.2:8000/` (already set)
   - For physical device: Change to your computer's IP address

4. **Build & Run**
   - Sync Gradle files
   - Run on emulator or device

## ✅ You're Ready!

The app should now:
- ✅ Connect to backend API
- ✅ Scan SMS, calls, emails, URLs
- ✅ Show fraud detection results
- ✅ Save history (if Firebase configured)

## 🧪 Test Examples

### Test SMS Scan
```
Text: "URGENT: Your account will be suspended. Click here to verify"
Expected: FRAUD DETECTED (High confidence)
```

### Test Safe SMS
```
Text: "Your order has been shipped. Track at: https://example.com"
Expected: Safe (Low risk)
```

### Test URL
```
URL: "http://verify-bank-account.com"
Expected: MALICIOUS URL (Medium-High risk)
```

## 🐛 Troubleshooting

**Backend not starting?**
- Check Python version: `python --version` (need 3.8+)
- Check port 8000 is available
- Try: `python -m uvicorn main:app --reload`

**Mobile app not connecting?**
- Verify backend is running
- Check API URL in `ApiService.kt`
- For physical device, ensure same WiFi network
- Check AndroidManifest.xml has internet permission

**ML model errors?**
- Run `python train.py` in `ml-model/` directory
- Check `model.pkl` and `vectorizer.pkl` exist

## 📱 Demo Mode

If Firebase is not configured, the app will:
- Still work for scanning
- Show mock data in history
- Function fully for demo purposes

---

**Need help?** Check [docs/README.md](./docs/README.md) for detailed documentation.


