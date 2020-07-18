# !/usr/bin/env python
from random import randint, sample, uniform
from acme import Product

class Product:
    def __init__(self, name, price, weight, flammability, identifier=[]):
        # these are attributes
        self.name = name
        self.price = 10
        self.weight = 10
        self.flammability = 0.5
        self.identifier = random.randint(1000000, 9999999)
​
# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
​
​
def generate_products(num_products=30):
  products = [random.randint]
  # TODO - your code! Generate and add random products.
  return products
​
​
def inventory_report(products):
  pass  # TODO - your code! Loop over the products to calculate the report.
​
​
if __name__ == '__main__':
  inventory_report(generate_products())