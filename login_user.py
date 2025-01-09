import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, jsonify, session

app = Flask(__name__)

# Secret key to encode/decode JWT (use a more secure secret in production)
SECRET_KEY = 'my_random_secret_key_12345'  # You can replace this with a more secure key

# Sample user data
users = {
    "prernapokharkar7@gmail.com": {
        "password": generate_password_hash("Prerna@2002"),
        "name": "Prerna Pokharkar",
        "role": "user"
    }
}

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
        # Create token (JWT)
        token = jwt.encode({
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # token expiration time (1 hour)
        }, SECRET_KEY, algorithm='HS256')

        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401
