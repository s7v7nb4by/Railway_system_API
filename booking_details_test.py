import requests

# Use the same token obtained from login
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InByZXJuYXBva2hhcmthcjdAZ21haWwuY29tIiwiZXhwIjoxNzM2NDEzNDAzfQ.lyaNPbwKmKFsBBmIzzqqsNTdhUMFTyW7PgPvcCTtBWY'

# Example booking ID (replace with the actual ID from the booking response)
booking_id = 'B1469'

# Endpoint to get booking details
url = f'http://localhost:5000/booking_details/{booking_id}'
headers = {'Authorization': f'Bearer {token}'}

# Make the request
response = requests.get(url, headers=headers)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")
