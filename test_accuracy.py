#!/usr/bin/env python3
"""
Test script to verify NEURA detects both safe and fraud messages correctly
"""
import requests
import json

def test_detection_accuracy():
    """Test both safe and fraud detection"""
    base_url = "http://localhost:8000"
    
    print("Testing NEURA Detection Accuracy...")
    print("=" * 50)
    
    # Test cases: (text, expected_fraud, description)
    test_cases = [
        # FRAUD CASES (should detect as fraud)
        ("URGENT: Your account will be suspended. Click here to verify immediately!", True, "Urgent phishing SMS"),
        ("Congratulations! You won $50,000. Claim now: http://prize-claim.com", True, "Prize scam"),
        ("Your payment failed. Update your card details: http://secure-payment.com", True, "Payment scam"),
        ("ALERT: Suspicious activity detected. Verify identity: http://bank-verify.com", True, "Bank phishing"),
        
        # SAFE CASES (should detect as safe)
        ("Your order #12345 has been shipped. Track at: https://amazon.com/tracking", False, "Legitimate order update"),
        ("Thank you for your payment of $500. Transaction ID: TXN123456789", False, "Payment confirmation"),
        ("Your appointment is scheduled for tomorrow at 2 PM. See you then!", False, "Appointment reminder"),
        ("Welcome to our service! We're excited to have you on board.", False, "Welcome message"),
        ("Your monthly statement is ready. View at: https://yourbank.com/statements", False, "Bank statement"),
        ("Your delivery is out for delivery. Expected by 6 PM today.", False, "Delivery update"),
    ]
    
    correct_predictions = 0
    total_tests = len(test_cases)
    
    for i, (text, expected_fraud, description) in enumerate(test_cases, 1):
        try:
            print(f"\n{i}. Testing: {description}")
            print(f"   Text: {text[:60]}...")
            
            response = requests.post(f"{base_url}/scan/sms", 
                                   json={"text": text}, 
                                   timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                detected_fraud = result['is_fraud']
                confidence = result['confidence']
                
                if detected_fraud == expected_fraud:
                    print(f"   [OK] CORRECT: Detected as {'FRAUD' if detected_fraud else 'SAFE'} ({confidence:.1%})")
                    correct_predictions += 1
                else:
                    print(f"   [FAIL] WRONG: Expected {'FRAUD' if expected_fraud else 'SAFE'}, got {'FRAUD' if detected_fraud else 'SAFE'} ({confidence:.1%})")
            else:
                print(f"   [FAIL] API Error: {response.status_code}")
                
        except Exception as e:
            print(f"   [FAIL] Error: {e}")
    
    # Results
    accuracy = (correct_predictions / total_tests) * 100
    print("\n" + "=" * 50)
    print(f"ACCURACY RESULTS:")
    print(f"Correct: {correct_predictions}/{total_tests}")
    print(f"Accuracy: {accuracy:.1f}%")
    
    if accuracy >= 80:
        print("SUCCESS: Detection is working properly!")
    elif accuracy >= 60:
        print("GOOD: Detection is mostly working")
    else:
        print("POOR: Detection needs improvement")
    
    return accuracy >= 70

if __name__ == "__main__":
    try:
        # Check if server is running
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code != 200:
            print("[FAIL] Backend server not running. Start with: cd backend && python main.py")
            exit(1)
            
        success = test_detection_accuracy()
        exit(0 if success else 1)
        
    except requests.exceptions.ConnectionError:
        print("[FAIL] Cannot connect to backend. Start server first!")
        exit(1)
    except Exception as e:
        print(f"[FAIL] Error: {e}")
        exit(1)