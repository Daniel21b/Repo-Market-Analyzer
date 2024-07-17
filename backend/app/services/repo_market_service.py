import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from app.utils.data_fetcher import fetch_stfm_data
from app.utils.data_preprocessor import preprocess_data
from app.utils.feature_engineering import engineer_features

class RepoMarketService:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.data = None

    def fetch_and_prepare_data(self, mnemonic):
        raw_data = fetch_stfm_data(mnemonic)
        preprocessed_data = preprocess_data(raw_data)
        self.data = engineer_features(preprocessed_data)
    
    def train_model(self):
        if self.data is None:
            raise Exception("Data not loaded. Fetch and preprocess data first.")
        
        X = self.data.drop('target', axis=1)  # Replace 'target' with actual target column
        y = self.data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.model.fit(X_train, y_train)
        accuracy = self.model.score(X_test, y_test)
        return accuracy
    
    def predict_interest_rate(self, input_data):
        features = np.array([input_data['feature1'], input_data['feature2']]).reshape(1, -1)
        prediction = self.model.predict(features)
        return prediction[0]
    
    def analyze_market(self, input_data):
        # Placeholder for market analysis logic
        analysis_result = {
            'trend': 'upward',
            'volatility': 'low'
        }
        return analysis_result

    def assess_risk(self, input_data):
        # Placeholder for risk assessment logic
        risk_assessment = {
            'risk_level': 'medium',
            'recommendation': 'proceed with caution'
        }
        return risk_assessment
