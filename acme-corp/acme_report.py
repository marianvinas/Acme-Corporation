# !/usr/bin/env python

from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        adjective = sample(ADJECTIVES, 1)[0]
        noun = sample(NOUNS, 1)[0]
        name = adjective + ' ' + noun
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        prod = Product(name, price, weight, flammability)
        products.append(prod)
    return products

    def generate_products(num_products=30):
        products = []
        for i in range(num_products):
            adjective = sample(ADJECTIVES, 1)[0]
            noun = sample(NOUNS, 1)[0]
            name = adjective + ' ' + noun
            price = randint(5, 100)
            weight = randint(5, 100)
            flammability = uniform(0, 2.5)
            prod = Product(name, price, weight, flammability)
            products.append(prod)
        return products


def inventory_report(products):
    name_list = []
    weight_list = []
    price_list = []
    flammability_list = []
    for product in products:
        name_list.append(product.name)
        weight_list.append(product.weight)
        price_list.append(product.price)
        flammability_list.append(product.flammability)
    uniques = name_list
    mean_weight = sum(weight_list) / len(weight_list)
    mean_price = sum(price_list) / len(price_list)
    mean_flammability = sum(flammability_list) / len(flammability_list)
    print("Unique product names: {}".format(len(uniques)))
    # print("ACME INVENTORY REPORT Unique Products = {uniques}"),
    print("Average price: {}".format((mean_price)))
    print("Average Weight: {}".format((mean_weight)))
    print("Average Flammability: {}".format((mean_flammability)))

    # print("Unique product names: {}".format(len(uniques)))

if __name__ == '__main__':
    inventory_report(generate_products())