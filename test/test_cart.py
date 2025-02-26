from cart import Cart
import unittest
from device import Device


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.device1 = Device('Samsung A34', 399, 10, 12)
        self.device2 = Device('Acer Aspire 3', 399, 10, 12)
        self.device3 = Device('Ipad Air11', 399, 10, 12)

    def test_add_device(self):
        self.cart.add_device(self.device1, 10)
        self.cart.add_device(self.device2, 8)
        self.cart.add_device(self.device3, 5)
        self.assertIn((self.device1, 10), self.cart.items)
        self.assertIn((self.device2, 8), self.cart.items)
        self.assertIn((self.device3, 5), self.cart.items)

    def test_remove_device(self):
        self.cart = Cart()
        self.cart.add_device(self.device1, 10)
        self.cart.remove_device(self.device1, 10)
        self.assertNotIn((self.device1, 10), self.cart.items)

    def test_calculate_total(self):
        self.cart = Cart()
        self.cart.add_device(self.device1, 1)
        self.cart.add_device(self.device2, 1)
        self.cart.add_device(self.device3, 1)
        total = self.cart.get_total_price()
        self.assertEqual(total, 1197)

    def test_checkout(self):
        self.cart = Cart()
        self.assertEqual(self.cart.checkout(), None)
        self.cart.add_device(self.device1, 10)
        self.cart.add_device(self.device2, 10)
        self.cart.add_device(self.device3, 10)
        self.cart.checkout()
        self.assertEqual(self.cart.items, [])
        self.assertEqual(self.cart.total_amount, 0)