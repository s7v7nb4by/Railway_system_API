import requests

# URL for checking availability
availability_url = 'http://localhost:5000/check_availability'

# Test data for source and destination
params = {
    'source': 'Delhi',
    'destination': 'Mumbai'
}

# Sending GET request to check availability
response = requests.get(availability_url, params=params)

# Displaying the response status code and JSON response
print(f"Response Status Code: {response.status_code}")
print(f"Response JSON: {response.json()}")
