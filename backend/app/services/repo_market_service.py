# app/services/repo_market_service.py
import pandas as pd
import numpy as np
import logging
import joblib

from app.utils.data_fetcher import fetch_stfm_data
from app.utils.data_preprocessor import preprocess_data
from app.utils.feature_engineering import engineer_features
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

class RepoMarketService:
    def __init__(self):
        self.model = None
        self.features = None
        self.load_model()

    def fetch_and_prepare_data(self, mnemonic):
        raw_data = fetch_stfm_data(mnemonic)
        preprocessed_data = preprocess_data(raw_data)
        engineered_data = engineer_features(preprocessed_data)
        return engineered_data

    def train_model(self):
        try:
            data = self.fetch_and_prepare_data("REPO_RATE")
            self.features = ['feature1', 'feature2', 'feature3']
            X = data[self.features]
            y = data['interest_rate']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
            self.model.fit(X_train, y_train)

            y_pred = self.model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            accuracy = 1 - np.sqrt(mse) / np.mean(y_test)

            joblib.dump(self.model, 'path/to/saved_model.pkl')
            logging.info(f"Model trained successfully with accuracy: {accuracy}")
            return accuracy
        except Exception as e:
            logging.error(f"Error training model: {e}")
            raise

    def load_model(self):
        try:
            self.model = joblib.load('path/to/saved_model.pkl')
            logging.info("Model loaded successfully.")
        except FileNotFoundError:
            logging.error("Model file not found. Make sure to train the model first.")
        except Exception as e:
            logging.error(f"Error loading model: {e}")
            raise

    def predict_interest_rate(self, data):
        if self.model is None:
            raise ValueError("Model has not been trained yet. Call train_model() first.")
        
        try:
            input_data = pd.DataFrame([data])
            input_features = input_data[self.features]
            predicted_rate = self.model.predict(input_features)[0]
            logging.info(f"Predicted interest rate: {predicted_rate}")
            return predicted_rate
        except Exception as e:
            logging.error(f"Error predicting interest rate: {e}")
            raise

    def analyze_market(self, data):
        try:
            market_data = self.fetch_and_prepare_data("MARKET_INDEX")
            current_rate = data['interest_rate']
            market_average = market_data['interest_rate'].mean()
            market_volatility = market_data['interest_rate'].std()

            if current_rate > market_average + market_volatility:
                market_condition = "High interest rate environment"
            elif current_rate < market_average - market_volatility:
                market_condition = "Low interest rate environment"
            else:
                market_condition = "Stable interest rate environment"

            analysis = {
                "current_rate": current_rate,
                "market_average": market_average,
                "market_volatility": market_volatility,
                "market_condition": market_condition
            }

            logging.info(f"Market analysis: {analysis}")
            return analysis
        except Exception as e:
            logging.error(f"Error analyzing market: {e}")
            raise

    def assess_risk(self, data):
        try:
            historical_data = self.fetch_and_prepare_data("HISTORICAL_RATES")
            rate_volatility = historical_data['interest_rate'].std()
            max_drawdown = (historical_data['interest_rate'].cummax() - historical_data['interest_rate']).max()

            if rate_volatility > 0.5 and max_drawdown > 0.1:
                risk_level = "High"
            elif rate_volatility > 0.3 or max_drawdown > 0.05:
                risk_level = "Medium"
            else:
                risk_level = "Low"

            risk_assessment = {
                "rate_volatility": rate_volatility,
                "max_drawdown": max_drawdown,
                "risk_level": risk_level
            }

            logging.info(f"Risk assessment: {risk_assessment}")
            return risk_assessment
        except Exception as e:
            logging.error(f"Error assessing risk: {e}")
            raise
