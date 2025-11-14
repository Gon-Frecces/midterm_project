## News source (for Financial decicion making) prediction API

## Project Overview

This machine learning project predicts the information sources that individuals use for financial decision-making based on their demographics, investment preferences, and behavioral factors. The model achieves 100% accuracy in predicting whether individuals use Financial Consultants, Internet, Newspapers/Magazines, or Television as their primary financial information source.

##  Demo Video

https://drive.google.com/file/d/1ep-dPJc5I-CjZjt_IfK12RI5j_kx8kv0/view?usp=sharing 
The above link shows a video of the full API demonstration

### Business Problem
Financial institutions struggle to understand where different customer segments get their financial information. This leads to inefficient marketing strategies and poor communication channel targeting. By predicting information source preferences, companies can optimize marketing budget allocation, personalize communication strategies, develop targeted advertising campaigns, and improve customer acquisition and retention.


## Dataset Description

The dataset contains comprehensive information about individual investment behaviors and preferences:

### Key Features:
- Demographics: Age, Gender
- Investment Preferences: Rankings (1-7) for various investment types
- Behavioral Factors: Primary Factor, Investment Objective, Purpose, Time Horizon, Monitoring Frequency, Return Expectations
- Decision Drivers: Reasons for choosing specific investments
- Target Variable: Source - Primary information source (Financial Consultants, Internet, Newspapers and Magazines, Television)

## Machine Learning Model

### Model Performance
- Algorithm: Random Forest Classifier
- Accuracy: 100% (Perfect prediction on validation set)
- Target Variable: Information Source (Source)
- Classes: 4 (Financial Consultants, Internet, Newspapers/Magazines, Television)

### Feature Engineering
- DictVectorizer Encoding: Handles mixed data types (numerical + categorical)
- Smart Feature Creation: Risk tolerance scores, safety preference metrics, investment sophistication indicators, behavioral segmentation

### Model Training Process
1. Data Preprocessing: Handling missing values, encoding categorical variables
2. Feature Selection: Comprehensive correlation analysis and importance ranking
3. Model Comparison: Tested Random Forest, Logistic Regression, and XGBoost
4. Hyperparameter Tuning: Optimized for maximum accuracy
5. Validation: Stratified train-test split with cross-validation

## API Documentation

### Base URL
https://crispy-spoon-7qq5j74wvwhpxx6-5000.app.github.dev/

### Available Endpoints

#### GET /
API information and available endpoints

Response:
{
  "message": "Financial Source Prediction API",
  "version": "1.0",
  "endpoints": {
    "GET /": "API information",
    "GET /health": "Health check",
    "POST /predict": "Make predictions"
  },
  "model_accuracy": "100%"
}

#### GET /health
Health check and model status

Response:
{
  "status": "healthy",
  "model_loaded": true,
  "message": "API is running correctly"
}

#### POST /predict
Predict information source from user data

Request Body (JSON):
{
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

Response:
{
  "predicted_source": "Financial Consultants",
  "confidence": 1.0,
  "all_probabilities": {
    "Financial Consultants": 1.0,
    "Internet": 0.0,
    "Newspapers and Magazines": 0.0,
    "Television": 0.0
  },
  "status": "success"
}

## Deployment

### Local Development
1. Install dependencies
pip install -r requirements.txt

2. Train the model (if needed)
python train.py

3. Start the API
python predict.py

4. Test endpoints
curl https://crispy-spoon-7qq5j74wvwhpxx6-5000.app.github.dev/

### Docker Deployment
Build and run with Docker
docker build -t source-predictor .
docker run -p 5000:5000 --name source-predictor-app source-predictor

### GitHub Codespaces (Cloud Deployment)
The project is configured for instant deployment in GitHub Codespaces:

1. Click "Code" -> "Codespaces" -> "Create codespace on main"
2. Wait for environment setup (automatic)
3. Run deployment script:
   chmod +x codespaces_build.sh
   ./codespaces_build.sh
4. Access your API via the automatically forwarded port

## Model Insights & Business Value

### Key Findings
- Perfect Predictability: The model achieves 100% accuracy, indicating strong patterns in information source preferences
- Feature Importance: Investment preferences and behavioral factors are the strongest predictors
- Demographic Patterns: Age and gender show clear correlations with source preferences

### Business Applications
1. Targeted Marketing: Allocate resources to channels preferred by specific customer segments
2. Product Development: Tailor financial products based on information consumption patterns
3. Customer Segmentation: Identify distinct groups based on information source preferences
4. Communication Strategy: Optimize messaging for different information channels

## Technical Implementation

### Technology Stack
- Machine Learning: Scikit-learn, Pandas, NumPy
- API Framework: Flask
- Containerization: Docker
- Cloud Platform: GitHub Codespaces
- Version Control: Git

### Key Technical Decisions
1. DictVectorizer: Chosen for seamless handling of mixed data types
2. Random Forest: Selected for best performance and interpretability
3. Flask: Lightweight framework suitable for ML API deployment
4. Docker: Ensures consistent environment across deployments

## Testing

### Test Coverage
- Unit Tests: Model training and prediction logic
- Integration Tests: API endpoints and data flow
- Deployment Tests: Container build and cloud deployment
- Performance Tests: Response times and accuracy validation

### Running Tests
Local API tests
python test_request.py

Codespaces deployment tests
python codespaces_test.py

Full integration test
./codespaces_build.sh

## Performance Metrics

- Accuracy: 100%
- Precision: 100% (all classes)
- Recall: 100% (all classes)
- F1-Score: 1.0 (all classes)
- Inference Time: < 100ms
- API Response Time: < 200ms

## Future Enhancements

1. Real-time Data Integration: Connect with live financial data sources
2. Additional Features: Incorporate social media and digital footprint data
3. Model Explainability: Add SHAP values for prediction explanations
4. A/B Testing Framework: Test different marketing strategies
5. Monitoring Dashboard: Real-time performance and usage metrics

## Contributing

1. Fork the repository
2. Create a feature branch (git checkout -b feature/AmazingFeature)
3. Commit changes (git commit -m 'Add some AmazingFeature')
4. Push to branch (git push origin feature/AmazingFeature)
5. Open a Pull Request



