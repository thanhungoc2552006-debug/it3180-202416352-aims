import contextlib
import io
import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()):
            for index in range(MAX_NUMBERS_ORDERED):
                self.assertTrue(cart.add_dvd(DigitalVideoDisc(str(index), cost=1)))
            self.assertFalse(cart.add_dvd(DigitalVideoDisc('overflow', cost=1)))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_total_and_remove(self):
        cart = Cart()
        dvd = DigitalVideoDisc('Example', cost='19.95')
        with contextlib.redirect_stdout(io.StringIO()):
            cart.add_dvd(dvd)
        self.assertAlmostEqual(cart.total_cost(), 19.95)
        self.assertTrue(cart.remove_dvd(dvd))
        self.assertFalse(cart.remove_dvd(dvd))
        self.assertEqual(cart.total_cost(), 0)

    def test_empty_cart_output(self):
        cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()) as output:
            result = cart.print_cart()
        self.assertEqual(result, 'The cart is empty')
        self.assertEqual(output.getvalue().strip(), result)

    def test_reject_non_dvd(self):
        with self.assertRaises(TypeError):
            Cart().add_dvd('DVD')
