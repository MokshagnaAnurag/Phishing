"""
Quick test script for NEURA API
Run this after starting the backend server to verify endpoints work
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("Testing /health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print("✅ Health check passed\n")
        return True
    except Exception as e:
        print(f"❌ Health check failed: {e}\n")
        return False

def test_scan_sms():
    """Test SMS scanning"""
    print("Testing /scan/sms endpoint...")
    try:
        data = {
            "text": "URGENT: Your account will be suspended. Click here to verify",
            "phone_number": "+1234567890"
        }
        response = requests.post(f"{BASE_URL}/scan/sms", json=data)
        print(f"Status: {response.status_code}")
        result = response.json()
        print(f"Result: {json.dumps(result, indent=2)}")
        print(f"✅ SMS scan test passed - Fraud: {result['is_fraud']}, Confidence: {result['confidence']}\n")
        return True
    except Exception as e:
        print(f"❌ SMS scan test failed: {e}\n")
        return False

def test_scan_url():
    """Test URL scanning"""
    print("Testing /scan/url endpoint...")
    try:
        data = {
            "url": "http://verify-bank-account.com"
        }
        response = requests.post(f"{BASE_URL}/scan/url", json=data)
        print(f"Status: {response.status_code}")
        result = response.json()
        print(f"Result: {json.dumps(result, indent=2)}")
        print(f"✅ URL scan test passed - Fraud: {result['is_fraud']}, Confidence: {result['confidence']}\n")
        return True
    except Exception as e:
        print(f"❌ URL scan test failed: {e}\n")
        return False

def test_scan_email():
    """Test email scanning"""
    print("Testing /scan/email endpoint...")
    try:
        data = {
            "subject": "Verify your account",
            "body": "Click here to verify: http://verify.com",
            "sender": "noreply@example.com"
        }
        response = requests.post(f"{BASE_URL}/scan/email", json=data)
        print(f"Status: {response.status_code}")
        result = response.json()
        print(f"Result: {json.dumps(result, indent=2)}")
        print(f"✅ Email scan test passed - Fraud: {result['is_fraud']}, Confidence: {result['confidence']}\n")
        return True
    except Exception as e:
        print(f"❌ Email scan test failed: {e}\n")
        return False

def main():
    print("=" * 50)
    print("NEURA API Test Suite")
    print("=" * 50)
    print()
    
    # Check if server is running
    if not test_health():
        print("❌ Backend server is not running!")
        print("Start it with: cd backend && python main.py")
        return
    
    # Run tests
    results = []
    results.append(("Health Check", test_health()))
    results.append(("SMS Scan", test_scan_sms()))
    results.append(("URL Scan", test_scan_url()))
    results.append(("Email Scan", test_scan_email()))
    
    # Summary
    print("=" * 50)
    print("Test Summary")
    print("=" * 50)
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name}: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! API is working correctly.")
    else:
        print("\n⚠️ Some tests failed. Check the errors above.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


