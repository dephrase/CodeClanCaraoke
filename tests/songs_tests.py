import unittest
from classes.songs import *
from tests.songs_tests import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0
class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Stayin Alive")

    def test_song_has_name(self):
        self.assertEqual("Stayin Alive", self.song.name)