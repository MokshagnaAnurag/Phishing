# Git Setup & Upload Guide for NEURA

## Step 1: Install Git (if not installed)

### Windows:
1. Download Git: https://git-scm.com/download/win
2. Install with default settings
3. Restart terminal/PowerShell

### Verify Installation:
```bash
git --version
```

---

## Step 2: Initialize Git Repository

```bash
# Navigate to project directory
cd C:\hackathon

# Initialize git repository
git init

# Configure git (if first time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Step 3: Add Files to Git

```bash
# Add all files
git add .

# Check what will be committed
git status

# Create initial commit
git commit -m "Initial commit: NEURA Fraud Detection System

- Complete Android mobile app (Kotlin)
- FastAPI backend with ML integration
- Machine Learning models (Random Forest + Logistic Regression)
- Web frontend for testing
- Comprehensive documentation
- Test examples and scripts"
```

---

## Step 4: Create GitHub Repository

### Option A: Using GitHub Website

1. Go to https://github.com
2. Click "New repository"
3. Repository name: `neura-fraud-detection` (or your choice)
4. Description: "AI-Powered Fraud & Phishing Detection System"
5. Choose Public or Private
6. **DO NOT** initialize with README (we already have one)
7. Click "Create repository"

### Option B: Using GitHub CLI (if installed)

```bash
gh repo create neura-fraud-detection --public --description "AI-Powered Fraud & Phishing Detection System"
```

---

## Step 5: Connect Local Repository to GitHub

```bash
# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/neura-fraud-detection.git

# Or if using SSH:
# git remote add origin git@github.com:YOUR_USERNAME/neura-fraud-detection.git

# Verify remote
git remote -v
```

---

## Step 6: Push to GitHub

```bash
# Push to main branch
git branch -M main
git push -u origin main
```

If prompted for credentials:
- Username: Your GitHub username
- Password: Use a Personal Access Token (not your password)
  - Generate token: https://github.com/settings/tokens
  - Select scope: `repo`

---

## Step 7: Verify Upload

1. Go to your GitHub repository
2. Check that all files are uploaded
3. Verify README.md displays correctly

---

## Quick Commands Reference

```bash
# Check status
git status

# Add files
git add .
git add specific-file.txt

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push

# Pull latest changes
git pull

# View commit history
git log

# Create new branch
git checkout -b feature-name

# Switch branches
git checkout main
```

---

## Repository Structure (What Gets Uploaded)

```
NEURA/
├── .gitignore              ✅ (excludes sensitive files)
├── README.md               ✅
├── QUICK_START.md          ✅
├── TEST_EXAMPLES.md        ✅
├── HOW_IT_WORKS.md         ✅
├── ENHANCEMENT_GUIDE.md    ✅
├── PROJECT_SUMMARY.md      ✅
├── mobile-app/             ✅ (Android app)
├── backend/                 ✅ (FastAPI server)
├── ml-model/                ✅ (ML training)
├── frontend/                ✅ (Web UI)
├── docs/                    ✅ (Documentation)
└── test_*.py                ✅ (Test scripts)
```

**Excluded (via .gitignore):**
- `*.pkl` (ML model files - too large)
- `__pycache__/`
- `venv/`
- `google-services.json` (Firebase config - sensitive)
- `node_modules/`

---

## Troubleshooting

### Error: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/repo-name.git
```

### Error: "failed to push some refs"
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Error: Authentication failed
- Use Personal Access Token instead of password
- Or set up SSH keys

### Large files warning
If model files are too large:
```bash
# Add to .gitignore (already done)
# Use Git LFS for large files:
git lfs install
git lfs track "*.pkl"
git add .gitattributes
```

---

## Alternative: Upload via GitHub Desktop

1. Download GitHub Desktop: https://desktop.github.com/
2. Install and sign in
3. File → Add Local Repository
4. Select `C:\hackathon`
5. Click "Publish repository"
6. Choose name and visibility
7. Click "Publish repository"

---

## Next Steps After Upload

1. ✅ Add repository description
2. ✅ Add topics/tags: `fraud-detection`, `machine-learning`, `android`, `python`, `fastapi`
3. ✅ Enable GitHub Pages (if needed)
4. ✅ Add license file (MIT, Apache, etc.)
5. ✅ Create releases for versions
6. ✅ Add collaborators (if team project)

---

## Repository Settings to Configure

1. **Settings → General:**
   - Add description
   - Add website URL (if deployed)
   - Enable issues, projects, wiki

2. **Settings → Secrets:**
   - Add API keys (for threat intelligence)
   - Add Firebase credentials

3. **Settings → Actions:**
   - Enable GitHub Actions (for CI/CD)

---

**Need help?** Check Git documentation: https://git-scm.com/doc


