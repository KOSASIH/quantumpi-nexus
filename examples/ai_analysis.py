# ai_analysis.py - Example of AI-driven analytics

import numpy as np
from sklearn.linear_model import LinearRegression

class AIAnalytics:
    def __init__(self, data):
        self.data = data
        self.model = LinearRegression()

    def train_model(self):
        X = np.array(self.data['features']).reshape(-1, 1)
        y = np.array(self.data['target'])
        self.model.fit(X, y)

    def predict(self, new_data):
        return self.model.predict(np.array(new_data).reshape(-1, 1))

# Example usage
if __name__ == "__main__":
    data = {
        "features": [1, 2, 3, 4, 5],
        "target": [2, 3, 5, 7, 11]
    }
    analytics = AIAnalytics(data)
    analytics.train_model()
    prediction = analytics.predict([6])
    print(f"Predicted value for input 6: {prediction[0]}")
