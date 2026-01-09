# Deploy NEURA to Render

## 🚀 Quick Steps:

### 1. Update GitHub Repo
Push these files to your repo:
- `requirements.txt` (lightweight version)
- `backend/lightweight_detector.py`
- `backend/main.py` (updated)
- `render.yaml`

### 2. Deploy on Render
1. Go to render.com
2. Connect your GitHub repo
3. Select "Web Service"
4. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - **Environment**: `PYTHONPATH=.`

### 3. Update Mobile App
After deployment, update `ApiService.kt`:
```kotlin
private const val BASE_URL = "https://your-app.onrender.com/"
```

## ✅ Files Ready for Deployment:
- Lightweight detector (no ML models)
- Minimal dependencies
- Render configuration