"""
Enhanced training script using real Kaggle datasets
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
from preprocess import clean_text

def load_kaggle_datasets():
    """Load and combine Kaggle datasets"""
    print("Loading Kaggle datasets...")
    
    # Load phishing email dataset
    phishing_path = os.path.join('..', 'datasets', 'fraud-data', 'Phishing_Email.csv')
    phishing_df = pd.read_csv(phishing_path)
    
    # Load web phishing dataset  
    web_path = os.path.join('..', 'datasets', 'phishing-data', 'dataset_phishing.csv')
    web_df = pd.read_csv(web_path)
    
    # Process phishing email data
    if 'Email Text' in phishing_df.columns and 'Email Type' in phishing_df.columns:
        phishing_texts = phishing_df['Email Text'].astype(str)
        phishing_labels = (phishing_df['Email Type'] == 'Phishing Email').astype(int)
    else:
        # Fallback column names
        text_col = phishing_df.columns[0]
        label_col = phishing_df.columns[1] 
        phishing_texts = phishing_df[text_col].astype(str)
        phishing_labels = phishing_df[label_col].astype(int)
    
    # Process web phishing data
    if 'url' in web_df.columns and 'status' in web_df.columns:
        web_texts = web_df['url'].astype(str)
        web_labels = (web_df['status'] == 'phishing').astype(int)
    else:
        # Use first two columns
        web_texts = web_df.iloc[:, 0].astype(str)
        web_labels = web_df.iloc[:, 1].astype(int)
    
    # Combine datasets
    all_texts = pd.concat([phishing_texts, web_texts], ignore_index=True)
    all_labels = pd.concat([pd.Series(phishing_labels), pd.Series(web_labels)], ignore_index=True)
    
    # Create combined dataframe
    combined_df = pd.DataFrame({
        'text': all_texts,
        'label': all_labels
    })
    
    # Remove duplicates and clean
    combined_df = combined_df.drop_duplicates().reset_index(drop=True)
    combined_df = combined_df.dropna().reset_index(drop=True)
    
    print(f"Combined dataset: {len(combined_df)} samples")
    print(f"Fraud samples: {combined_df['label'].sum()}")
    print(f"Safe samples: {len(combined_df) - combined_df['label'].sum()}")
    
    return combined_df

def add_synthetic_data(df):
    """Add synthetic SMS and common fraud patterns"""
    synthetic_fraud = [
        "URGENT: Your account will be suspended. Click here to verify immediately",
        "Congratulations! You won $50000. Claim now before it expires",
        "Your payment failed. Update card details: http://secure-pay.com",
        "ALERT: Suspicious activity detected. Verify identity now",
        "Your SIM will be deactivated. Call +91-9876543210 to reactivate",
        "Limited time offer! 90% discount. Act now or miss out forever",
        "Your package delivery failed. Pay $99 to reschedule delivery",
        "Netflix subscription expired. Renew: http://netflix-renew.com",
        "Bank account needs verification. Send details to verify@bank.com",
        "Credit card payment due. Pay $5000 immediately or face penalty"
    ]
    
    synthetic_safe = [
        "Your order #12345 shipped. Track: https://amazon.com/tracking",
        "Appointment scheduled tomorrow 2 PM. See you then!",
        "Payment of $500 successful. Transaction ID: TXN123456789",
        "Monthly statement ready. View: https://yourbank.com/statements", 
        "Password changed successfully. Contact support if not you",
        "Welcome to our service! Excited to have you on board",
        "Subscription renews 2024-12-31. No action needed",
        "Delivery out for delivery. Expected by 6 PM today",
        "Account balance: $10000. Last updated: 2024-01-15",
        "Bill payment of $2000 successful. Thank you for using our service"
    ]
    
    # Add synthetic data
    synthetic_df = pd.DataFrame({
        'text': synthetic_fraud + synthetic_safe,
        'label': [1] * len(synthetic_fraud) + [0] * len(synthetic_safe)
    })
    
    return pd.concat([df, synthetic_df], ignore_index=True)

def train_enhanced_model():
    """Train model with Kaggle datasets"""
    try:
        # Load Kaggle datasets
        df = load_kaggle_datasets()
        
        # Add synthetic SMS data
        df = add_synthetic_data(df)
        
        # Balance dataset if needed
        fraud_count = df['label'].sum()
        safe_count = len(df) - fraud_count
        
        if abs(fraud_count - safe_count) > min(fraud_count, safe_count) * 0.5:
            print("Balancing dataset...")
            fraud_df = df[df['label'] == 1]
            safe_df = df[df['label'] == 0]
            
            min_count = min(len(fraud_df), len(safe_df))
            max_samples = min_count * 2  # Allow 2:1 ratio max
            
            if len(fraud_df) > max_samples:
                fraud_df = fraud_df.sample(max_samples, random_state=42)
            if len(safe_df) > max_samples:
                safe_df = safe_df.sample(max_samples, random_state=42)
                
            df = pd.concat([fraud_df, safe_df], ignore_index=True)
        
        print(f"Final dataset: {len(df)} samples")
        print(f"Fraud: {df['label'].sum()}, Safe: {len(df) - df['label'].sum()}")
        
        # Clean text
        df['cleaned_text'] = df['text'].apply(clean_text)
        
        # Split data
        X = df['cleaned_text']
        y = df['label']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Vectorize
        vectorizer = TfidfVectorizer(
            max_features=10000,
            ngram_range=(1, 3),
            min_df=2,
            max_df=0.95,
            stop_words='english'
        )
        
        X_train_vec = vectorizer.fit_transform(X_train)
        X_test_vec = vectorizer.transform(X_test)
        
        # Train Random Forest
        model = RandomForestClassifier(
            n_estimators=200,
            max_depth=30,
            random_state=42,
            n_jobs=-1,
            class_weight='balanced'
        )
        
        print("Training enhanced model...")
        model.fit(X_train_vec, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test_vec)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"Enhanced Model Accuracy: {accuracy:.4f}")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, target_names=['Safe', 'Fraud']))
        
        # Save model
        joblib.dump(model, 'model_enhanced.pkl')
        joblib.dump(vectorizer, 'vectorizer_enhanced.pkl')
        
        print("Enhanced model saved!")
        return model, vectorizer
        
    except Exception as e:
        print(f"Error loading Kaggle datasets: {e}")
        print("Falling back to original training...")
        
        # Fallback to original method
        from train import generate_sample_dataset, train_model
        df = generate_sample_dataset()
        return train_model(df)

if __name__ == '__main__':
    print("=" * 60)
    print("NEURA - Enhanced Training with Kaggle Datasets")
    print("=" * 60)
    
    model, vectorizer = train_enhanced_model()
    
    print("\n" + "=" * 60)
    print("Enhanced training completed!")
    print("=" * 60)