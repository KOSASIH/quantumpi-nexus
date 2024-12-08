import unittest
from src.main.machine_learning.model_training import ModelTraining

class TestModelTraining(unittest.TestCase):

    def setUp(self):
        self.model_trainer = ModelTraining()
        self.training_data = [[1, 2], [2, 3], [3, 4], [4, 5]]
        self.labels = [0, 0, 1, 1]  # Example binary labels

    def test_train_model(self):
        model = self.model_trainer.train(self.training_data, self.labels)
        self.assertIsNotNone(model)  # Ensure a model is returned
        self.assertTrue(hasattr(model, 'predict'))  # Check if the model has a predict method

    def test_training_with_invalid_data(self):
        with self.assertRaises(ValueError):
            self.model_trainer.train([], self.labels)  # Empty training data

if __name__ == '__main__':
    unittest.main()
