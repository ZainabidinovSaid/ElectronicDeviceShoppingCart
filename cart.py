class Cart:
    def __init__(self):
        self.items = []
        self.total_amount = 0

    def add_device(self, device, amount):
        pair = (device, amount)
        self.items.append(pair)
        print(f'Added to cart: {amount} of {device.display_info()}')

    def remove_device(self, device, amount):
        for index, (item_device, quantity) in enumerate(self.items):
            if item_device == device:
                if amount >= quantity:
                    self.items.pop(index)
                else:
                    self.items[index] = (item_device, quantity - amount)

        print(f"{device.name} is not in the cart.")

    def get_total_price(self):
        self.total_amount = sum(device.price * quantity for device, quantity in self.items)
        return self.total_amount

    def print_items(self):
        for device, quantity in self.items:
            print(f"{quantity} x {device.name} - ${device.price} each")

    def checkout(self):
        total = 0
        receipt = "Receipt\n"

        for device, quantity in self.items:
            receipt += f"{quantity} x {device.name} - ${device.price * quantity}\n"
            total += device.price * quantity

        receipt += f"Total Amount: ${total}"
        self.items.clear()
        self.total_amount = 0

        return receipt