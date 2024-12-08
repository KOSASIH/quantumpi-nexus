import unittest
from user_authentication import UserAuthentication

class TestUser Authentication(unittest.TestCase):
    def setUp(self):
        self.auth = UserAuthentication()
        self.auth.register("testuser", "securepassword")

    def test_login_success(self):
        self.assertTrue(self.auth.login("testuser", "securepassword"))

    def test_login_failure(self):
        self.assertFalse(self.auth.login("testuser", "wrongpassword"))

    def test_registration_existing_user(self):
        response = self.auth.register("testuser", "newpassword")
        self.assertEqual(response, "User  already exists.")

if __name__ == "__main__":
    unittest.main()
