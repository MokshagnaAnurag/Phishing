# NEURA Test Examples Guide

Test examples for all scan types with expected confidence levels.

## 📱 SMS Scan Examples

### 🔴 HIGH CONFIDENCE FRAUD (Expected: 70-95% confidence)

1. **Urgent Account Suspension**
   ```
   URGENT: Your account will be suspended in 24 hours. Click here to verify: http://bank-verify.com
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.70-0.95`

2. **Prize/Win Scam**
   ```
   Congratulations! You won ₹50,000. Claim now: www.prize-claim.in
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.75-0.90`

3. **Payment Failed Scam**
   ```
   Payment failed. Update your card details immediately: http://secure-payment.com
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.70-0.85`

4. **OTP Sharing Scam**
   ```
   Your OTP is 123456. Do not share with anyone. Bank will never ask for OTP.
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.65-0.80`

5. **Account Compromised**
   ```
   Your account has been compromised. Verify your identity: www.secure-bank.com
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.70-0.85`

### 🟠 MEDIUM CONFIDENCE (Expected: 40-70% confidence)

6. **Suspicious Link**
   ```
   Check out this amazing offer: http://deals-now.com/discount
   ```
   - Expected: `is_fraud: false/true`, `risk_level: MEDIUM`, `confidence: 0.40-0.60`

7. **Generic Urgency**
   ```
   Limited time offer! Get 50% discount. Act now!
   ```
   - Expected: `is_fraud: false/true`, `risk_level: MEDIUM`, `confidence: 0.45-0.65`

8. **Mixed Content**
   ```
   Your order #12345 has been shipped. Track at: http://tracking-link.com
   ```
   - Expected: `is_fraud: false`, `risk_level: MEDIUM`, `confidence: 0.40-0.60`

### 🟢 LOW CONFIDENCE SAFE (Expected: 20-40% confidence)

9. **Normal Order Update**
   ```
   Your order #12345 has been shipped. Track at: https://tracking.example.com
   ```
   - Expected: `is_fraud: false`, `risk_level: LOW`, `confidence: 0.20-0.40`

10. **Appointment Reminder**
    ```
    Your appointment is scheduled for tomorrow at 2 PM. See you then!
    ```
    - Expected: `is_fraud: false`, `risk_level: LOW`, `confidence: 0.15-0.30`

11. **Payment Confirmation**
    ```
    Thank you for your payment of ₹500. Transaction ID: TXN123456789
    ```
    - Expected: `is_fraud: false`, `risk_level: LOW`, `confidence: 0.20-0.35`

12. **Welcome Message**
    ```
    Welcome to our service! We're excited to have you on board.
    ```
    - Expected: `is_fraud: false`, `risk_level: LOW`, `confidence: 0.10-0.25`

---

## 📞 CALL Scan Examples

### 🔴 HIGH CONFIDENCE FRAUD

1. **Repeated Digits (Suspicious Pattern)**
   ```
   Phone: +91-1111111111
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.60-0.80`

2. **Very Short Number**
   ```
   Phone: 12345
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.70-0.85`

3. **Suspicious Pattern**
   ```
   Phone: +1-800-000-0000
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.65-0.80`

### 🟠 MEDIUM CONFIDENCE

4. **Generic Number**
   ```
   Phone: +91-9876543210
   ```
   - Expected: `is_fraud: false`, `risk_level: MEDIUM`, `confidence: 0.30-0.50`

5. **US Number**
   ```
   Phone: +1-555-123-4567
   ```
   - Expected: `is_fraud: false`, `risk_level: MEDIUM`, `confidence: 0.25-0.45`

### 🟢 LOW CONFIDENCE SAFE

6. **Normal Format**
   ```
   Phone: +44-20-7946-0958
   ```
   - Expected: `is_fraud: false`, `risk_level: LOW`, `confidence: 0.15-0.30`

---

## 📧 EMAIL Scan Examples

### 🔴 HIGH CONFIDENCE FRAUD

1. **Phishing with Urgency**
   ```
   Subject: Verify your account
   Body: Your account will be suspended. Click here to verify: http://verify-bank.com
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.75-0.90`

2. **Prize Email**
   ```
   Subject: Congratulations! You Won!
   Body: You have won $10,000! Claim now: www.prize-claim.com
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.70-0.85`

3. **Payment Request**
   ```
   Subject: Payment Required
   Body: Your payment failed. Update immediately: http://payment-update.com
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.70-0.85`

4. **Account Compromised**
   ```
   Subject: Security Alert
   Body: Unusual activity detected. Verify account: http://secure-verify.com
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.75-0.90`

### 🟠 MEDIUM CONFIDENCE

5. **Generic Marketing**
   ```
   Subject: Special Offer
   Body: Get 30% off on all products. Shop now: https://store.com
   ```
   - Expected: `is_fraud: false/true`, `risk_level: MEDIUM`, `confidence: 0.40-0.60`

6. **Newsletter with Link**
   ```
   Subject: Monthly Newsletter
   Body: Check out our latest updates: http://newsletter.com
   ```
   - Expected: `is_fraud: false`, `risk_level: MEDIUM`, `confidence: 0.35-0.55`

