import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

class ModelTrainer:
    def __init__(self, model_path='trained_model.joblib'):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model_path = model_path

    def load_data(self, file_path):
        data = pd.read_csv(file_path)
        return data

    def preprocess_data(self, data):
        # Simple preprocessing: drop missing values and separate features and target
        data = data.dropna()
        X = data.drop('target', axis=1)
        y = data['target']
        return X, y

    def train_model(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f'Model trained with MSE: {mse}')
        self.save_model()

    def save_model(self):
        joblib.dump(self.model, self.model_path)
        print(f'Model saved to {self.model_path}')

# Example usage
if __name__ == "__main__":
    trainer = ModelTrainer()
    data = trainer.load_data('data.csv')  # Replace with your data file
    X, y = trainer.preprocess_data(data)
    trainer.train_model(X, y)
