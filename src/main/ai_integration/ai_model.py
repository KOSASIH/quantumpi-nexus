import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

class AIModel:
    def __init__(self, model_path='model.joblib'):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model_path = model_path

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f'Model trained with MSE: {mse}')
        self.save_model()

    def predict(self, X):
        return self.model.predict(X)

    def save_model(self):
        joblib.dump(self.model, self.model_path)
        print(f'Model saved to {self.model_path}')

    def load_model(self):
        self.model = joblib.load(self.model_path)
        print(f'Model loaded from {self.model_path}')

# Example usage
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'feature1': np.random.rand(100),
        'feature2': np.random.rand(100),
        'target': np.random.rand(100)
    })
    
    X = data[['feature1', 'feature2']]
    y = data['target']

    ai_model = AIModel()
    ai_model.train(X, y)
    predictions = ai_model.predict(X)
    print("Predictions:", predictions)
