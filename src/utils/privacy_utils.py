import hashlib
import os
import base64
from cryptography.fernet import Fernet
import secrets

class PrivacyUtils:
    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def generate_key() -> bytes:
        """Generates a secure random key for encryption."""
        return Fernet.generate_key()

    @staticmethod
    def encrypt_data(data: str, key: bytes) -> bytes:
        """Encrypts data using the provided key."""
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data

    @staticmethod
    def decrypt_data(encrypted_data: bytes, key: bytes) -> str:
        """Decrypts data using the provided key."""
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return decrypted_data

    @staticmethod
    def generate_secure_token(length: int = 32) -> str:
        """Generates a secure random token."""
        return base64.urlsafe_b64encode(secrets.token_bytes(length)).decode()

    @staticmethod
    def is_password_strong(password: str) -> bool:
        """Checks if the password is strong based on certain criteria."""
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
            return False
        return True

# Usage examples
if __name__ == "__main__":
    # Hashing a password
    password = "SecureP@ssw0rd"
    hashed_password = PrivacyUtils.hash_password(password)
    print(f"Hashed Password: {hashed_password}")

    # Generating a key
    key = PrivacyUtils.generate_key()
    print(f"Generated Key: {key}")

    # Encrypting data
    data = "Sensitive Data"
    encrypted = PrivacyUtils.encrypt_data(data, key)
    print(f"Encrypted Data: {encrypted}")

    # Decrypting data
    decrypted = PrivacyUtils.decrypt_data(encrypted, key)
    print(f"Decrypted Data: {decrypted}")

    # Generating a secure token
    token = PrivacyUtils.generate_secure_token()
    print(f"Secure Token: {token}")

    # Checking password strength
    is_strong = PrivacyUtils.is_password_strong(password)
    print(f"Is the password strong? {is_strong}")
