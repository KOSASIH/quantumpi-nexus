import unittest
from src.main.ai_integration.ai_model import AIModel

class TestAIModel(unittest.TestCase):

    def setUp(self):
        self.model = AIModel()
        self.model.train(data=[1, 2, 3, 4, 5])  # Example training data

    def test_model_training(self):
        self.assertTrue(self.model.is_trained())

    def test_model_prediction(self):
        prediction = self.model.predict([6, 7, 8])
        self.assertIsInstance(prediction, list)  # Ensure prediction is a list
        self.assertEqual(len(prediction), 3)  # Assuming 3 inputs

    def test_model_accuracy(self):
        accuracy = self.model.evaluate(data=[1, 2, 3, 4, 5], labels=[1, 2, 3, 4, 5])
        self.assertGreaterEqual(accuracy, 0.8)  # Assuming we expect at least 80% accuracy

if __name__ == '__main__':
    unittest.main()
