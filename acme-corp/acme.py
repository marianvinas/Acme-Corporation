import random

class Product:
    def __init__(self, name, price, weight, flammability, identifier=[]):
        # these are attributes
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000, 9999999)

    def Stealability(self):
        stealability = self.price / self.weight
        if stealability  < 0.5:
            print("Not so stealable...")
        else: 
            stealability >= 0.5
            print("Kinda stealable.")
        return print("Very stealable!")

    def explode(self):
        explode = self.flammability * self.weight
        if explode < 10:
            print(f"...fizzle.")
        elif explode >= 50:
            print("...boom!")
        else:
            print("...it's a glove.")

if __name__ == "__main__":
    product1 = [
        {"name": "A Cool Toy", "price": "10", "weight": "20", "flammability": "0.5"},
    ]
    #print(product1.name)
    #print(product1.price)
    #print(product1.weight)
    #print(product1.flammability)
    #print(product1.identifier)
    for d in product1:
        product = Product(d["name"], d["price"], d["weight"], d["flammability"])
        print(product.name)
        product.Stealability()
        product.explode()