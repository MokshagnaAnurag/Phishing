"""
Training script for fraud and phishing detection model
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os
from preprocess import clean_text, extract_features

# Set random seed for reproducibility
np.random.seed(42)


def load_dataset(filepath: str = 'dataset.csv') -> pd.DataFrame:
    """
    Load dataset from CSV file
    
    Args:
        filepath: Path to dataset CSV
        
    Returns:
        DataFrame with text and label columns
    """
    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    else:
        # Generate sample dataset if file doesn't exist
        return generate_sample_dataset()


def generate_sample_dataset() -> pd.DataFrame:
    """
    Generate a sample dataset for training
    
    Returns:
        DataFrame with sample fraud and safe messages
    """
    fraud_samples = [
        "URGENT: Your account will be suspended in 24 hours. Click here to verify: http://bank-verify.com",
        "Congratulations! You won ₹50,000. Claim now: www.prize-claim.in",
        "Your OTP is 123456. Do not share with anyone. Bank will never ask for OTP.",
        "Payment failed. Update your card details immediately: http://secure-payment.com",
        "Your SIM card will be deactivated. Call +91-9876543210 to reactivate.",
        "Limited time offer! Get 90% discount. Act now before it expires.",
        "Your account has been compromised. Verify your identity: www.secure-bank.com",
        "You have received ₹10,000. Click to claim: http://money-transfer.in",
        "Your package delivery failed. Pay ₹99 to reschedule: www.delivery-pay.com",
        "Your Netflix subscription expired. Renew now: http://netflix-renew.com",
        "Your bank account needs verification. Send your details to verify@bank.com",
        "WARNING: Unusual activity detected. Verify account: http://bank-security.com",
        "Your credit card payment is due. Pay ₹5,000 immediately: www.payment-gateway.com",
        "You have 3 unread messages. Click here: http://sms-reader.com",
        "Your insurance claim is approved. Claim ₹25,000: www.insurance-claim.in",
    ]
    
    safe_samples = [
        "Your order #12345 has been shipped. Track at: https://tracking.example.com",
        "Your appointment is scheduled for tomorrow at 2 PM. See you then!",
        "Thank you for your payment of ₹500. Transaction ID: TXN123456789",
        "Your monthly statement is ready. View at: https://bank.example.com/statements",
        "Your password was changed successfully. If this wasn't you, contact support.",
        "Welcome to our service! We're excited to have you on board.",
        "Your subscription will renew on 2024-12-31. No action needed.",
        "Your delivery is out for delivery. Expected by 6 PM today.",
        "Your account balance is ₹10,000. Last updated: 2024-01-15",
        "Your login was successful from New Delhi. If this wasn't you, please contact us.",
        "Your bill payment of ₹2,000 was successful. Thank you!",
        "Your profile has been updated successfully.",
        "Your request has been received. We'll get back to you within 24 hours.",
        "Your verification code is 456789. Valid for 10 minutes.",
        "Your transaction of ₹1,500 was completed. Receipt: RCP123456",
    ]
    
    # Create DataFrame
    data = {
        'text': fraud_samples + safe_samples,
        'label': [1] * len(fraud_samples) + [0] * len(safe_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Save to CSV for future use
    df.to_csv('dataset.csv', index=False)
    print("Sample dataset generated and saved to dataset.csv")
    
    return df


def train_model(df: pd.DataFrame, model_type: str = 'random_forest'):
    """
    Train fraud detection model
    
    Args:
        df: DataFrame with text and label columns
        model_type: 'random_forest' or 'logistic_regression'
        
    Returns:
        Trained model and vectorizer
    """
    print(f"\nTraining {model_type} model...")
    print(f"Dataset size: {len(df)} samples")
    print(f"Fraud samples: {df['label'].sum()}")
    print(f"Safe samples: {len(df) - df['label'].sum()}")
    
    # Clean text
    df['cleaned_text'] = df['text'].apply(clean_text)
    
    # Split data
    X = df['cleaned_text']
    y = df['label']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # TF-IDF Vectorization
    print("\nVectorizing text...")
    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.95
    )
    
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    # Train model
    if model_type == 'random_forest':
        model = RandomForestClassifier(
            n_estimators=100,
            max_depth=20,
            random_state=42,
            n_jobs=-1
        )
    else:
        model = LogisticRegression(
            max_iter=1000,
            random_state=42,
            C=1.0
        )
    
    print("Training model...")
    model.fit(X_train_vec, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nModel Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Safe', 'Fraud']))
    
    # Save model and vectorizer
    model_path = 'model.pkl'
    vectorizer_path = 'vectorizer.pkl'
    
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)
    
    print(f"\nModel saved to {model_path}")
    print(f"Vectorizer saved to {vectorizer_path}")
    
    return model, vectorizer


def predict(text: str, model, vectorizer) -> tuple:
    """
    Predict if text is fraud or safe
    
    Args:
        text: Input text
        model: Trained model
        vectorizer: Fitted vectorizer
        
    Returns:
        Tuple of (prediction, confidence_score)
        prediction: 1 for fraud, 0 for safe
        confidence_score: Probability of fraud
    """
    cleaned = clean_text(text)
    text_vec = vectorizer.transform([cleaned])
    
    prediction = model.predict(text_vec)[0]
    probabilities = model.predict_proba(text_vec)[0]
    
    confidence = probabilities[1] if prediction == 1 else probabilities[0]
    
    return int(prediction), float(confidence)


if __name__ == '__main__':
    print("=" * 50)
    print("NEURA - Fraud Detection Model Training")
    print("=" * 50)
    
    # Load or generate dataset
    df = load_dataset()
    
    # Train Random Forest model (preferred for demo)
    model, vectorizer = train_model(df, model_type='random_forest')
    
    # Also train Logistic Regression as backup
    print("\n" + "=" * 50)
    model_lr, vectorizer_lr = train_model(df, model_type='logistic_regression')
    joblib.dump(model_lr, 'model_lr.pkl')
    joblib.dump(vectorizer_lr, 'vectorizer_lr.pkl')
    
    print("\n" + "=" * 50)
    print("Training completed successfully!")
    print("=" * 50)


