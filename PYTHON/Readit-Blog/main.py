from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/readit_blog'
with open('config.json', 'r') as c:
    params = json.load(c)["params"]
db = SQLAlchemy(app)

class contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    reason = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=True)

class Post(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=True)    


@app.route('/')
def home():
    return render_template('index.html', params=params)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contacts():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('Phone-no')
        reason = request.form.get('reason')
        date = datetime.now()
        submit = contact(name=name, email=email, phone=phone, reason=reason, date=date)
        db.session.add(submit)
        db.session.commit()
    return render_template('contact.html')

@app.route('/post', methods=['GET', 'POST'])
def posts():
    if request.method=='POST':
        name = request.form.get('name')
        title = request.form.get('title')
        slug = request.form.get('slug')
        img_file = request.form.get('img_file')
        content = request.form.get('content')
        date = datetime.now()
        posted = Post(name=name, title=title, slug=slug, content=content, date=date)
        db.session.add(posted)
        db.session.commit()
    return render_template('post.html')

@app.route('/dashboard')
def dashboard():
    posts = Post.query.all()
    return render_template('dashboard.html', post=posts)

@app.route("/post/<string:post_slug>", methods=['GET'])
def otherspost(post_slug):
    otherposts = Post.query.filter_by(slug=post_slug).first()
    return render_template('others_post.html', post=otherposts)

@app.route('/admin-dashboard/')
def admin():
    posts = Post.query.all()
    return render_template('admin_dashboard.html', post=posts)

@app.route('/edit/<string:sno>', methods=['GET', 'POST'])
def edit(sno):
    if request.method=='POST':
        name = request.form.get('name')
        title = request.form.get('title')
        slug = request.form.get('slug')
        content = request.form.get('content')
        date = datetime.now()

        if sno=='0':
            posted_by = Post(name=name, title=title, slug=slug, content=content, date=date)
            db.session.add(posted_by)
            db.session.commit()
        
        else:
            posts = Post.query.filter_by(sno=sno).first()
            posts.name = name
            posts.title = title
            posts.slug = slug
            posts.content = content
            posts.date = datetime.now()
            db.session.commit()
    post_editelement = Post.query.filter_by(sno=sno).first()
    return render_template('edit.html', post=post_editelement, sno=sno)

@app.route('/delete/<string:sno>', methods=['GET', 'POST'])
def delete(sno):
    post = Post.query.filter_by(sno=sno).first()
    db.session.delete(post)
    db.session.commit()
    return redirect('/admin-dashboard/')

@app.route('/admin-login/', methods=['GET', 'POST'])
def admin_login():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if (username==params['admin-username'] and password==params['admin-password']):
            return redirect('/admin-dashboard/')
    return render_template('admin_login.html')

app.run(debug=True)