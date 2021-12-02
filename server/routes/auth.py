from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from db.database import storage_db
 
auth = Blueprint("auth", __name__)

@auth.route("/users")
def get_users():
    return jsonify(storage_db.get_users())

@auth.route("/rooms")
def get_rooms():
    return jsonify(storage_db.get_rooms())

@auth.route("/register", methods=["POST"])
def create_user():
    user = request.form['user']
    email = request.form['email']
    password = request.form['password']
    password = generate_password_hash(password)
    return jsonify(storage_db.create_user(email, user, password))

@auth.route("/login", methods=["POST"])
def login():
    user = request.form['user']
    password = request.form['password']
    return jsonify(storage_db.authenticate(user, password))

@auth.route("/save_balance", methods=["POST"])
def save_balance():
    user = request.form['user']
    balance = request.form['balance']
    return jsonify(storage_db.update_balance(user, balance))

@auth.route("/create_room", methods=["POST"])
def create_room():
    user = request.form['user']
    return jsonify(storage_db.create_room(user))

@auth.route("/join_room", methods=["POST"])
def join_room():
    room_id = request.form['id']
    user = request.form['user']
    return jsonify(storage_db.join_room(room_id, user))
