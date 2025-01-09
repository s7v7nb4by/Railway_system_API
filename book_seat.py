import requests

# Login to get the token
login_data = {
    'email': 'prernapokharkar7@gmail.com',
    'password': 'Prerna@2002'
}

login_url = 'http://localhost:5000/login'
login_response = requests.post(login_url, json=login_data)

print(f"Login Status Code: {login_response.status_code}")
login_json = login_response.json()
print(f"Login Response JSON: {login_json}")

# Store the token from the response
token = login_json.get('token')
if token:
    print(f"Token: {token}")

    # Now use this token for the booking request
    booking_data = {
        'token': token,  # Use the stored token here
        'train_id': 'T1001',
        'seat_class': 'First Class',
        'date_of_travel': '2025-01-15'
    }

    booking_url = 'http://localhost:5000/book_seat'
    booking_response = requests.post(booking_url, json=booking_data)
    print(f"Booking Status Code: {booking_response.status_code}")
    print(f"Booking Response: {booking_response.json()}")
else:
    print("Failed to obtain token")
