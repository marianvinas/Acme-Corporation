import random


class Product:
    def __init__(self, name, price, weight, flammability, identifier=[]):
        # these are attributes
        self.name = name
        self.price = 10
        self.weight = 10
        self.flammability = 0.5
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        stealability = self.price / self.weight
        if stealability < 0.5:
            return "Not so stealable..."
        else:
            stealability >= 0.5
            return "Kinda stealable."
        return "Very stealable!"

    def explode(self):
        explode = self.flammability * self.weight
        if explode < 10:
            return "...it's a glove."
        elif explode >= 50:
            return "...boom!"
        else:
            return "...it's a glove."


class BoxingGlove(Product):
    def __init__(self, name, price, weight, glove, flammability=[],
                 identifier=[]):
        super().__init__(self, name, price, weight, flammability=[],
                         identifier=[])
        self.glove = glove

    def punch(self):
        punch = self.weight
        if punch < 5:
            return "That tickles."
        elif punch >= 5:
            return "Hey that hurt!"
        else:
            return "OUCH!"

if __name__ == "__main__":
    product1 = [
        {"name": "A Cool Toy", "price": "10", "weight": "20",
         "flammability": "0.5", "glove": "10"},
    ]

    for d in product1:
        product = Product(d["name"], d["price"], d["weight"],
                          d["flammability"])
        # print(product.name)
        # product.Stealability()
        # product.explode()

    for d in product1:
        glove = Product(d["name"], d["price"], d["weight"],
                        d["flammability"], d["glove"])
        print(glove.name)
        print(glove.price)
        print(glove.weight)
        # glove.punch()
        glove.explode()
