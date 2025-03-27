import random

class BiometricAuth:
    def __init__(self):
        self.biometric_data = {}

    def enroll_user(self, user_id, biometric_info):
        """Enroll a user with their biometric information."""
        self.biometric_data[user_id] = biometric_info
        print(f"User {user_id} enrolled successfully.")

    def authenticate(self, user_id, biometric_info):
        """Authenticate a user using their biometric information."""
        if user_id not in self.biometric_data:
            raise ValueError("User not enrolled.")
        
        if self.biometric_data[user_id] == biometric_info:
            print(f"User {user_id} authenticated successfully.")
            return True
        else:
            print(f"Authentication failed for user {user_id}.")
            return False

    def simulate_biometric_scan(self, user_id):
        """Simulate a biometric scan for authentication."""
        if user_id not in self.biometric_data:
            raise ValueError("User not enrolled.")
        
        # Simulate a random biometric match (for demonstration purposes)
        return self.biometric_data[user_id] if random.choice([True, False]) else "invalid_data"
