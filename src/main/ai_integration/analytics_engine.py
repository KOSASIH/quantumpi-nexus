import pandas as pd
from ai_model import AIModel
from data_preprocessing import DataPreprocessing

class AnalyticsEngine:
    def __init__(self):
        self.data_preprocessor = DataPreprocessing()
        self.ai_model = AIModel()

    def run_analysis(self, raw_data):
        # Preprocess the data
        processed_data = self.data_preprocessor.preprocess(raw_data)
        
        # Split processed data into features and target
        X = processed_data[:, :-1]  # All columns except the last
        y = processed_data[:, -1]   # Last column as target
        
        # Train the AI model
        self.ai_model.train(pd.DataFrame(X), pd.Series(y))
        
        # Make predictions
        predictions = self.ai_model.predict(pd.DataFrame(X))
        return predictions

# Example usage
if __name__ == "__main__":
    # Sample raw data
    raw_data = pd.DataFrame({
        'feature1': [1.0, 2.0, 3.0, 4.0],
        'feature2': [5.0, 6.0, 7.0, 8.0],
        'target': [1.5, 2.5, 3.5, 4.5]
    })

    analytics_engine = AnalyticsEngine()
    predictions = analytics_engine.run_analysis(raw_data)
    print("Predictions from Analytics Engine:", predictions)
