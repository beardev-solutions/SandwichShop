from flask import Flask
from datetime import datetime
import json
import os
import csv

print("Working directory: ", os.getcwd())

sandwich_dictionary = {}

app = Flask(__name__)

with app.app_context():
    PATH_TO_SANDWICHES = "sandwich_shop_menu_csv.csv"
    with open(PATH_TO_SANDWICHES, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter= ',')
            for row in reader:
                sandwich_dictionary[row[0]] = {'Name':row[1], 'Price':row[2]}

@app.route('/products/<int:id>')
def get_product(id):
    return sandwich_dictionary[str(id)]


@app.route('/products/price/<int:id>')
def get_product_price(id):
    print(sandwich_dictionary[str(id)]['Price'], flush=True)
    print(type(sandwich_dictionary[str(id)]['Price']), flush=True)   
    return sandwich_dictionary[str(id)]['Price']

#@app.route('/products/getAllProducts')
#def get_all_products():
     
@app.route('/products/getAllProducts')
def get_all_products():
    product_name_list = list()
    for key in sandwich_dictionary:
        product_name_list.append(sandwich_dictionary[key]['Name'])
    return product_name_list




