from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime
from flask_mail import Mail
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/clean_blog'
db = SQLAlchemy(app)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'maulikmishra11@gmail.com',
    MAIL_PASSWORD = 'maulik123#'
)
mail = Mail(app)
class signup(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user = db.Column(db.String(255), nullable=False)
    passw= db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=True)
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        user = request.form.get('username')
        passw = request.form.get('password')
        database = signup.query.filter_by(passw=passw, user=user).first()
        if database:
            return redirect('/home')
    return render_template('Login.html')
@app.route('/existing')
def existing():
    return render_template('existing.html')

@app.route('/signup', methods=['GET', 'POST'])
def sign():
    if request.method=='POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        date = datetime.now()
        submit = signup(name=name, user=username, passw=password, date=date)
        database = signup.query.filter_by(user=username).first()
        databasepass = signup.query.filter_by(passw=password).first()
        if database:
            return redirect ('/existing')
        elif databasepass:
            return redirect('/existing')
        db.session.add(submit)
        db.session.commit()
    return render_template('signup.html')

app.run(debug=True)