import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import joblib

class ModelEvaluator:
    def __init__(self, model_path='trained_model.joblib'):
        self.model = joblib.load(model_path)

    def load_data(self, file_path):
        data = pd.read_csv(file_path)
        return data

    def evaluate_model(self, X, y):
        predictions = self.model.predict(X)
        mse = mean_squared_error(y, predictions)
        r2 = r2_score(y, predictions)
        print(f'Model Evaluation:\nMSE: {mse}\nR²: {r2}')

# Example usage
if __name__ == "__main__":
    evaluator = ModelEvaluator()
    data = evaluator.load_data('test_data.csv')  # Replace with your test data file
    X = data.drop('target', axis=1)
    y = data['target']
    evaluator.evaluate_model(X, y)
