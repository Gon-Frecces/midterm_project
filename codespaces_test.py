# codespaces_test.py
import requests
import json
import time

def test_codespaces_api():
    print("=== CODESPACES API TEST ===")
    
    # In Codespaces, use the forwarded port
    base_url = "http://localhost:5000"
    
    sample_data = {
        "gender": "Male", "age": 35, "Investment_Avenues": "Yes", 
        "Mutual_Funds": 2, "Equity_Market": 4, "Debentures": 7,
        "Government_Bonds": 5, "Fixed_Deposits": 3, "PPF": 1, "Gold": 6,
        "Stock_Market": "Yes", "Factor": "Risk", "Objective": "Growth",
        "Purpose": "Wealth Creation", "Duration": "Less than 1 year",
        "Invest_Monitor": "Weekly", "Expect": "20%-30%",
        "Avenue": "Public Provident Fund", 
        "What are your savings objectives?": "Health Care",
        "Reason_Equity": "Dividend", "Reason_Mutual": "Fund Diversification",
        "Reason_Bonds": "Assured Returns", "Reason_FD": "Fixed Returns"
    }
    
    print("Testing endpoints...")
    
    endpoints = [
        ("GET", "/", "API Information"),
        ("GET", "/health", "Health Check"),
        ("POST", "/predict", "Prediction")
    ]
    
    for method, endpoint, description in endpoints:
        try:
            url = f"{base_url}{endpoint}"
            print(f"\n🔍 {description}: {method} {endpoint}")
            
            if method == "GET":
                response = requests.get(url, timeout=10)
            else:
                response = requests.post(url, json=sample_data, timeout=10)
            
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                if endpoint == "/predict":
                    print(f"    SUCCESS: {result['predicted_source']}")
                    print(f"    Confidence: {result['confidence']:.4f}")
                else:
                    print(f"   SUCCESS: {result}")
            else:
                print(f"    FAILED: {response.text}")
                
        except Exception as e:
            print(f"    ERROR: {e}")
            return False
    
    print("\n CODESPACES API TEST PASSED!")
    return True

if __name__ == "__main__":
    # Wait a bit for container to start
    print("Waiting for container to be ready...")
    time.sleep(5)
    test_codespaces_api()