# PowerShell script to set up Git repository for NEURA
# Run this script: .\setup_git.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "NEURA Git Repository Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
try {
    $gitVersion = git --version
    Write-Host "[OK] Git is installed: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Git is not installed!" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host "Then run this script again." -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Check if already a git repository
if (Test-Path .git) {
    Write-Host "[INFO] Git repository already initialized" -ForegroundColor Yellow
    $continue = Read-Host "Continue anyway? (y/n)"
    if ($continue -ne "y") {
        exit 0
    }
} else {
    # Initialize git repository
    Write-Host "[1/5] Initializing Git repository..." -ForegroundColor Cyan
    git init
    Write-Host "[OK] Git repository initialized" -ForegroundColor Green
}

Write-Host ""

# Check git config
Write-Host "[2/5] Checking Git configuration..." -ForegroundColor Cyan
$userName = git config user.name
$userEmail = git config user.email

if (-not $userName -or -not $userEmail) {
    Write-Host "[WARNING] Git user not configured" -ForegroundColor Yellow
    $userName = Read-Host "Enter your name"
    $userEmail = Read-Host "Enter your email"
    git config --global user.name $userName
    git config --global user.email $userEmail
    Write-Host "[OK] Git user configured" -ForegroundColor Green
} else {
    Write-Host "[OK] Git user: $userName <$userEmail>" -ForegroundColor Green
}

Write-Host ""

# Add all files
Write-Host "[3/5] Adding files to Git..." -ForegroundColor Cyan
git add .
$status = git status --short
if ($status) {
    Write-Host "[OK] Files added to staging area" -ForegroundColor Green
    Write-Host "Files to be committed:" -ForegroundColor Yellow
    git status --short
} else {
    Write-Host "[INFO] No new files to add (everything already committed)" -ForegroundColor Yellow
}

Write-Host ""

# Create initial commit
Write-Host "[4/5] Creating initial commit..." -ForegroundColor Cyan
$commitMessage = @"
Initial commit: NEURA Fraud Detection System

- Complete Android mobile app (Kotlin)
- FastAPI backend with ML integration
- Machine Learning models (Random Forest + Logistic Regression)
- Web frontend for testing
- Comprehensive documentation
- Test examples and scripts
"@

try {
    git commit -m $commitMessage
    Write-Host "[OK] Initial commit created" -ForegroundColor Green
} catch {
    Write-Host "[WARNING] Commit failed or nothing to commit" -ForegroundColor Yellow
}

Write-Host ""

# Instructions for GitHub
Write-Host "[5/5] Next steps:" -ForegroundColor Cyan
Write-Host ""
Write-Host "To upload to GitHub:" -ForegroundColor Yellow
Write-Host "1. Create a new repository on GitHub (https://github.com/new)" -ForegroundColor White
Write-Host "2. Run these commands:" -ForegroundColor White
Write-Host ""
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/neura-fraud-detection.git" -ForegroundColor Cyan
Write-Host "   git branch -M main" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor Cyan
Write-Host ""
Write-Host "Or see GIT_SETUP.md for detailed instructions" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Setup complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan


