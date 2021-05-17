import unittest
from classes.bars import Bar
from classes.drinks import Drink

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("Main Bar")

    def test_bar_has_name(self):
        self.assertEqual("Main Bar", self.bar.name)

    def test_bar_has_empty_list_of_drinks(self):
        self.assertEqual(0, len(self.bar.stock))

    def test_bar_can_add_drinks_to_stock(self):
        self.drink = Drink("Peroni", 5)
        self.bar.add_drink_to_stock(self.drink, 50)
        self.assertEqual(50, self.bar.stock[self.drink])

    def test_bar_can_add_existing_drinks(self):
        self.drink = Drink("Peroni", 5)
        self.bar.add_drink_to_stock(self.drink, 50)
        self.bar.add_drink_to_stock(self.drink, 50)
        self.assertEqual(100, self.bar.stock[self.drink])
