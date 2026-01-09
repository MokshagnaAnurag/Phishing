# 🚀 NEURA - Ready for GitHub Push

## Files to Upload to GitHub:

### Root Files:
- `main.py` - Entry point for Render
- `requirements.txt` - Lightweight dependencies
- `README.md` - Documentation

### Backend Folder:
- `backend/main.py` - FastAPI app
- `backend/lightweight_detector.py` - Fraud detection logic

### Mobile App Folder:
- `mobile-app/` - Complete Android project

## Render Deployment Settings:

1. **Repository**: https://github.com/MokshagnaAnurag/Phishing.git
2. **Build Command**: (leave empty)
3. **Start Command**: `python main.py`
4. **Environment**: `PYTHONPATH=.`

## Key Files Content:

### main.py (Root):
```python
"""NEURA API - Root entry point for Render deployment"""
import os
from backend.main import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
```

### requirements.txt:
```
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
pydantic>=2.5.0
python-multipart>=0.0.6
```

## Upload Instructions:
1. Upload all files to GitHub repo
2. Deploy on Render with manual settings above
3. Update mobile app API URL after deployment

✅ **Ready for deployment!**