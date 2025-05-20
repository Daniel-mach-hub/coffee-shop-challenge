from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

c1.create_order(latte, 4.5)
c1.create_order(espresso, 3.0)
c2.create_order(latte, 5.0)

print("Alice's Coffees:", [c.name for c in c1.coffees()])
print("Latte Customers:", [c.name for c in latte.customers()])
print("Latte Avg Price:", latte.average_price())
print("Most Aficionado for Latte:", Customer.most_aficionado(latte).name)
