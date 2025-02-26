class Device:
    def __init__(self, name, price, stock, warranty_period=12):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    def display_info(self):
        return f'Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty period: {self.warranty_period} months'

    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.price -= self.price * (discount_percentage / 100)

    def is_available(self, amount):
        return amount <= self.stock

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount