from device import Device


class Smartphone(Device):
    def __init__(self, name, price, stock, screen_size, battery_life, warranty_period=12):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def make_call(self, phone_number):
        print(f'{self.name} is calling {phone_number}...')

    def install_app(self, app_name):
        print(f'Installing {app_name} on {self.name}...')

    def display_info(self):
        return f'Name: {self.name}, Price: {self.price}$, Stock: {self.stock}, Warranty period: {self.warranty_period} months, Screen size: {self.screen_size} inches,Battery life: {self.battery_life} hours'