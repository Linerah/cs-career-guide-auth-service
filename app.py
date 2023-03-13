# import os
from flask import Flask, request
import pymongo
from user import models

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

app.config['MONGO_DBNAME'] = 'user_auth'

client = pymongo.MongoClient(
    "mongodb+srv://admin:NtXLrfmOBLhl00bm@capstoneauth.25mmcqj.mongodb.net/?retryWrites=true&w=majority", tls=True,
    tlsAllowInvalidCertificates=True)
db = client['user-auth']


@app.route('/auth/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        user = models.User()
        password = request.json['password']
        email = request.json['email']
        return user.login(email, password)
    if request.method == 'POST':
        user = models.User()
        name = request.json['name']
        password = request.json['password']
        email = request.json['email']
        return user.signup(name, email, password)
