from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__, template_folder='templates')
CORS(app)  # Enable CORS for cross-domain requests

# Load the trained model (ensure that the model file exists)
try:
    model = joblib.load('model/fake_profile_model.pkl')
except Exception as e:
    print("Model could not be loaded. Please run the training script first.")
    model = None

def extract_features(profile_url):
    """
    Dummy function to extract features from a profile URL.
    In a real-world scenario, you would scrape the profile or use an API.
    For demonstration, we return a random vector.
    """
    # Example features: [activity_score, completeness, language_score, engagement]
    return np.array([[0.5, 0.7, 0.6, 0.8]])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_profile():
    data = request.get_json()
    profile_url = data.get('profile_url', '')
    
    if not profile_url:
        return jsonify({'error': 'Profile URL is required.'}), 400

    # Feature extraction (dummy in this case)
    features = extract_features(profile_url)
    
    # Check if the model is loaded
    if model is None:
        return jsonify({'error': 'Model not available. Please train the model first.'}), 500
    
    # Predict using the trained model
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0].max() * 100

    # Map prediction to a human-readable result
    result = {
        'profile_url': profile_url,
        'prediction': 'Fake' if prediction == 1 else 'Real',
        'confidence': round(probability, 2)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
