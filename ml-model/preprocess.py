"""
Preprocessing utilities for fraud and phishing detection
"""
import re
import string
from typing import List


def clean_text(text: str) -> str:
    """
    Clean and normalize text input
    
    Args:
        text: Raw text input
        
    Returns:
        Cleaned text string
    """
    if not text:
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub(r'www\.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove phone numbers
    text = re.sub(r'[\+]?[(]?[0-9]{1,4}[)]?[-\s\.]?[(]?[0-9]{1,4}[)]?[-\s\.]?[0-9]{1,9}', '', text)
    
    # Remove special characters but keep spaces
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text.strip()


def extract_features(text: str) -> dict:
    """
    Extract handcrafted features from text
    
    Args:
        text: Input text
        
    Returns:
        Dictionary of features
    """
    features = {
        'length': len(text),
        'word_count': len(text.split()),
        'has_urgency_words': bool(re.search(r'\b(urgent|immediately|act now|limited time|expire|suspended|verify|confirm)\b', text.lower())),
        'has_currency': bool(re.search(r'[\$₹€£]|rupee|dollar|euro', text.lower())),
        'has_number': bool(re.search(r'\d', text)),
        'has_link': bool(re.search(r'http|www|\.com|\.in|\.org', text.lower())),
        'has_phone': bool(re.search(r'[\+]?[(]?[0-9]{1,4}[)]?[-\s\.]?[(]?[0-9]{1,4}[)]?[-\s\.]?[0-9]{1,9}', text)),
        'has_email': bool(re.search(r'\S+@\S+', text)),
        'uppercase_ratio': sum(1 for c in text if c.isupper()) / len(text) if text else 0,
        'digit_ratio': sum(1 for c in text if c.isdigit()) / len(text) if text else 0,
    }
    return features


def preprocess_url(url: str) -> str:
    """
    Preprocess URL for analysis
    
    Args:
        url: Raw URL string
        
    Returns:
        Cleaned URL string
    """
    if not url:
        return ""
    
    # Remove protocol
    url = re.sub(r'^https?://', '', url)
    
    # Remove www
    url = re.sub(r'^www\.', '', url)
    
    # Extract domain
    domain = url.split('/')[0]
    
    return domain.lower().strip()


