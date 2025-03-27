# ai_integration/predictive_insights.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

class PredictiveInsights:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def prepare_data(self, data):
        """Prepare data for training the model."""
        data['price_change'] = data['close'].pct_change()
        data.dropna(inplace=True)
        
        X = data[['open', 'high', 'low', 'volume']]
        y = data['close'].shift(-1).dropna()
        X = X[:-1]  # Align X with y
        
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self, data):
        """Train the predictive model."""
        X_train, X_test, y_train, y_test = self.prepare_data(data)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        
        mse = mean_squared_error(y_test, predictions)
        print(f"Model trained with Mean Squared Error: {mse:.4f}")

    def predict(self, new_data):
        """Make predictions on new data."""
        return self.model.predict(new_data)

    def evaluate_model(self, data):
        """Evaluate the model's performance."""
        X_train, X_test, y_train, y_test = self.prepare_data(data)
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Model evaluation completed with Mean Squared Error: {mse:.4f}")
