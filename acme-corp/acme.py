import random

class Product:
    def __init__(self, name, price, weight, flammability, identifier=[]):
        # these are attributes
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000, 9999999)

if __name__ == "__main__":
    product1 = Product(name="A Cool Toy", price=10, weight=20, flammability=0.5)
    print(product1.name)
    print(product1.price)
    print(product1.weight)
    print(product1.flammability)
    print(product1.identifier)