# test_api.py
import requests
import json

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

# Make prediction request
response = requests.post('http://localhost:5000/predict', json=sample_data)
print("API Response:")
print(json.dumps(response.json(), indent=2))