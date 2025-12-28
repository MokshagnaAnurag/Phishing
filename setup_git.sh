#!/bin/bash
# Bash script to set up Git repository for NEURA
# Run this script: chmod +x setup_git.sh && ./setup_git.sh

echo "========================================"
echo "NEURA Git Repository Setup"
echo "========================================"
echo ""

# Check if Git is installed
if ! command -v git &> /dev/null; then
    echo "[ERROR] Git is not installed!"
    echo "Please install Git from: https://git-scm.com/downloads"
    exit 1
fi

echo "[OK] Git is installed: $(git --version)"
echo ""

# Check if already a git repository
if [ -d .git ]; then
    echo "[INFO] Git repository already initialized"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 0
    fi
else
    # Initialize git repository
    echo "[1/5] Initializing Git repository..."
    git init
    echo "[OK] Git repository initialized"
fi

echo ""

# Check git config
echo "[2/5] Checking Git configuration..."
USER_NAME=$(git config user.name)
USER_EMAIL=$(git config user.email)

if [ -z "$USER_NAME" ] || [ -z "$USER_EMAIL" ]; then
    echo "[WARNING] Git user not configured"
    read -p "Enter your name: " USER_NAME
    read -p "Enter your email: " USER_EMAIL
    git config --global user.name "$USER_NAME"
    git config --global user.email "$USER_EMAIL"
    echo "[OK] Git user configured"
else
    echo "[OK] Git user: $USER_NAME <$USER_EMAIL>"
fi

echo ""

# Add all files
echo "[3/5] Adding files to Git..."
git add .

if [ -n "$(git status --short)" ]; then
    echo "[OK] Files added to staging area"
    echo "Files to be committed:"
    git status --short
else
    echo "[INFO] No new files to add (everything already committed)"
fi

echo ""

# Create initial commit
echo "[4/5] Creating initial commit..."
COMMIT_MSG="Initial commit: NEURA Fraud Detection System

- Complete Android mobile app (Kotlin)
- FastAPI backend with ML integration
- Machine Learning models (Random Forest + Logistic Regression)
- Web frontend for testing
- Comprehensive documentation
- Test examples and scripts"

if git commit -m "$COMMIT_MSG" 2>/dev/null; then
    echo "[OK] Initial commit created"
else
    echo "[WARNING] Commit failed or nothing to commit"
fi

echo ""

# Instructions for GitHub
echo "[5/5] Next steps:"
echo ""
echo "To upload to GitHub:"
echo "1. Create a new repository on GitHub (https://github.com/new)"
echo "2. Run these commands:"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/neura-fraud-detection.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "Or see GIT_SETUP.md for detailed instructions"
echo ""
echo "========================================"
echo "Setup complete!"
echo "========================================"


