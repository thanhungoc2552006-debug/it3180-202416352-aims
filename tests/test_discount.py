import contextlib
import io
import unittest
from decimal import Decimal

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class DiscountTests(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()):
            self.cart.add_dvd(DigitalVideoDisc('Example', cost=100))

    def test_integer_discount(self):
        self.assertEqual(self.cart.total_cost_with_discount(20), 80)

    def test_fractional_discount(self):
        self.assertEqual(self.cart.total_cost_with_discount(20.5), 79.5)
        self.assertEqual(self.cart.total_cost_with_discount(Decimal('20.5')), 79.5)

    def test_boundary_discounts(self):
        self.assertEqual(self.cart.total_cost_with_discount(0), 100)
        self.assertEqual(self.cart.total_cost_with_discount(100), 0)

    def test_invalid_discounts(self):
        for percent in (-1, 150, float('nan'), float('inf'), True, '20'):
            with self.subTest(percent=percent), self.assertRaises(ValueError):
                self.cart.total_cost_with_discount(percent)
