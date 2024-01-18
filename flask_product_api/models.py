from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_PASSWORD

db_string = f'postgresql://localhost/products?user=postgres&password={DB_PASSWORD}'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_string
db = SQLAlchemy(app)

class ProductPrice(db.Model):  

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    insert_time = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String, nullable=False, unique=True)
    product_url = db.Column(db.String, nullable=False)

if __name__ == '__main__':
    app.run(debug=True)