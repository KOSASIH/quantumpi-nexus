import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

class DataPreprocessing:
    def __init__(self):
        self.scaler = StandardScaler()
        self.imputer = SimpleImputer(strategy='mean')

    def preprocess(self, data):
        # Handle missing values
        data = self.imputer.fit_transform(data)
        
        # Normalize features
        data = self.scaler.fit_transform(data)
        
        return data

# Example usage
if __name__ == "__main__":
    # Sample data with missing values
    data = pd.DataFrame({
        'feature1': [1.0, 2.0, None, 4.0],
        'feature2': [5.0, None, 7.0, 8.0]
    })

    preprocessing = DataPreprocessing()
    processed_data = preprocessing.preprocess(data)
    print("Processed Data:\n", processed_data)
