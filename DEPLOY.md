# Deploy NEURA to Vercel

## 🚀 Quick Deploy Steps:

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Login to Vercel
```bash
vercel login
```

### 3. Deploy from Project Root
```bash
cd hackathon
vercel --prod
```

### 4. Update Mobile App API URL
After deployment, update `ApiService.kt`:
```kotlin
private const val BASE_URL = "https://your-app.vercel.app/"
```

## 📝 Files Added for Deployment:
- `vercel.json` - Vercel configuration
- `requirements.txt` - Python dependencies
- Updated `backend/main.py` - Vercel handler

## 🔧 Environment Variables (if needed):
```bash
vercel env add PYTHONPATH .
```

## ✅ Deployment Complete!
Your NEURA API will be available at: `https://your-app.vercel.app`