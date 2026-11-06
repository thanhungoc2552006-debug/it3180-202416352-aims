import unittest
from aims.cart import Cart, sort_by_cost, sort_by_title
from aims.dvd import DigitalVideoDisc as D


class SortTests(unittest.TestCase):
    def test_title_sort_both_directions(self):
        cart = Cart()
        cart.items = [D('beta', cost=2), D('Alpha', cost=1)]
        self.assertEqual([d.title for d in cart.sort_by_title()], ['Alpha', 'beta'])
        self.assertEqual([d.title for d in cart.sort_by_title(reverse=True)], ['beta', 'Alpha'])

    def test_cost_sort_and_ties(self):
        cart = Cart()
        cart.items = [D('B', cost=2), D('A', cost=2), D('C', cost=1)]
        self.assertEqual([d.title for d in cart.sort_by_cost()], ['C', 'A', 'B'])
        self.assertEqual([d.title for d in cart.sort_by_cost(reverse=True)], ['B', 'A', 'C'])

    def test_helpers_preserve_input(self):
        items = [D('B', cost=2), D('A', cost=1)]
        self.assertEqual([d.title for d in sort_by_title(items)], ['A', 'B'])
        self.assertEqual([d.title for d in sort_by_cost(items, reverse=True)], ['B', 'A'])
        self.assertEqual([d.title for d in items], ['B', 'A'])

    def test_empty_sort(self):
        self.assertEqual(Cart().sort_by_cost(reverse=True), [])
        self.assertEqual(Cart().sort_by_title(), [])
        self.assertEqual(sort_by_title([], reverse=True), [])
