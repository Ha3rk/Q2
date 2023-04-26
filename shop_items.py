
class Food:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def full_info(self):
        return f"{self.name} ({self.quantity} units) - ${self.price:.2f}"


class Drink:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def full_info(self):
        return f"{self.name} ({self.quantity} bottles) - ${self.price:.2f}"


# food items
chocolate = Food("Chocolate", 10, 2.5)
bread = Food("Bread", 5, 3.0)
apples = Food("Apples", 12, 1.8)
butter = Food("Butter", 1, 1.3)

# drink items
coke = Drink("Coca-Cola", 6, 2.0)
orange_juice = Drink("Orange Juice", 4, 2.5)
lemonade = Drink("Lemonade", 8, 1.5)
sprite = Drink("Sprite", 2, 1.7)
