import unittest
from src.main.quantum_security.quantum_authentication import QuantumAuthentication

class TestQuantumAuthentication(unittest.TestCase):

    def setUp(self):
        self.qa = QuantumAuthentication()

    def test_authentication_success(self):
        user_id = "user123"
        token = self.qa.generate_token(user_id)
        self.assertTrue(self.qa.authenticate(user_id, token))

    def test_authentication_failure(self):
        user_id = "user123"
        invalid_token = "invalid_token"
        self.assertFalse(self.qa.authenticate(user_id, invalid_token))

if __name__ == '__main__':
    unittest.main()
