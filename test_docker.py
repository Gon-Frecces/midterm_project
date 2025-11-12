# test_docker.py
import requests
import json
import time
import sys

def test_docker_container():
    """Test the Dockerized API"""
    print("=== TESTING DOCKERIZED API ===")
    
    # Wait for container to start
    print("Waiting for container to be ready...")
    time.sleep(10)
    
    sample_data = {
        "gender": "Male",
        "age": 35,
        "Investment_Avenues": "Yes", 
        "Mutual_Funds": 2,
        "Equity_Market": 4,
        "Debentures": 7,
        "Government_Bonds": 5,
        "Fixed_Deposits": 3,
        "PPF": 1,
        "Gold": 6,
        "Stock_Market": "Yes",
        "Factor": "Risk",
        "Objective": "Growth", 
        "Purpose": "Wealth Creation",
        "Duration": "Less than 1 year",
        "Invest_Monitor": "Weekly",
        "Expect": "20%-30%",
        "Avenue": "Public Provident Fund",
        "What are your savings objectives?": "Health Care",
        "Reason_Equity": "Dividend",
        "Reason_Mutual": "Fund Diversification", 
        "Reason_Bonds": "Assured Returns",
        "Reason_FD": "Fixed Returns"
    }
    
    max_retries = 10
    for attempt in range(max_retries):
        try:
            # Test health endpoint
            health_response = requests.get('http://localhost:5000/health', timeout=5)
            print(f"✅ Health check (attempt {attempt + 1}): {health_response.status_code}")
            
            if health_response.status_code == 200:
                # Test prediction endpoint
                response = requests.post(
                    'http://localhost:5000/predict', 
                    json=sample_data,
                    timeout=10
                )
                
                if response.status_code == 200:
                    result = response.json()
                    print(f"🎯 PREDICTION SUCCESSFUL!")
                    print(f"Predicted Source: {result['predicted_source']}")
                    print(f"Confidence: {result['confidence']:.4f}")
                    print(f"Status: {result['status']}")
                    return True
                else:
                    print(f" Prediction failed: {response.json()}")
            else:
                print(f"⏳ Container not ready yet...")
                
        except requests.exceptions.ConnectionError:
            print(f"⏳ Waiting for container to start... (attempt {attempt + 1}/{max_retries})")
            time.sleep(5)
        except Exception as e:
            print(f" Error: {e}")
            time.sleep(5)
    
    print(" Failed to connect to container after multiple attempts")
    return False

if __name__ == "__main__":
    success = test_docker_container()
    sys.exit(0 if success else 1)