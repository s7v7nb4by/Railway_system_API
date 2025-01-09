# Railway_system_API

Railway Management System API
This is a simple Railway Management System API built using Flask. It allows users to register, login, check train availability, and book train tickets. The API also provides functionalities to view booking details using JWT-based authentication.

Features
User Registration - Users can register with an email, name, and password.
User Login - Users can log in using their email and password, receiving a JWT token for authentication.
Train Availability - Users can check available trains between a source and destination.
Book Tickets - Users can book a ticket, choosing the train and class, after successful login.
Booking Details - Users can view their booking details with the provided booking ID.
Requirements
Python 3.x
Flask
Flask-Session
Flask-Werkzeug
PyJWT
Requests (for testing)
Setup and Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/s7v7nb4by/RailwayManagementSystem.git
Navigate to the project directory:


cd RailwayManagementSystem
Create a Virtual Environment:

If you haven't already created a virtual environment, you can do so with:

python -m venv venv
Activate the Virtual Environment:

On Windows:

venv\Scripts\activate
On macOS/Linux:

source venv/bin/activate
Install Required Packages:

pip install -r requirements.txt
If you don't have requirements.txt, install the necessary packages manually:

pip install flask werkzeug pyjwt requests
Running the Application

Start the Flask server:

python app.py
By default, the application will be running at http://127.0.0.1:5000/.

Access the API: Use a tool like Postman or curl to send requests to the API.

Endpoints
1. Register User
POST /register

Request body:


{
  "email": "newuser@example.com",
  "password": "NewUser@123",
  "name": "New User"
}

Response:

Success: 201 Created
Failure: 400 Bad Request (if validation fails)

2. Login User
POST /login

Request body:

{
  "email": "newuser@example.com",
  "password": "NewUser@123"
}
Response:

Success: 200 OK with JWT token
Failure: 401 Unauthorized (invalid email/password)

3. Check Train Availability
GET /check_availability?source=<source>&destination=<destination>

Response:

Success: 200 OK with train details
Failure: 404 Not Found (if no trains available)

4. Book Ticket
POST /book_seat

Request body:

{
  "token": "JWT_TOKEN",
  "train_id": "T1001",
  "seat_class": "First Class",
  "date_of_travel": "2025-01-15"
}
Response:

Success: 201 Created with booking details
Failure: 400 Bad Request (if validation fails)


5. View Booking Details
GET /booking_details/<booking_id>

Response:

Success: 200 OK with booking details
Failure: 404 Not Found (if booking not found)
Running Tests (Optional)
If you'd like to test the API using requests module, follow the steps below:

Install requests:


pip install requests
Use the provided test scripts to test the registration and login functionality.

For example, in register_test.py:

import requests

url = 'http://localhost:5000/register'
data = {
    "email": "newuser@example.com",
    "password": "NewUser@123",
    "name": "New User"
}

response = requests.post(url, json=data)
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")
To test login, you can follow a similar approach with the /login endpoint.

Assumptions
Authentication: JWT tokens are used for authentication, and they expire after one hour.
Database: For simplicity, the user and train data are stored in memory (not persistent).
No rate-limiting or input validation: This project is a basic demonstration of the Railway Management System API and doesn't implement advanced security, rate-limiting, or in-depth input validation.
