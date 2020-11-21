from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import os
import math
from werkzeug.utils import secure_filename
from datetime import datetime

with open('config.json', 'r') as c:
    params = json.load(c)["params"]
local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)

class contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    information = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=True)

@app.route('/', methods=['GET', 'POST'])
def contacts():
    if (request.method=='POST'):
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        email = request.form.get('email')
        phone = request.form.get('phone')
        information = request.form.get('desc')
        posts = contact(name=name, age=age, gender=gender, email=email, phone=phone, information=information, date=datetime.now())
        db.session.add(posts)
        db.session.commit()
    return render_template('index.html')

@app.route('/dash')
def dash():
    return render_template('dashboard.html')
app.run(debug=True)