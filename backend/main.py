"""
NEURA - Fraud & Phishing Detection API Server
FastAPI backend for mobile app
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
import sys
import os

# Add ml-model to path (try multiple locations for Render compatibility)
ml_model_paths = [
    os.path.join(os.path.dirname(__file__), '..', 'ml-model'),
    os.path.join(os.path.dirname(__file__), 'ml-model'),
    os.path.join(os.getcwd(), 'ml-model'),
    'ml-model'
]
for path in ml_model_paths:
    abs_path = os.path.abspath(path)
    if os.path.exists(abs_path) and abs_path not in sys.path:
        sys.path.append(abs_path)

from ml.fraud_detector import FraudDetector

# Initialize FastAPI app
app = FastAPI(
    title="NEURA Fraud Detection API",
    description="AI-Powered Fraud & Phishing Detection API",
    version="1.0.0"
)

# CORS middleware for mobile app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize fraud detector
detector = FraudDetector()


# Request/Response Models
class SMSRequest(BaseModel):
    text: str = Field(..., description="SMS text content")
    phone_number: Optional[str] = Field(None, description="Sender phone number")


class CallRequest(BaseModel):
    phone_number: str = Field(..., description="Phone number to check")
    call_duration: Optional[int] = Field(None, description="Call duration in seconds")


class EmailRequest(BaseModel):
    subject: str = Field(..., description="Email subject")
    body: str = Field(..., description="Email body content")
    sender: Optional[str] = Field(None, description="Sender email address")


class URLRequest(BaseModel):
    url: str = Field(..., description="URL to scan")


class ScanResponse(BaseModel):
    is_fraud: bool = Field(..., description="True if fraud detected, False if safe")
    confidence: float = Field(..., description="Confidence score (0.0 to 1.0)")
    risk_level: str = Field(..., description="Risk level: LOW, MEDIUM, HIGH")
    message: str = Field(..., description="Human-readable result message")
    details: Optional[dict] = Field(None, description="Additional detection details")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
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


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "model_loaded": detector.is_loaded()}


@app.post("/scan/sms", response_model=ScanResponse)
async def scan_sms(request: SMSRequest):
    """
    Scan SMS for fraud/phishing
    
    Args:
        request: SMSRequest with text and optional phone_number
        
    Returns:
        ScanResponse with fraud detection result
    """
    try:
        result = detector.detect_sms(request.text, request.phone_number)
        return ScanResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing SMS: {str(e)}")


@app.post("/scan/call", response_model=ScanResponse)
async def scan_call(request: CallRequest):
    """
    Scan phone number for scam/fraud
    
    Args:
        request: CallRequest with phone_number
        
    Returns:
        ScanResponse with fraud detection result
    """
    try:
        result = detector.detect_call(request.phone_number)
        return ScanResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing call: {str(e)}")


@app.post("/scan/email", response_model=ScanResponse)
async def scan_email(request: EmailRequest):
    """
    Scan email for phishing/fraud
    
    Args:
        request: EmailRequest with subject, body, and optional sender
        
    Returns:
        ScanResponse with fraud detection result
    """
    try:
        result = detector.detect_email(request.subject, request.body, request.sender)
        return ScanResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing email: {str(e)}")


@app.post("/scan/url", response_model=ScanResponse)
async def scan_url(request: URLRequest):
    """
    Scan URL for malicious content
    
    Args:
        request: URLRequest with url
        
    Returns:
        ScanResponse with fraud detection result
    """
    try:
        result = detector.detect_url(request.url)
        return ScanResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing URL: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)


