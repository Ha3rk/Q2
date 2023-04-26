from shop_customers import names
from shop_items import Food, Drink


class Customer:
    _customer_count = 0

    def __init__(self, name, shopping_cart=None):
        if not isinstance(name, str):
            raise TypeError("Name should be a string.")
        self._name = name
        Customer._customer_count += 1
        self._identifier = Customer._customer_count
        self.shopping_cart = [] if shopping_cart is None else shopping_cart

    def add_item(self, item):
        if not isinstance(item, (Food, Drink)):
            raise TypeError("Item should be a Food or Drink object.")
        self.shopping_cart.append(item)

    def remove_item(self, index):
        if index >= len(self.shopping_cart):
            raise IndexError("Index is out of range.")
        self.shopping_cart.pop(index)

    def get_items(self):
        return [item.full_info() for item in self.shopping_cart]

    def get_identifier(self):
        return self._identifier

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name should be a string.")
        self._name = value

    def full_info(self):
        return f"({self._identifier}) {self._name}"


c1 = Customer("Jonas Jonaitis", [
              Food("Bread", 2, 1.3), Drink("CocaCola", 3, 1.7)])
c2 = Customer("Petras Petraitis", [
              Food("Butter", 1, 1.3), Drink("Sprite", 2, 1.7)])

print(c1.get_items())
print(c2.get_items())

c1.add_item(Drink("Fanta", 10, 1.7))
print(c1.get_items())

c2.remove_item(2)
c2.remove_item(1)
print(c2.get_items())
