#!/usr/bin/env python3
"""
Quick test script to verify NEURA backend is working
"""
import requests
import json
import sys

def test_backend():
    """Test if backend is running and working"""
    base_url = "http://localhost:8000"
    
    print("Testing NEURA Backend...")
    print("=" * 50)
    
    # Test 1: Health check
    try:
        print("1. Testing health endpoint...")
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("   [OK] Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"   [FAIL] Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("   [FAIL] Cannot connect to backend server")
        print("   TIP: Make sure to start the server with: cd backend && python main.py")
        return False
    except Exception as e:
        print(f"   [FAIL] Health check error: {e}")
        return False
    
    # Test 2: SMS scan
    try:
        print("\n2. Testing SMS scan...")
        data = {
            "text": "URGENT: Your account will be suspended. Click here to verify immediately!",
            "phone_number": "+1234567890"
        }
        response = requests.post(f"{base_url}/scan/sms", json=data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            print("   [OK] SMS scan working")
            print(f"   Fraud detected: {result['is_fraud']}")
            print(f"   Confidence: {result['confidence']:.2%}")
            print(f"   Risk level: {result['risk_level']}")
        else:
            print(f"   [FAIL] SMS scan failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False
    except Exception as e:
        print(f"   [FAIL] SMS scan error: {e}")
        return False
    
    # Test 3: URL scan
    try:
        print("\n3. Testing URL scan...")
        data = {"url": "http://suspicious-bank-verify.com/login"}
        response = requests.post(f"{base_url}/scan/url", json=data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            print("   [OK] URL scan working")
            print(f"   Fraud detected: {result['is_fraud']}")
            print(f"   Confidence: {result['confidence']:.2%}")
            print(f"   Risk level: {result['risk_level']}")
        else:
            print(f"   [FAIL] URL scan failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"   [FAIL] URL scan error: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("SUCCESS: All tests passed! Backend is working correctly.")
    print("\nMobile app should now be able to connect to:")
    print(f"   - Emulator: http://10.0.2.2:8000/")
    print(f"   - Physical device: http://YOUR_COMPUTER_IP:8000/")
    return True

if __name__ == "__main__":
    try:
        success = test_backend()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user.")
    except Exception as e:
        print(f"\nERROR: Unexpected error: {e}")