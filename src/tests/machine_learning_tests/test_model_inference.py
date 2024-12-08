import unittest
from src.main.machine_learning.model_inference import ModelInference

class TestModelInference(unittest.TestCase):

    def setUp(self):
        self.inference = ModelInference()
        self.model = self.inference.train_model([[1, 2], [2, 3]], [0, 1])  # Example training

    def test_inference_on_new_data(self):
        new_data = [[1, 2], [3, 4]]
        predictions = self.inference.predict(self.model, new_data)
        self.assertEqual(len(predictions), 2)  # Expecting predictions for 2 new data points

    def test_inference_with_invalid_data(self):
        with self.assertRaises(ValueError):
            self.inference.predict(self.model, [])  # Empty new data

if __name__ == '__main__':
    unittest.main()
