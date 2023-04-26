#make item the parent class
class Item:

    #get item_name, quantity and price
    def __init__(self, item_name, quantity=1, price=10):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    #multiply quantity and price
    def get_total_price(self):
        return self.quantity * self.price

    #the formatted string replaces the parameters with their values
    def full_info(self):
        return f"{self.item_name}  {self.price}  {self.quantity}  {self.get_total_price()}"
    
    #conversion of the above parameters into a dictionary
    def to_dict(self):
        return {"name": self.item_name, "quantity": self.quantity, "price": self.price, "total_price": self.get_total_price()}
    
#the objects
i1 = Item("Carrots")
i2 = Item("Milk", 2, 1.5)
i3 = Item("Bread", price=0.5)

print(i1.full_info())
print(i2.full_info())
print(i3.full_info())

print(i1.to_dict())
print(i2.to_dict())
print(i3.to_dict())