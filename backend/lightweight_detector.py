"""
Lightweight fraud detector for Vercel deployment
No large ML models - uses optimized rule-based detection
"""
import re
from typing import Dict, Optional

class LightweightFraudDetector:
    """Lightweight fraud detection without large ML models"""
    
    def __init__(self):
        self.model_loaded = True  # Always true for lightweight version
    
    def is_loaded(self) -> bool:
        return True
    
    def _advanced_rule_detection(self, text: str) -> tuple:
        """Advanced rule-based detection optimized for accuracy"""
        text_lower = text.lower()
        
        # High-risk fraud indicators (score: 3)
        high_risk = [
            'urgent.*suspend', 'click.*verify', 'account.*compromised',
            'won.*prize', 'claim.*now', 'act.*immediately', 'expire.*soon',
            'payment.*failed', 'update.*card', 'verify.*identity'
        ]
        
        # Medium-risk indicators (score: 2)
        medium_risk = [
            'congratulations', 'winner', 'limited.*time', 'offer.*expires',
            'verify.*account', 'confirm.*details', 'suspicious.*activity'
        ]
        
        # Low-risk indicators (score: 1)
        low_risk = [
            'free', 'discount', 'sale', 'promotion', 'deal'
        ]
        
        # Safe indicators (negative score)
        safe_indicators = [
            'thank.*you', 'receipt', 'confirmation', 'order.*shipped',
            'appointment', 'delivery', 'statement.*ready', 'welcome',
            'subscription.*renew', 'balance.*update'
        ]
        
        score = 0
        
        # Check patterns
        for pattern in high_risk:
            if re.search(pattern, text_lower):
                score += 3
        
        for pattern in medium_risk:
            if re.search(pattern, text_lower):
                score += 2
                
        for pattern in low_risk:
            if re.search(pattern, text_lower):
                score += 1
        
        for pattern in safe_indicators:
            if re.search(pattern, text_lower):
                score -= 2
        
        # URL analysis
        if re.search(r'http://[^\\s]+', text_lower):  # Non-HTTPS
            score += 2
        elif re.search(r'https://[^\\s]+\\.(gov|edu|amazon|google)', text_lower):  # Trusted
            score -= 1
        
        # Suspicious domains
        if re.search(r'(verify|secure|bank).*\\.(com|net)', text_lower):
            score += 2
        
        # Phone numbers in suspicious context
        if re.search(r'call.*\\+?[0-9]{10,}', text_lower):
            score += 1
        
        # Normalize score (0-1)
        confidence = max(0, min(score / 8.0, 1.0))
        is_fraud = confidence > 0.4
        
        return is_fraud, confidence
    
    def detect_sms(self, text: str, phone_number: Optional[str] = None) -> Dict:
        """SMS fraud detection"""
        is_fraud, confidence = self._advanced_rule_detection(text)
        
        risk_level = "HIGH" if confidence >= 0.7 else "MEDIUM" if confidence >= 0.4 else "LOW"
        
        message = "⚠️ FRAUD DETECTED" if is_fraud else "✅ Safe"
        if is_fraud:
            message += f" - High risk of phishing/scam (Confidence: {confidence:.1%})"
        else:
            message += f" - No threats detected (Confidence: {confidence:.1%})"
        
        return {
            "is_fraud": is_fraud,
            "confidence": round(confidence, 4),
            "risk_level": risk_level,
            "message": message,
            "details": {
                "type": "SMS",
                "phone_number": phone_number,
                "text_length": len(text)
            }
        }
    
    def detect_call(self, phone_number: str) -> Dict:
        """Phone number verification"""
        # Simple phone analysis
        digits = re.sub(r'\\D', '', phone_number)
        
        is_fraud = False
        confidence = 0.2
        
        # Very short numbers
        if len(digits) < 10:
            is_fraud = True
            confidence = 0.8
        # Repeated digits
        elif len(set(digits[-6:])) < 3:
            is_fraud = True
            confidence = 0.6
        
        risk_level = "HIGH" if confidence >= 0.7 else "MEDIUM" if confidence >= 0.4 else "LOW"
        
        message = "⚠️ SCAM NUMBER" if is_fraud else "✅ Safe Number"
        
        return {
            "is_fraud": is_fraud,
            "confidence": round(confidence, 4),
            "risk_level": risk_level,
            "message": message,
            "details": {"type": "CALL", "phone_number": phone_number}
        }
    
    def detect_email(self, subject: str, body: str, sender: Optional[str] = None) -> Dict:
        """Email phishing detection"""
        full_text = f"{subject} {body}"
        is_fraud, confidence = self._advanced_rule_detection(full_text)
        
        # Check sender domain
        if sender and '@' in sender:
            domain = sender.split('@')[1].lower()
            if any(word in domain for word in ['verify', 'secure', 'bank']) and len(domain) > 20:
                confidence = max(confidence, 0.7)
                is_fraud = True
        
        risk_level = "HIGH" if confidence >= 0.7 else "MEDIUM" if confidence >= 0.4 else "LOW"
        
        message = "⚠️ PHISHING EMAIL" if is_fraud else "✅ Safe Email"
        
        return {
            "is_fraud": is_fraud,
            "confidence": round(confidence, 4),
            "risk_level": risk_level,
            "message": message,
            "details": {"type": "EMAIL", "sender": sender}
        }
    
    def detect_url(self, url: str) -> Dict:
        """URL malware detection"""
        url_lower = url.lower()
        
        score = 0
        
        # IP addresses (suspicious)
        if re.search(r'\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}', url):
            score += 3
        
        # Suspicious keywords in domain
        suspicious_words = ['verify', 'secure', 'bank', 'login', 'account']
        for word in suspicious_words:
            if word in url_lower:
                score += 1
        
        # Non-HTTPS
        if url.startswith('http://'):
            score += 1
        
        # Very long domains
        if len(url) > 50:
            score += 1
        
        # Multiple subdomains
        if url.count('.') > 3:
            score += 1
        
        confidence = min(score / 6.0, 1.0)
        is_fraud = confidence > 0.4
        
        risk_level = "HIGH" if confidence >= 0.7 else "MEDIUM" if confidence >= 0.4 else "LOW"
        
        message = "⚠️ MALICIOUS URL" if is_fraud else "✅ Safe URL"
        
        return {
            "is_fraud": is_fraud,
            "confidence": round(confidence, 4),
            "risk_level": risk_level,
            "message": message,
            "details": {"type": "URL", "url": url}
        }