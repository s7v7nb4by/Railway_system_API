from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import random
import jwt
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample user data
users = {
    "prernapokharkar7@gmail.com": {
        "password": generate_password_hash("Prerna@2002"),
        "name": "Prerna Pokharkar",
        "role": "user"
    }
}

# Sample trains data
trains = [
    {"train_id": "T1001", "source": "Delhi", "destination": "Mumbai", "total_seats": 100, "available_seats": 50},
    {"train_id": "T1002", "source": "Delhi", "destination": "Bangalore", "total_seats": 150, "available_seats": 30},
    {"train_id": "T1003", "source": "Mumbai", "destination": "Delhi", "total_seats": 200, "available_seats": 80},
    {"train_id": "T1004", "source": "Bangalore", "destination": "Mumbai", "total_seats": 120, "available_seats": 60},
]

# Sample bookings data
bookings = {}

# JWT Secret Key
SECRET_KEY = 'hello123'

# Token required decorator for authentication
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            token = token.split(" ")[1]  # Extract token from 'Bearer' prefix
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403

        return f(*args, **kwargs)
    return decorator

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data provided"}), 400

    email = data.get("email")
    password = data.get("password")
    name = data.get("name")

    if not email or not password or not name:
        return jsonify({"message": "Email, password, and name are required"}), 400

    if email in users:
        return jsonify({"message": "User already exists"}), 400

    users[email] = {
        "password": generate_password_hash(password),
        "name": name,
        "role": "user"
    }

    return jsonify({"message": "User registered successfully"}), 201

# Endpoint to reset users
@app.route('/reset_users', methods=['POST'])
def reset_users():
    global users
    users = {
        "prernapokharkar7@gmail.com": {
            "password": generate_password_hash("Prerna@2002"),
            "name": "Prerna Pokharkar",
            "role": "user"
        }
    }
    return jsonify({"message": "Users reset successfully"}), 200

# Endpoint to login a user
@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    user = users.get(email)
    if user and check_password_hash(user['password'], password):
        token = jwt.encode({
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm='HS256')

        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401

# Endpoint to check train availability
@app.route('/check_availability', methods=['GET'])
def check_availability():
    source = request.args.get('source')
    destination = request.args.get('destination')

    if not source or not destination:
        return jsonify({"message": "Source and destination are required"}), 400

    available_trains = [train for train in trains if train['source'] == source and train['destination'] == destination]

    if available_trains:
        return jsonify({"trains": available_trains}), 200
    else:
        return jsonify({"message": "No trains available for the specified route"}), 404

# Endpoint to book a ticket
@app.route('/book_seat', methods=['POST'])
def book_ticket():
    data = request.get_json()
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"message": "Token is required to book a seat"}), 401

    try:
        token = token.split(" ")[1]
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        email = decoded_token['email']
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired!"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token!"}), 403

    user = users.get(email)

    if not user:
        return jsonify({"message": "User not found"}), 404

    train_id = data.get('train_id')
    seat_class = data.get('seat_class')
    date_of_travel = data.get('date_of_travel')

    if not all([train_id, seat_class, date_of_travel]):
        return jsonify({'message': 'All fields are required'}), 400

    train = next((train for train in trains if train['train_id'] == train_id), None)

    if not train:
        return jsonify({'message': 'Train not found'}), 404

    if train['available_seats'] > 0:
        train['available_seats'] -= 1
        booking_id = f'B{random.randint(1000, 9999)}'
        booking = {
            'booking_id': booking_id,
            'user_id': email,
            'train_id': train_id,
            'seat_class': seat_class,
            'date_of_travel': date_of_travel,
        }

        bookings[booking_id] = booking
        return jsonify({'message': 'Ticket booked successfully', 'booking': booking}), 201
    else:
        return jsonify({'message': 'No seats available'}), 400

# Endpoint to fetch booking details
@app.route('/booking_details/<booking_id>', methods=['GET'])
@token_required
def get_booking_details(booking_id):
    booking = bookings.get(booking_id)

    if not booking:
        return jsonify({"message": "Booking not found"}), 404

    return jsonify({"booking": booking}), 200

if __name__ == '__main__':
    app.run(debug=True)
