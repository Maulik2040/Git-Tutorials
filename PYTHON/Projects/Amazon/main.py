from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/Amazon'
db = SQLAlchemy(app)
class Products(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    product_id = db.Column(db.String(255), nullable=False)
    product_description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=False)
    img_file = db.Column(db.String(255), nullable=False)

class addtocart(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    product_id = db.Column(db.String(255), nullable=False)
    product_description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=False)
    image= db.Column(db.String(255), nullable=False)

@app.route('/')
def home():
    product = Products.query.all()
    image = 'https://images-na.ssl-images-amazon.com/images/I/81jNGP%2B6tYL._SL1500_.jpg'
    return render_template('index.html', product=product, image=image)

@app.route('/product/<string:product_id>', methods=['GET', 'POST'])
def order(product_id):
    product = Products.query.filter_by(product_id=product_id).first()
    if request.method=='POST':
        Addtocartname = product.product_name
        Addtocartid = product.product_id
        Addtocartdescription = product.product_description
        Addtocartprice = product.price
        date = datetime.now()
        image = product.img_file
        addedtocart = addtocart(product_name=Addtocartname, product_id=Addtocartid, product_description=Addtocartdescription, price=Addtocartprice, date=date, image=image)
        db.session.add(addedtocart)
        db.session.commit()
    return render_template('product.html', product=product)

@app.route('/yourCart')
def your_Cart():
    product = addtocart.query.all()
    return render_template('cart.html', product=product)

app.run(debug=True)