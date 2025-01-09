import requests
import json

# Base URL for the Flask application
base_url = 'http://127.0.0.1:5000'

# Test data for login
login_data = {
    "email": "prernapokharkar7@gmail.com",
    "password": "Prerna@2002"
}

# Login to obtain the session cookie
login_response = requests.post(f'{base_url}/login', json=login_data)

if login_response.status_code == 200:
    print("Login successful")

    # Extract session cookie
    session_cookie = login_response.cookies

    # Data for booking a ticket
    booking_data = {
        "train_id": "T1001",  # Choose a train_id
        "seat_class": "First Class",  # Seat class
        "date_of_travel": "2025-01-15"  # Date of travel
    }

    # Book the ticket by sending the session cookie along with the data
    booking_response = requests.post(f'{base_url}/book_seat', json=booking_data, cookies=session_cookie)

    # Check the status of the booking response
    print(f"Booking Status Code: {booking_response.status_code}")
    print(f"Response Text: {booking_response.text}")

else:
    print(f"Login failed, status code: {login_response.status_code}")
    print(f"Response Text: {login_response.text}")
