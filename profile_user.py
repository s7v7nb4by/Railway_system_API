import requests

# The URL of the login and profile endpoints in your app
login_url = 'http://localhost:5000/login'
profile_url = 'http://localhost:5000/profile'

# User credentials for login
data = {
    "email": "prernapokharkar7@gmail.com",
    "password": "Prerna@2002"
}

# First, log in to get the session cookie
login_response = requests.post(login_url, json=data)

# Check if login is successful
if login_response.status_code == 200:
    print(f"Login Response: {login_response.json()}")

    # Now, get the profile using the session from login
    profile_response = requests.get(profile_url, cookies=login_response.cookies)

    # Display profile response
    print(f"Profile Response Status Code: {profile_response.status_code}")
    print(f"Profile Response JSON: {profile_response.json()}")

else:
    print(f"Login failed: {login_response.json()}")
