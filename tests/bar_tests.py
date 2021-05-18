import unittest
from classes.bars import Bar
from classes.drinks import Drink
from classes.guests import Guest
from classes.rooms import Room

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

    def test_bar_has_empty_tab(self):
        self.assertEqual(0, len(self.bar.tab))

    def test_customer_can_order_a_drink_and_add_to_bar_tab(self):
        self.guest = Guest("Ben", 50, "Purple Rain")
        self.drink = Drink("Peroni", 5)
        self.newRoom = Room("DrinkRoom", 10, 10)
        self.bar.add_drink_to_stock(self.drink, 50)
        self.bar.order_drink(self.drink)
        self.assertEqual(1, self.bar.tab[self.drink])
        self.assertEqual(50, self.guest.wallet)
        self.assertEqual(0, self.newRoom.total_cash)

    def test_customer_add_two_drinks_to_tab(self):
        self.guest = Guest("Ben", 50, "Purple Rain")
        self.drink = Drink("Peroni", 5)
        self.newRoom = Room("DrinkRoom", 10, 10)
        self.bar.add_drink_to_stock(self.drink, 50)
        self.bar.order_drink(self.drink)
        self.bar.order_drink(self.drink)
        self.assertEqual(2, self.bar.tab[self.drink])

    def test_add_two_different_drinks_to_tab(self):
        self.guest = Guest("Ben", 50, "Purple Rain")
        self.drink = Drink("Peroni", 5)
        self.drink2 = Drink("Cobra", 4)
        self.newRoom = Room("DrinkRoom", 10, 10)
        self.bar.add_drink_to_stock(self.drink, 50)
        self.bar.add_drink_to_stock(self.drink2, 50)
        self.bar.order_drink(self.drink)
        self.bar.order_drink(self.drink2)
        self.assertEqual(1, self.bar.tab[self.drink])
        self.assertEqual(1, self.bar.tab[self.drink2])

    def test_room_can_start_a_tab(self):
        self.newRoom = Room("New Room", 10, 5)
        self.bar.start_tab(self.newRoom)
        self.assertEqual(False, bool(self.bar.tab_list[self.newRoom.name]))
        
