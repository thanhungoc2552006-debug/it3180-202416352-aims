import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.items = [DigitalVideoDisc('The Lion King'), DigitalVideoDisc('Star Wars')]

    def test_case_and_padding(self):
        self.assertEqual(search_by_title(self.items, '  LION  '), [self.items[0]])

    def test_canonical_unicode_equivalence(self):
        composed = DigitalVideoDisc('Caf\u00e9 Society')
        decomposed = DigitalVideoDisc('Cafe\u0301 Society')
        self.assertEqual(search_by_title([composed], 'CAFE\u0301'), [composed])
        self.assertEqual(search_by_title([decomposed], 'Caf\u00e9'), [decomposed])

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



class CategorySearchTests(unittest.TestCase):
    def test_category_case_and_padding(self):
        from aims.search import search_by_category
        items = [DigitalVideoDisc('A', 'Animation'), DigitalVideoDisc('B', 'Drama'),
                 DigitalVideoDisc('C', 'Animation')]
        self.assertEqual(search_by_category(items, '  ANIMATION  '), [items[0], items[2]])

    def test_category_missing_and_blank(self):
        from aims.search import search_by_category
        items = [DigitalVideoDisc('A', 'Animation')]
        for category in ('', '  ', 'missing'):
            self.assertEqual(search_by_category(items, category), [])
        self.assertEqual(search_by_category([], 'Animation'), [])

    def test_category_preserves_input(self):
        from aims.search import search_by_category
        items = [DigitalVideoDisc('A', 'Animation'), DigitalVideoDisc('B', 'Drama')]
        before = list(items)
        search_by_category(items, 'Drama')
        self.assertEqual(items, before)
