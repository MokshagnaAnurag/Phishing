# 🚀 NEURA Render Deployment - Final Fix

## Manual Render Settings:

### 1. Create New Web Service
- Connect GitHub repo: `MokshagnaAnurag/Phishing`
- Branch: `main`

### 2. Configure Settings:
- **Name**: `neura-api`
- **Environment**: `Python 3`
- **Build Command**: (leave empty)
- **Start Command**: `python main.py`

### 3. Environment Variables:
- `PYTHONPATH` = `.`

### 4. Push Final Files:
```bash
git add main.py
git commit -m "Final Render deployment fix"
git push
```

## ✅ Files Ready:
- `main.py` - Uses PORT env variable
- `requirements.txt` - Lightweight dependencies
- `backend/lightweight_detector.py` - No ML models
- `backend/main.py` - Updated imports

**Deploy with these manual settings - should work!** 🎯