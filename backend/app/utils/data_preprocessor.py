import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def preprocess_data(data):
    # Convert to DataFrame
    df = pd.DataFrame(data['series_data'])
    
    # Handle missing values
    df.fillna(method='ffill', inplace=True)
    
    # Encode categorical variables
    encoder = OneHotEncoder()
    categorical_features = ['category1', 'category2']  # Replace with actual categories
    encoded_features = encoder.fit_transform(df[categorical_features])
    
    # Normalize numerical features
    scaler = StandardScaler()
    numerical_features = ['feature1', 'feature2']  # Replace with actual features
    scaled_features = scaler.fit_transform(df[numerical_features])
    
    # Combine processed features
    processed_data = pd.concat([pd.DataFrame(encoded_features.toarray()), pd.DataFrame(scaled_features)], axis=1)
    
    return processed_data
