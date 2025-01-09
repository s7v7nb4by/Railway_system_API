import requests

# URLs for API endpoints
BASE_URL = "http://localhost:5000"
RESET_USERS_URL = f"{BASE_URL}/reset_users"
REGISTER_URL = f"{BASE_URL}/register"

# Function to reset users
def reset_users():
    try:
        response = requests.post(RESET_USERS_URL)
        response.raise_for_status()  # Raise an error for HTTP errors
        print("Users reset successfully:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Failed to reset users. Error: {e}")

# Function to register a new user
def register_user(email, password, name):
    user_data = {
        "email": email,
        "password": password,
        "name": name
    }
    try:
        response = requests.post(REGISTER_URL, json=user_data)
        response.raise_for_status()  # Raise an error for HTTP errors
        print("User registered successfully:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Failed to register user. Error: {e}")

# Main function to call the APIs
if __name__ == "__main__":
    # Reset users
    reset_users()

    # Register a new user
    register_user(
        email="prernapokharkar7@gmail.com",
        password="Prerna@2002",
        name="User"
    )