### 🟢 LOW CONFIDENCE SAFE

7. **Order Confirmation**
   ```
   Subject: Order Confirmation #12345
   Body: Your order has been confirmed. Track at: https://tracking.example.com
   ```
   - Expected: `is_fraud: false`, `risk_level: LOW`, `confidence: 0.20-0.40`

8. **Password Changed**
   ```
   Subject: Password Changed Successfully
   Body: Your password was changed. If this wasn't you, contact support.
   ```
   - Expected: `is_fraud: false`, `risk_level: LOW`, `confidence: 0.15-0.30`

9. **Welcome Email**
   ```
   Subject: Welcome to Our Service
   Body: Thank you for joining! We're excited to have you.
   ```
   - Expected: `is_fraud: false`, `risk_level: LOW`, `confidence: 0.10-0.25`

---

## 🔗 URL Scan Examples

### 🔴 HIGH CONFIDENCE FRAUD

1. **Verify/Bank Keywords**
   ```
   URL: http://verify-bank-account.com
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.65-0.80`

2. **Suspicious Domain**
   ```
   URL: http://secure-payment-update.com
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.60-0.75`

3. **IP Address (Suspicious)**
   ```
   URL: http://192.168.1.100/verify
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.75-0.90`

4. **HTTP (Not HTTPS)**
   ```
   URL: http://login-bank.com
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.55-0.70`

5. **Very Long Domain**
   ```
   URL: http://verify-your-bank-account-security-update-now.com
   ```
   - Expected: `is_fraud: true`, `risk_level: HIGH`, `confidence: 0.60-0.75`

### 🟠 MEDIUM CONFIDENCE

6. **Generic Suspicious**
   ```
   URL: http://claim-prize.com
   ```
   - Expected: `is_fraud: true/false`, `risk_level: MEDIUM`, `confidence: 0.45-0.65`

7. **Multiple Subdomains**
   ```
   URL: http://www.deals.offers.discount.com
   ```
   - Expected: `is_fraud: false/true`, `risk_level: MEDIUM`, `confidence: 0.40-0.60`

### 🟢 LOW CONFIDENCE SAFE

8. **Legitimate HTTPS**
   ```
   URL: https://www.example.com
   ```
   - Expected: `is_fraud: false`, `risk_level: LOW`, `confidence: 0.15-0.35`

9. **Known Domain**
   ```
   URL: https://github.com
   ```
   - Expected: `is_fraud: false`, `risk_level: LOW`, `confidence: 0.10-0.30`

10. **Normal Website**
    ```
    URL: https://tracking.example.com/orders/12345
    ```
    - Expected: `is_fraud: false`, `risk_level: LOW`, `confidence: 0.20-0.40`

---

## 🧪 Quick Test Script

Use these in the web frontend or API:

### High Confidence Fraud Tests:
```javascript
// SMS
{ text: "URGENT: Your account will be suspended. Click here to verify", phone_number: "+1234567890" }

// Email
{ subject: "Verify your account", body: "Your account will be suspended. Click here: http://verify.com" }

// URL
{ url: "http://verify-bank-account.com" }
```

### Medium Confidence Tests:
```javascript
// SMS
{ text: "Limited time offer! Get 50% discount. Act now!" }

// Email
{ subject: "Special Offer", body: "Get 30% off. Shop now: https://store.com" }
```

### Low Confidence Safe Tests:
```javascript
// SMS
{ text: "Your order #12345 has been shipped. Track at: https://tracking.example.com" }

// Email
{ subject: "Order Confirmation", body: "Your order has been confirmed. Thank you!" }

// URL
{ url: "https://www.example.com" }
```

---

## 📊 Expected Results Summary

| Type | Example | Expected Fraud | Expected Risk | Expected Confidence |
|------|---------|----------------|---------------|---------------------|
| SMS | Urgent account suspension | ✅ True | HIGH | 70-95% |
| SMS | Prize won scam | ✅ True | HIGH | 75-90% |
| SMS | Normal order update | ❌ False | LOW | 20-40% |
| Call | Repeated digits | ✅ True | HIGH | 60-80% |
| Call | Normal number | ❌ False | LOW | 15-30% |
| Email | Phishing with urgency | ✅ True | HIGH | 75-90% |
| Email | Generic marketing | ⚠️ Maybe | MEDIUM | 40-60% |
| Email | Order confirmation | ❌ False | LOW | 20-40% |
| URL | Verify bank account | ✅ True | HIGH | 65-80% |
| URL | IP address | ✅ True | HIGH | 75-90% |
| URL | HTTPS legitimate | ❌ False | LOW | 15-35% |

---

## 🎯 Testing Tips

1. **Start with High Confidence examples** - These should clearly show fraud detection
2. **Test Medium examples** - These show the model's decision boundary
3. **Verify Low examples** - These confirm the model doesn't over-detect
4. **Compare results** - Notice how confidence scores vary
5. **Check risk levels** - HIGH (≥70%), MEDIUM (40-70%), LOW (<40%)

---

**Note:** Actual confidence scores may vary slightly based on the trained model, but these examples should consistently produce results in the expected ranges.


