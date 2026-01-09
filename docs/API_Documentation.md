# NEURA API Documentation

Base URL: `http://localhost:8000` (or your server IP)

## Endpoints

### 1. Root Endpoint

**GET** `/`

Returns API information.

**Response:**
```json
{
  "name": "NEURA Fraud Detection API",
  "version": "1.0.0",
  "status": "operational",
  "endpoints": {
    "sms": "/scan/sms",
    "call": "/scan/call",
    "email": "/scan/email",
    "url": "/scan/url"
  }
}
```

### 2. Health Check

**GET** `/health`

Check API and model status.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### 3. Scan SMS

**POST** `/scan/sms`

Scan SMS text for fraud/phishing.

**Request Body:**
```json
{
  "text": "URGENT: Your account will be suspended. Click here to verify",
  "phone_number": "+1234567890"  // Optional
}
```

**Response:**
```json
{
  "is_fraud": true,
  "confidence": 0.85,
  "risk_level": "HIGH",
  "message": "⚠️ FRAUD DETECTED - High risk of phishing/scam (Confidence: 85.0%)",
  "details": {
    "type": "SMS",
    "phone_number": "+1234567890",
    "text_length": 65
  }
}
```

### 4. Scan Call

**POST** `/scan/call`

Check if phone number is a scam/fraud.

**Request Body:**
```json
{
  "phone_number": "+1234567890",
  "call_duration": 120  // Optional, in seconds
}
```

**Response:**
```json
{
  "is_fraud": false,
  "confidence": 0.2,
  "risk_level": "LOW",
  "message": "✅ Safe Number - Number appears safe (Confidence: 20.0%)",
  "details": {
    "type": "CALL",
    "phone_number": "+1234567890"
  }
}
```

### 5. Scan Email

**POST** `/scan/email`

Detect phishing/fraud in email.

**Request Body:**
```json
{
  "subject": "Verify your account",
  "body": "Click here to verify your account: http://verify.com",
  "sender": "noreply@example.com"  // Optional
}
```

**Response:**
```json
{
  "is_fraud": true,
  "confidence": 0.78,
  "risk_level": "MEDIUM",
  "message": "⚠️ PHISHING EMAIL - High risk of phishing (Confidence: 78.0%)",
  "details": {
    "type": "EMAIL",
    "sender": "noreply@example.com",
    "subject": "Verify your account"
  }
}
```

### 6. Scan URL

**POST** `/scan/url`

Analyze URL for malicious content.

**Request Body:**
```json
{
  "url": "http://suspicious-site.com/verify"
}
```

**Response:**
```json
{
  "is_fraud": true,
  "confidence": 0.65,
  "risk_level": "MEDIUM",
  "message": "⚠️ MALICIOUS URL - This URL is likely malicious (Confidence: 65.0%)",
  "details": {
    "type": "URL",
    "url": "http://suspicious-site.com/verify",
    "domain": "suspicious-site.com"
  }
}
```

## Response Fields

### Common Response Structure

All scan endpoints return the same structure:

- `is_fraud` (boolean): `true` if fraud detected, `false` if safe
- `confidence` (float): Confidence score from 0.0 to 1.0
- `risk_level` (string): `LOW`, `MEDIUM`, or `HIGH`
- `message` (string): Human-readable result message
- `details` (object): Additional information about the scan

### Risk Levels

- **LOW**: Confidence < 0.4 - Likely safe
- **MEDIUM**: 0.4 ≤ Confidence < 0.7 - Suspicious
- **HIGH**: Confidence ≥ 0.7 - High risk of fraud

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Error message here"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Error processing request: error details"
}
```

## Example Requests

### cURL Examples

**Scan SMS:**
```bash
curl -X POST "http://localhost:8000/scan/sms" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "URGENT: Your account will be suspended",
    "phone_number": "+1234567890"
  }'
```

**Scan URL:**
```bash
curl -X POST "http://localhost:8000/scan/url" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "http://example.com"
  }'
```

### Python Example

```python
import requests

response = requests.post(
    "http://localhost:8000/scan/sms",
    json={
        "text": "URGENT: Your account will be suspended",
        "phone_number": "+1234567890"
    }
)

result = response.json()
print(f"Fraud: {result['is_fraud']}")
print(f"Confidence: {result['confidence']}")
```

## Rate Limiting

Currently, no rate limiting is implemented. For production, implement rate limiting based on your requirements.

## CORS

CORS is enabled for all origins. In production, restrict to specific domains.


