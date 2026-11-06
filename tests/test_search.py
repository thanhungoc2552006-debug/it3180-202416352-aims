import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.items = [DigitalVideoDisc('The Lion King'), DigitalVideoDisc('Star Wars')]

    def test_case_and_padding(self):
        self.assertEqual(search_by_title(self.items, '  LION  '), [self.items[0]])

    def test_blank_keyword(self):
        self.assertEqual(search_by_title(self.items, ''), [])
        self.assertEqual(search_by_title(self.items, '   '), [])

    def test_empty_and_missing_results(self):
        self.assertEqual(search_by_title([], 'lion'), [])
        self.assertEqual(search_by_title(self.items, 'missing'), [])

    def test_input_not_modified(self):
        original = list(self.items)
        search_by_title(self.items, 'star')
        self.assertEqual(self.items, original)
