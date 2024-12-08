import numpy as np
from qiskit import QuantumCircuit, Aer, transpile, assemble, execute

class QuantumEncryption:
    def __init__(self):
        self.backend = Aer.get_backend('qasm_simulator')

    def encrypt(self, plaintext: str) -> str:
        """Encrypts the plaintext using quantum encryption."""
        # Convert plaintext to binary
        binary_data = ''.join(format(ord(char), '08b') for char in plaintext)
        encrypted_bits = []

        for bit in binary_data:
            # Create a quantum circuit with one qubit
            qc = QuantumCircuit(1, 1)
            if bit == '1':
                qc.x(0)  # Apply X gate for bit '1'
            qc.h(0)  # Apply Hadamard gate
            qc.measure(0, 0)  # Measure the qubit

            # Execute the circuit
            transpiled_qc = transpile(qc, self.backend)
            qobj = assemble(transpiled_qc)
            result = execute(qc, self.backend).result()
            encrypted_bit = result.get_counts(qc)
            encrypted_bits.append(list(encrypted_bit.keys())[0])

        return ''.join(encrypted_bits)

    def decrypt(self, encrypted_bits: str) -> str:
        """Decrypts the encrypted bits back to plaintext."""
        decrypted_bits = []

        for bit in encrypted_bits:
            # Create a quantum circuit with one qubit
            qc = QuantumCircuit(1, 1)
            if bit == '1':
                qc.x(0)  # Apply X gate for bit '1'
            qc.h(0)  # Apply Hadamard gate
            qc.measure(0, 0)  # Measure the qubit

            # Execute the circuit
            transpiled_qc = transpile(qc, self.backend)
            qobj = assemble(transpiled_qc)
            result = execute(qc, self.backend).result()
            decrypted_bit = result.get_counts(qc)
            decrypted_bits.append(list(decrypted_bit.keys())[0])

        # Convert binary to string
        decrypted_string = ''.join(chr(int(decrypted_bits[i:i + 8], 2)) for i in range(0, len(decrypted_bits), 8))
        return decrypted_string

# Example usage
if __name__ == "__main__":
    quantum_encryption = QuantumEncryption()
    plaintext = "Hello, Quantum World!"
    encrypted = quantum_encryption.encrypt(plaintext)
    print(f"Encrypted: {encrypted}")
    decrypted = quantum_encryption.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
