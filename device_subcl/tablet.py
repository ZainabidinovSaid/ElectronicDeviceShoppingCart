from device import Device


class Tablet(Device):
    def __init__(self, name, price, stock, screen_resolution, weight, warranty_period=12):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def browse_internet(self, website="youtube.com"):
        print(f'{self.name} is browsing {website}...')

    def use_touchscreen(self):
        print(f"Using {self.name}'s touchscreen...")

    def display_info(self):
        return f'Name: {self.name}, Price: {self.price}$, Stock: {self.stock}, Warranty period: {self.warranty_period} months, Screen resolution: {self.screen_resolution}, Weight: {self.weight} grams'