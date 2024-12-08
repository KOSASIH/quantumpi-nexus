import unittest
from src.main.quantum_security.quantum_key_distribution import QuantumKeyDistribution

class TestQuantumKeyDistribution(unittest.TestCase):

    def setUp(self):
        self.qkd = QuantumKeyDistribution()

    def test_key_distribution(self):
        key1 = self.qkd.distribute_key()
        key2 = self.qkd.distribute_key()
        self.assertNotEqual(key1, key2)

    def test_key_security(self):
        key = self.qkd.distribute_key()
        self.assertTrue(self.qkd.is_secure(key))

if __name__ == '__main__':
    unittest.main()
