from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from config import DB_PASSWORD
from models import ProductPrice, Product, base
from generate_mock_data import generate_mock_data

import datetime

db_string = f'postgresql://localhost/products?user=postgres&password={DB_PASSWORD}'

db = create_engine(db_string)

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)

def insert_mock_data():
    # generate the mock data
    mock_data = list()

    for _ in range(1):
        mock_data.append(generate_mock_data())

    cur_utc_time = datetime.datetime.utcnow().isoformat()
    # print(mock_data)
    # exit()

    # transform the data as necessary to insert into the database
    for data in mock_data:
        for product_name, product_details in data.items():

            product_id = session.query(Product.id).filter(Product.product_name==product_name).scalar()

            if product_id == None:
                print(f"product does not exist yet. Adding in a product: {product_name} and a price: {product_details['price']}")
                new_product = Product(product_name=product_name, product_url=product_details['url'])
                new_product_price = ProductPrice(insert_time=cur_utc_time, price=product_details['price'])

                new_product.prices.append(new_product_price)
                session.add(new_product)
                session.add(new_product_price)
            else:
                print(f"product already exists. Adding in a new price value: {product_details['price']} for product {product_name}!")
                new_product_price = ProductPrice(insert_time=cur_utc_time, price=product_details['price'], product_id=product_id)
                session.add(new_product_price)
            # insert product data into db

            # TODO: have to do a check to insert only if the product doesn't already exist
            # otherwise, must use the existing product with its id for the foreign key!
            # print(product_exists)
            # print(product_name, product_details)

    # commit changes to the database
    # session.commit()

insert_mock_data()
session.commit()