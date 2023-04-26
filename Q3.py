from Q2 import Item

# food as the child class of Item


class Food(Item):
    def __init__(self, item_name, quantity, price):
        super().__init__(item_name, quantity, price)
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    # the formatted string replaces the parameters with their values
    def full_info(self):
        super().full_info()
        return f"Food {self.item_name} {self.price} {self.quantity} {self.get_total_price()}"

# Drink as the child class of Item


class Drink(Item):
    def __init__(self, item_name, quantity, price):
        super().__init__(item_name, quantity, price)
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    # the formatted string replaces the parameters with their values
    def full_info(self):
        super().full_info()
        return f"Drink {self.item_name} {self.price} {self.quantity} {self.get_total_price()}"


# the objects
f1 = Food("Bread", 2, 1.3)
f2 = Food("Butter", 1, 1.3)

d1 = Drink("CocaCola", 3, 1.7)
d2 = Drink("Sprite", 2, 1.7)

print(f1.full_info())
print(f2.full_info())
print(d1.full_info())
print(d2.full_info())
