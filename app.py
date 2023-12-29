# app.py
from flask import Flask, request, jsonify
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('tree.pkl') # Assume you already trained the model

# Endpoint to predict if a website is phishing or legitimate
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Assume 'data' contains features of the website

    # Preprocess the features (encode categorical variables, handle missing values, etc.)
    # ...

    # Make predictions using the trained model
    prediction = model.predict(data)

    # Return the prediction as JSON response
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(port=5000)























