import pandas as pd
import joblib

class ModelInference:
    def __init__(self, model_path='trained_model.joblib'):
        self.model = joblib.load(model_path)

    def predict(self, input_data):
        predictions = self.model.predict(input_data)
        return predictions

# Example usage
if __name__ == "__main__":
    inference = ModelInference()
    
    # Sample input data for prediction
    input_data = pd.DataFrame({
        'feature1': [1.0, 2.0],
        'feature2': [5.0, 6.0]
    })
    
    predictions = inference.predict(input_data)
    print("Predictions:", predictions)
