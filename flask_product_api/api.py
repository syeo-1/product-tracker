import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Resource, Api
from models import Product

load_dotenv()

app = Flask(__name__)
api = Api(app)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

# what endpoints should i have?

# one for a specific product
class ProductList(Resource):
    def get(self):
        # get the product and its details in json format based on the id passed in!
        return 

# one for all product names
# one for all products under a brand or store (eventually)
# one for all prices for a specific product