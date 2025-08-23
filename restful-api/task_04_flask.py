#!/usr/bin/python3


from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    content = request.get_json(silent=True) or {}
    username = content.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = {
        "username": username,
        "name": content.get("name"),
        "age": content.get("age"),
        "city": content.get("city"),
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run()
