# ML Model Training

This directory contains the Machine Learning models and training scripts for NEURA.

## Files

- `train.py` - Main training script
- `preprocess.py` - Text preprocessing utilities
- `dataset.csv` - Sample training dataset
- `requirements.txt` - Python dependencies

## Training the Model

```bash
# Install dependencies
pip install -r requirements.txt

# Train the model
python train.py
```

This will generate:
- `model.pkl` - Trained Random Forest model
- `vectorizer.pkl` - TF-IDF vectorizer
- `model_lr.pkl` - Logistic Regression model (backup)
- `vectorizer_lr.pkl` - Logistic Regression vectorizer

## Model Details

### Random Forest Classifier (Primary)
- **Algorithm**: Random Forest
- **Estimators**: 100 trees
- **Max Depth**: 20
- **Features**: TF-IDF with 5000 max features
- **N-grams**: 1-2 grams

### Logistic Regression (Backup)
- **Algorithm**: Logistic Regression
- **Max Iterations**: 1000
- **Regularization**: C=1.0
- **Features**: Same TF-IDF vectorization

## Dataset

The included `dataset.csv` contains:
- 15 fraud samples
- 15 safe samples
- Total: 30 samples

For production, expand this dataset with more real-world examples.

## Preprocessing

Text preprocessing includes:
- Lowercasing
- URL removal
- Email removal
- Phone number removal
- Special character removal
- Whitespace normalization

## Feature Extraction

Handcrafted features:
- Text length
- Word count
- Urgency words detection
- Currency mentions
- Number presence
- Link presence
- Phone number presence
- Email presence
- Uppercase ratio
- Digit ratio

## Usage in Backend

The trained models are automatically loaded by `backend/ml/fraud_detector.py` when the backend starts.

If models are not found, the system falls back to rule-based detection.


