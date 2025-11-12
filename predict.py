# predict.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model artifacts
try:
    model_artifacts = joblib.load('source_model.joblib')
    model = model_artifacts['model']
    dv = model_artifacts['dict_vectorizer']
    le = model_artifacts['label_encoder']
    print("Model loaded successfully!")
except:
    print("Model not found. Please run train.py first.")
    exit(1)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Financial Source Prediction API',
        'version': '1.0',
        'status': 'running',
        'endpoints': {
            'GET /': 'API information',
            'GET /health': 'Health check',
            'POST /predict': 'Make predictions'
        },
        'model_accuracy': '100%',
        'instructions': 'Send POST request to /predict with user data'
    })

@app.route('/predict', methods=['POST'])
def predict_source():
    """
    Predict information source from user data
    Expects JSON with all feature columns except 'Source'
    """
    try:
        # Get JSON data
        data = request.get_json()
        
        # Convert to DataFrame
        user_data = pd.DataFrame([data])
        
        # Preprocess
        user_data = user_data.fillna(0)
        
        # Transform using DictVectorizer
        user_dict = user_data.to_dict(orient='records')[0]
        X_encoded = dv.transform([user_dict])
        
        # Make prediction
        prediction_encoded = model.predict(X_encoded)[0]
        prediction_proba = model.predict_proba(X_encoded)[0]
        
        # Convert back to original label
        predicted_source = le.inverse_transform([prediction_encoded])[0]
        confidence = prediction_proba[prediction_encoded]
        
        # Prepare response
        response = {
            'predicted_source': predicted_source,
            'confidence': float(confidence),
            'all_probabilities': {
                source: float(prob) for source, prob in zip(le.classes_, prediction_proba)
            },
            'status': 'success'
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy', 
        'model_loaded': True,
        'message': 'API is running correctly'
    })

if __name__ == '__main__':
    print("Starting Flask server for Source Prediction API...")
    print("Endpoints:")
    print("   GET  /         - API information")
    print("   GET  /health   - Health check")
    print("   POST /predict  - Predict information source")
    app.run(host='0.0.0.0', port=5000, debug=True)