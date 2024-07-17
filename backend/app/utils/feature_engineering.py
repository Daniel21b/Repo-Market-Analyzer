import pandas as pd

def engineer_features(data):
    # Example feature engineering steps
    
    # Extract borrowing history
    data['borrow_history'] = data['loan_amount'].rolling(window=12).sum()
    
    # Calculate economic indicators (example: moving average)
    data['moving_avg'] = data['interest_rate'].rolling(window=12).mean()
    
    # Derive additional features
    data['new_feature'] = data['feature1'] * data['feature2']
    
    return data
