import unittest
from src.main.machine_learning.model_evaluation import ModelEvaluation

class TestModelEvaluation(unittest.TestCase):

    def setUp(self):
        self.evaluator = ModelEvaluation()
        self.predictions = [0, 1, 1, 0]
        self.labels = [0, 1, 1, 1]

    def test_accuracy(self):
        accuracy = self.evaluator.calculate_accuracy(self.predictions, self.labels)
        self.assertAlmostEqual(accuracy, 0.75)  # 3 correct out of 4

    def test_confusion_matrix(self):
        cm = self.evaluator.get_confusion_matrix(self.predictions, self.labels)
        self.assertEqual(cm['TP'], 2)  # True Positives
        self.assertEqual(cm['TN'], 1)  # True Negatives
        self.assertEqual(cm['FP'], 0)  # False Positives
        self.assertEqual(cm['FN'], 1)  # False Negatives

if __name__ == '__main__':
    unittest.main()
