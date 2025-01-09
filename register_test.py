import unittest
import requests

BASE_URL = "http://localhost:5000"
RESET_USERS_URL = f"{BASE_URL}/reset_users"
REGISTER_URL = f"{BASE_URL}/register"

class TestUserAPI(unittest.TestCase):
    def test_reset_users(self):
        """Test the reset_users endpoint."""
        response = requests.post(RESET_USERS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Users reset successfully")

    def test_register_user(self):
        """Test the register endpoint."""
        user_data = {
            "email": "prernapokharkar7@gmail.com",
            "password": "Prerna@2002",
            "name": "User"
        }
        response = requests.post(REGISTER_URL, json=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "User registered successfully")

if __name__ == "__main__":
    unittest.main()
