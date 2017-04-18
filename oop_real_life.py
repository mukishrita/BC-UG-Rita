class ShoppingCart(object):
    """ 
        A shopping cart
    """
    def __init__(self):
    	self.total = 0
    	self.items = {}

    def add_item(self, item_name, quantity, price):
    	if isinstance(quantity, int) and isinstance(price, int):
            self.items[item_name] = quantity
            self.total += (price * quantity)

    def remove_item(self, item_name, quantity, price):
        if isinstance(quantity, int) and isinstance(price, int):
            if item_name in self.items:
                if  quantity >= self.items[item_name]:
                    if self.total >= (price * self.items[item_name]):  
                         self.total -= (price * self.items[item_name])
                    del(self.items[item_name])
                else:
                    self.items[item_name] -= quantity
                    if self.total >= (price * quantity):
                        self.total -= (price * quantity)
                    else:
                        self.total -= (price * self.items[item_name])

    def checkout(self, cash_paid):
    	if isinstance(cash_paid, int):
            if cash_paid >= self.total:
                return cash_paid - self.total
            else:
                return "Cash paid not enough"


class Shop(ShoppingCart):
    """
        A Shop
    """
    def __init__(self):
        self.quantity = 100

    def remove_item(self):
        self.quantity -= 1

cart = ShoppingCart()
cart.add_item("Car", 1, 2000)
cart.add_item("Book", 5, 3)
cart.add_item("Laptop", 1, 1000)
cart.add_item("Phone", 1, 600)

print(cart.items)
print(cart.total)

print(cart.checkout(5000))

shop = Shop()
shop.remove_item()

print(shop.quantity)
