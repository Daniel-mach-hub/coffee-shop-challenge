from order import Order

class Customer:
    _all = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        best_customer = None
        most_spent = 0
        for customer in cls._all:
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total > most_spent:
                most_spent = total
                best_customer = customer
        return best_customer
