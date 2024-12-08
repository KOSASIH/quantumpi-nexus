import unittest
from src.main.ai_integration.data_preprocessing import DataPreprocessing

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        self.preprocessing = DataPreprocessing()

    def test_clean_data(self):
        raw_data = [None, 1, 2, None, 3]
        cleaned_data = self.preprocessing.clean_data(raw_data)
        self.assertEqual(cleaned_data, [1, 2, 3])  # Expecting None values to be removed

    def test_normalize_data(self):
        data = [1, 2, 3, 4, 5]
        normalized_data = self.preprocessing.normalize_data(data)
        self.assertEqual(normalized_data, [0, 0.25, 0.5, 0.75, 1])  # Normalized values

    def test_split_data(self):
        data = [1, 2, 3, 4, 5]
        train_data, test_data = self.preprocessing.split_data(data, test_size=0.2)
        self.assertEqual(len(train_data), 4)  # 80% of 5
        self.assertEqual(len(test_data), 1)   # 20% of 5

if __name__ == '__main__':
    unittest.main()
