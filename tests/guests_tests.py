import unittest
from classes.guests import *
from tests.guests_tests import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Barry", 10, "Stayin Alive")

    def test_guest_has_name(self):
        self.assertEqual("Barry", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(10, self.guest.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Stayin Alive", self.guest.favourite_song)

    

