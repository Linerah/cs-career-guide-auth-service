from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
import uuid


class User:

    def start_session(self, user):
        del user['password']
        return jsonify(user), 200

    def signup(self, name, email, password, isProfessor, db):
        print(request.form)

        # Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": name,
            "email": email,
            "password": password,
            "isProfessor": isProfessor
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Check for existing email address
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email address already in use"}), 400

        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    def login(self, email, password, db):

        user = db.users.find_one({
            "email": email
        })

        if user and pbkdf2_sha256.verify(password, user['password']):
            return self.start_session(user)

        return jsonify({"error": "Invalid login credentials"}), 401
