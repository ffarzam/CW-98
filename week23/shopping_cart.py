class ShoppingCart:

    def __init__(self):
        self.observers = []
        self.items = []
        self.total_price = 0

    def reg(self, observer):
        self.observers.append(observer)

    def add_item(self, item):
        self.items.append(item)
        self.total_price += item.price

    def remove_item(self, item):
        self.items.remove(item)
        self.total_price -= item.price

    def notify(self):
        for observer in self.observers:
            observer.tp(self)


class TotalPrice:
    @classmethod
    def tp(cls, cart):
        tp = cart.total_price
        tp -= Discount.calculate_discount(cart)
        return tp


class Discount:
    discount_amount = 0.1

    @classmethod
    def calculate_discount(cls, cart: ShoppingCart):
        if cart.total_price > 100:
            return cart.total_price * cls.discount_amount
        else:
            return 0


class Checkout:

    def checkout(self, cart, tp_obj):
        final_price = tp_obj.tp(cart)

        print(f"Total price: {cart.total_price}")
        print("final price", final_price)


class Item:
    def __init__(self, price, quantity):
        self.price = price


i1 = Item(100)
i2 = Item(200)
tp = TotalPrice()
cart = ShoppingCart()
cart.reg(tp)
cart.add_item(i1)
cart.add_item(i2)
cart.notify()

checkout = Checkout()
checkout.checkout(cart, tp)
