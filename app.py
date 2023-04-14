# import os
from flask import Flask, request
import pymongo
from user import models
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

app.config['MONGO_DBNAME'] = 'user_auth'

client = pymongo.MongoClient(
    "mongodb+srv://admin:NtXLrfmOBLhl00bm@capstoneauth.25mmcqj.mongodb.net/?retryWrites=true&w=majority", tls=True,
    tlsAllowInvalidCertificates=True)
db = client['user-auth']


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        user = models.User()
        print('hi')
        password = request.args.get('password')
        email = request.args.get('email')
        print("password: ", password)
        print("email: ", email)
        return user.login(email, password, db)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user = models.User()
        name = request.json['name']
        password = request.json['password']
        email = request.json['email']
        print(request.json)
        return user.signup(name, email, password, db)
