import unittest
import random
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product(name='Test Product', price=100, weight=100, flammability=100)
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        prod = Product(name='Test Product', price=100, weight=100, flammability=100)
        self.assertEqual(prod.weight, 20)

    def test_stealyboom(self):
        prod = Product(name='Test Product', price=100, weight=100, flammability=100)
        self.assertEqual(prod.Stealability(), "Very stealable!")
        self.assertEqual(prod.explode(), "...BABOOM!!")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        case = generate_products()
        self.assertEqual(len(case), 30)

    def test_legal_names(self):
        case = generate_products()
        for product in case:
            adjective, noun = product.name.split()
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()