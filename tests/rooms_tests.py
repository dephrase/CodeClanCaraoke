import unittest
from classes.rooms import *
from classes.guests import *
from classes.songs import *
from classes.drinks import *
from classes.bars import *
from tests.rooms_tests import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room 1", 10, 5)

    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room.name)

    def test_room_starts_with_no_guests(self):
        self.assertEqual(0, len(self.room.guests))

    def test_room_starts_with_no_songs(self):
        self.assertEqual(0, len(self.room.songs))

    def test_room_can_check_in_guest(self):
        self.guest = Guest("Barry", 10, "Hey Jude")
        self.room.checkIn(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_room_can_check_out_guests(self):
        self.guest = Guest("Barry", 10, "Hey Jude")
        self.room.checkIn(self.guest)
        self.room.checkOut(self.guest)
        self.assertEqual(0, len(self.room.guests))

    def test_room_can_add_songs(self):
        self.song = Song("Stayin Alive")
        self.room.addSong(self.song)
        self.assertEqual(1, len(self.room.songs))

    def test_room_can_have_multiple_guests(self):
        self.guest = Guest("Barry", 10, "Hey Jude")
        self.guest2 = Guest("John", 10, "Hey Jude")
        self.room.checkIn(self.guest)
        self.room.checkIn(self.guest2)
        self.assertEqual(2, len(self.room.guests))

    def test_room_can_have_multiple_songs(self):
        self.song = Song("Stayin Alive")
        self.song2 = Song("Night Fever")
        self.room.addSong(self.song)
        self.room.addSong(self.song2)
        self.assertEqual(2, len(self.room.songs))

    def test_room_has_max_capacity(self):
        self.assertEqual(10, self.room.max_capacity)

    def test_room_has_current_capacity(self):
        self.guest = Guest("Barry", 10, "Hey Jude")
        self.room.checkIn(self.guest)
        self.assertEqual(1, self.room.current_capacity)

    def test_guest_cannot_enter_if_room_at_max_capacity(self):
        self.smallCapacityRoom = Room("Small Capacity Room", 1, 5)
        self.guest = Guest("Barry", 10, "Hey Jude")
        self.guest2 = Guest("John", 10, "Hey Jude")
        self.smallCapacityRoom.checkIn(self.guest)
        self.smallCapacityRoom.checkIn(self.guest2)
        self.assertEqual(1, self.smallCapacityRoom.current_capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(5, self.room.entry_fee)

    def test_room_total_cash_increases_by_price(self):
        self.guest = Guest("Barry", 10, "Hey Jude")
        self.room.checkIn(self.guest)
        self.assertEqual(5, self.room.total_cash)

    def test_customer_cant_afford_room_entry_fee(self):
        self.guest = Guest("Barry", 2, "Hey Jude")
        self.lowEntryFeeRoom = Room("Low Entry Fee Room", 10, 5)
        self.lowEntryFeeRoom.checkIn(self.guest)
        self.assertEqual(0, self.lowEntryFeeRoom.current_capacity)
        self.assertEqual(2, self.guest.wallet)
        self.assertEqual(0, self.lowEntryFeeRoom.total_cash)

    def test_customer_whoops_if_room_has_favourite_song(self):
        self.guest = Guest("John", 50, "Hey Jude")
        self.newSong = Song("Hey Jude")
        self.newRoom = Room("Favourite Song Room", 10, 2)
        self.newRoom.addSong(self.newSong)
        self.assertEqual("Whoo!", self.newRoom.room_has_favourite_song(self.guest))

    def test_customer_boos_if_room_doesnt_have_favourite_song(self):
        self.guest = Guest("Ben", 50, "Purple Rain")
        self.song = Song("Happy Birthday")
        self.room.addSong(self.song)
        self.assertEqual("Boo!", self.room.room_has_favourite_song(self.guest))

    def test_customer_can_order_a_drink_and_add_to_bar_tab(self):
        self.guest = Guest("Ben", 50, "Purple Rain")
        self.drink = Drink("Peroni", 5)
        self.bar = Bar("Main Bar")
        self.newRoom = Room("DrinkRoom", 10, 10)
        self.bar.add_drink_to_stock(self.drink, 50)
        self.newRoom.order_drink(self.guest, self.drink, self.bar)
        self.assertEqual(1, self.bar.tab[self.drink])
        self.assertEqual(50, self.guest.wallet)
        self.assertEqual(0, self.newRoom.total_cash)

    def test_customer_add_two_drinks_to_tab(self):
        self.guest = Guest("Ben", 50, "Purple Rain")
        self.drink = Drink("Peroni", 5)
        self.bar = Bar("Main Bar")
        self.newRoom = Room("DrinkRoom", 10, 10)
        self.bar.add_drink_to_stock(self.drink, 50)
        self.newRoom.order_drink(self.guest, self.drink, self.bar)
        self.newRoom.order_drink(self.guest, self.drink, self.bar)
        self.assertEqual(2, self.bar.tab[self.drink])

    def test_add_two_different_drinks_to_tab(self):
        self.guest = Guest("Ben", 50, "Purple Rain")
        self.drink = Drink("Peroni", 5)
        self.drink2 = Drink("Cobra", 4)
        self.bar = Bar("Main Bar")
        self.newRoom = Room("DrinkRoom", 10, 10)
        self.bar.add_drink_to_stock(self.drink, 50)
        self.bar.add_drink_to_stock(self.drink2, 50)
        self.newRoom.order_drink(self.guest, self.drink, self.bar)
        self.newRoom.order_drink(self.guest, self.drink2, self.bar)
        self.assertEqual(1, self.bar.tab[self.drink])
        self.assertEqual(1, self.bar.tab[self.drink2])