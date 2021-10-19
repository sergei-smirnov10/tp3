from rss import words
from rss import app
import unittest


class UnitTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(words.list_words(2), 'Питон')

    def test2(self):
        self.assertEqual(app.app_cod(), '')

    def test3(self):
        self.assertEqual(app.app_cod(), '')