import unittest
from src.main.quantum_security.quantum_encryption import QuantumEncryption

class TestQuantumEncryption(unittest.TestCase):

    def setUp(self):
        self.qe = QuantumEncryption()

    def test_encryption(self):
        plaintext = "Hello, Quantum World!"
        ciphertext = self.qe.encrypt(plaintext)
        self.assertIsNotNone(ciphertext)
        self.assertNotEqual(plaintext, ciphertext)

    def test_decryption(self):
        plaintext = "Hello, Quantum World!"
        ciphertext = self.qe.encrypt(plaintext)
        decrypted_text = self.qe.decrypt(ciphertext)
        self.assertEqual(plaintext, decrypted_text)

if __name__ == '__main__':
    unittest.main()
