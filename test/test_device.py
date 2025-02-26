from device import Device
import unittest


class TestDevice(unittest.TestCase):
    def setUp(self):
        self.device1 = Device('Samsung', 399, 10, 12)

    def test_display_info(self):
        expect_info = f'Name: Samsung, Price: 399, Stock: 10, Warranty period: 12'
        self.assertEqual(self.device1.display_info(), expect_info)

    def test_apply_discount(self):
        for x in range(10, 101, 10):
            expect_price = self.device1.price - self.device1.price * (x / 100)
            self.device1.apply_discount(x)
            self.assertEqual(expect_price, self.device1.price)

    def test_is_available(self):
        expect_amount = self.device1.stock
        self.assertTrue(expect_amount, self.device1.is_available(10))

    def test_reduce_stock(self):
        expect_stock = self.device1.stock - 5
        self.device1.reduce_stock(5)
        self.assertEqual(self.device1.stock, expect_stock)
        self.device1.reduce_stock(10)
        self.assertNotEqual(self.device1, expect_stock)