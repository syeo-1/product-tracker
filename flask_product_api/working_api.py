from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

from config import DB_PASSWORD

db_string = f'postgresql://localhost/products?user=postgres&password={DB_PASSWORD}'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_string
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class ProductPrice(db.Model):

    __tablename__ = 'costco_products_prices_dev'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    insert_time = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

class Product(db.Model):

    __tablename__ = 'costco_products_dev'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String, nullable=False, unique=True)
    product_url = db.Column(db.String, nullable=False)

class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "product_name", "product_url")


class ProductPriceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'product_id', 'insert_time', 'price')


products_schema = ProductSchema(many=True)
product_schema = ProductSchema()
product_price_schema = ProductPriceSchema(many=True)


class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return products_schema.dump(products)

class ProductResource(Resource):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return product_schema.dump(product)

class ProductPriceResource(Resource):
    def get(self, product_id):
        product_prices = ProductPrice.query.filter_by(product_id=product_id)
        return product_price_schema.dump(product_prices)

# return a list of json for data of all the products available
api.add_resource(ProductListResource, '/products')

# return details for a specific product based on the id given
api.add_resource(ProductResource, '/products/<int:product_id>')

# return list of price data for a specific product
api.add_resource(ProductPriceResource, '/productPrices/<int:product_id>')

# example usage: 
# http://127.0.0.1:5000/productPrices/2
# http://127.0.0.1:5000/products
# http://127.0.0.1:5000/products/25


if __name__ == '__main__':
    app.run(debug=True)