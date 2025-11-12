# test_request.py
import requests
import json
import time

def test_api():
    """Test the prediction API with sample data"""
    
    # Sample data for prediction
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
    
    print("=== TESTING SOURCE PREDICTION API ===")
    
    # Test health endpoint first
    try:
        health_response = requests.get('http://localhost:5000/health', timeout=5)
        print(f"Health check: {health_response.status_code}")
        print(f"Health response: {health_response.json()}")
    except requests.exceptions.ConnectionError:
        print("Cannot connect to API. Make sure predict.py is running!")
        return False
    except Exception as e:
        print(f"Health check failed: {e}")
        return False
    
    # Test prediction endpoint
    try:
        print(f"\nSending prediction request...")
        start_time = time.time()
        
        response = requests.post(
            'http://localhost:5000/predict', 
            json=sample_data,
            timeout=10
        )
        
        response_time = time.time() - start_time
        
        print(f"Response status: {response.status_code}")
        print(f"Response time: {response_time:.2f}s")
        
        if response.status_code == 200:
            result = response.json()
            print(f"\n🎯 PREDICTION RESULTS:")
            print(f"Predicted Source: {result['predicted_source']}")
            print(f"Confidence: {result['confidence']:.4f}")
            print(f"All Probabilities:")
            for source, prob in result['all_probabilities'].items():
                print(f"  {source}: {prob:.4f}")
            print(f"Status: {result['status']}")
        else:
            print(f"Prediction failed: {response.json()}")
            
        return True
        
    except Exception as e:
        print(f"Prediction test failed: {e}")
        return False

def test_multiple_requests():
    """Test with multiple different samples"""
    print(f"\n{'='*50}")
    print("TESTING MULTIPLE REQUESTS")
    print(f"{'='*50}")
    
    test_cases = [
        {
            "gender": "Female",
            "age": 28,
            "Investment_Avenues": "Yes", 
            "Mutual_Funds": 2,
            "Equity_Market": 3,
            "Debentures": 7,
            "Government_Bonds": 5,
            "Fixed_Deposits": 4,
            "PPF": 1,
            "Gold": 6,
            "Stock_Market": "Yes",
            "Factor": "Returns",
            "Objective": "Capital Appreciation", 
            "Purpose": "Wealth Creation",
            "Duration": "3-5 years",
            "Invest_Monitor": "Daily",
            "Expect": "10%-20%",
            "Avenue": "Mutual Fund",
            "What are your savings objectives?": "Health Care",
            "Reason_Equity": "Capital Appreciation",
            "Reason_Mutual": "Better Returns", 
            "Reason_Bonds": "Assured Returns",
            "Reason_FD": "Risk Free"
        },
        {
            "gender": "Male",
            "age": 45,
            "Investment_Avenues": "Yes", 
            "Mutual_Funds": 3,
            "Equity_Market": 6,
            "Debentures": 7,
            "Government_Bonds": 2,
            "Fixed_Deposits": 1,
            "PPF": 4,
            "Gold": 5,
            "Stock_Market": "No",
            "Factor": "Risk",
            "Objective": "Income", 
            "Purpose": "Retirement",
            "Duration": "More than 5 years",
            "Invest_Monitor": "Monthly",
            "Expect": "10%-20%",
            "Avenue": "Fixed Deposits",
            "What are your savings objectives?": "Retirement Plan",
            "Reason_Equity": "Liquidity",
            "Reason_Mutual": "Tax Benefits", 
            "Reason_Bonds": "Tax Incentives",
            "Reason_FD": "High Interest Rates"
        }
    ]
    
    for i, test_data in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i} ---")
        try:
            response = requests.post('http://localhost:5000/predict', json=test_data, timeout=10)
            if response.status_code == 200:
                result = response.json()
                print(f"Predicted: {result['predicted_source']} (Confidence: {result['confidence']:.4f})")
            else:
                print(f"Failed: {response.json()}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Test basic API functionality
    if test_api():
        # Test multiple requests if basic test passes
        test_multiple_requests()