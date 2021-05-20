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

    def test_bar_starts_with_empty_stock(self):
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
        self.newRoom = Room("New Room", 5, 5)
        self.bar.start_tab(self.newRoom)
        self.assertEqual(False, bool(self.bar.tab_list[self.newRoom.name]))

    def test_customer_can_order_a_drink_and_add_to_bar_tab(self):
        self.guest = Guest("Ben", 50, "Purple Rain")
        self.drink = Drink("Peroni", 5)
        self.newRoom = Room("DrinkRoom", 10, 10)
        self.bar.add_drink_to_stock(self.drink, 50)
        self.bar.start_tab(self.newRoom)
        self.bar.order_drink(self.drink, self.newRoom)
        self.assertEqual(1, self.bar.tab_list[self.newRoom.name][self.drink])
        self.assertEqual(50, self.guest.wallet)
        self.assertEqual(0, self.newRoom.total_cash)

    def test_customer_add_two_drinks_to_tab(self):
        self.guest = Guest("Ben", 50, "Purple Rain")
        self.drink = Drink("Peroni", 5)
        self.newRoom = Room("DrinkRoom", 10, 10)
        self.bar.add_drink_to_stock(self.drink, 50)
        self.bar.start_tab(self.newRoom)
        self.bar.order_drink(self.drink, self.newRoom)
        self.bar.order_drink(self.drink, self.newRoom)
        self.assertEqual(2, self.bar.tab_list[self.newRoom.name][self.drink])

    def test_add_two_different_drinks_to_tab(self):
        self.guest = Guest("Ben", 50, "Purple Rain")
        self.drink = Drink("Peroni", 5)
        self.drink2 = Drink("Cobra", 4)
        self.newRoom = Room("DrinkRoom", 10, 10)
        self.bar.add_drink_to_stock(self.drink, 50)
        self.bar.add_drink_to_stock(self.drink2, 50)
        self.bar.start_tab(self.newRoom)
        self.bar.order_drink(self.drink, self.newRoom)
        self.bar.order_drink(self.drink2, self.newRoom)
        self.assertEqual(1, self.bar.tab_list[self.newRoom.name][self.drink])
        self.assertEqual(1, self.bar.tab_list[self.newRoom.name][self.drink2])

    def test_room_can_start_a_tab(self):
        self.newRoom = Room("New Room", 10, 5)
        self.bar.start_tab(self.newRoom)
        self.assertEqual(False, bool(self.bar.tab_list[self.newRoom.name]))

    def test_bar_can_have_two_tabs(self):
        self.room1 = Room("Room 1", 5, 5)
        self.room2 = Room("Room 2", 10, 3)
        self.bar.start_tab(self.room1)
        self.bar.start_tab(self.room2)
        self.assertEqual(False, bool(self.bar.tab_list[self.room1.name]))
        self.assertEqual(False, bool(self.bar.tab_list[self.room2.name]))

    def test_room_can_request_total_cost_of_tab(self):
        self.room1 = Room("Room 1", 5, 5)
        self.guest = Guest("John", 50, "Hello")
        self.drink1 = Drink("Peroni", 5)
        self.drink2 = Drink("Cobra", 4)
        self.room1.checkIn(self.guest)
        self.bar.add_drink_to_stock(self.drink1, 10)
        self.bar.add_drink_to_stock(self.drink2, 10)
        self.bar.start_tab(self.room1)
        self.bar.order_drink(self.drink1, self.room1)
        self.bar.order_drink(self.drink2, self.room1)
        self.assertEqual(9, self.bar.request_tab_cost(self.room1))

    # def test_room_can_pay_tab(self):
    #     self.room1 = Room("Room 1", 5, 5)
    #     self.guest = Guest("John", 10, "Hello")
    #     self.guest = Guest("John", 10, "Hello")
    #     self.drink1 = Drink("Peroni", 5)
    #     self.drink2 = Drink("Cobra", 4)
    #     self.drink3 = Drink("Menabrea", 7)
    #     self.room1.checkIn(self.guest)
    #     self.bar.add_drink_to_stock(self.drink1, 10)
    #     self.bar.add_drink_to_stock(self.drink2, 10)
    #     self.bar.add_drink_to_stock(self.drink3, 10)
    #     self.bar.start_tab(self.room1)
    #     self.bar.order_drink(self.drink1, self.room1)
    #     self.bar.order_drink(self.drink2, self.room1)
    #     self.bar.order_drink(self.drink3, self.room1)
    #     self.bar.pay_tab(self.room1)
    #     self.assertEqual(0, self.bar.request_tab_cost(self.room1))