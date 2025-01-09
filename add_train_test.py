import requests

# Replace with your actual API URL
url = 'http://localhost:5000/add_train'

# Admin API Key for Authorization
headers = {'Authorization': 'Bearer your_admin_api_key'}

# Train data to add
train_data = {
    'train_id': 'T1005',
    'source': 'Delhi',
    'destination': 'Kolkata',
    'total_seats': 150
}

# Sending POST request to add train
response = requests.post(url, json=train_data, headers=headers)

# Output response details
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")
