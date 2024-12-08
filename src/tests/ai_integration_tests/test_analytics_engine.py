import unittest
from src.main.ai_integration.analytics_engine import AnalyticsEngine

class TestAnalyticsEngine(unittest.TestCase):

    def setUp(self):
        self.analytics = AnalyticsEngine()

    def test_generate_report(self):
        data = [1, 2, 3, 4, 5]
        report = self.analytics.generate_report(data)
        self.assertIn('mean', report)
        self.assertIn('median', report)
        self.assertIn('std_dev', report)

    def test_analyze_trends(self):
        data = [1, 2, 3, 4, 5]
        trends = self.analytics.analyze_trends(data)
        self.assertIsInstance(trends, dict)  # Expecting a dictionary of trends

    def test_predict_future_values(self):
        historical_data = [1, 2, 3, 4, 5]
        future_values = self.analytics.predict_future_values(historical_data, periods=3)
        self.assertEqual(len(future_values), 3)  # Expecting 3 future predictions

if __name__ == '__main__':
    unittest.main()
