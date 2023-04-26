from shop_customers import names
from shop_items import Food, Drink
import json


class Customer:
    _customer_count = 0

    def __init__(self, name, items=None):
        self.name = name
        self.identifier = Customer._customer_count + 1
        Customer._customer_count += 1
        self.items = items or []

    @property
    def full_info(self):
        return f"{self.identifier} - {self.name}"

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        try:
            del self.items[index]
        except IndexError:
            print(f"Error: Index {index} is out of range for item list.")

    def get_items(self):
        return [item.full_info for item in self.items]

    def export_to_json(self, file_path):
        data = {
            "name": self.name,
            "identifier": self.identifier,
            "items": [item.__dict__ for item in self.items]
        }
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Exported customer data to {file_path} successfully.")


c1 = Customer("Jonas Jonaitis", [
              Food("Bread", 2, 1.3), Drink("CocaCola", 3, 1.7)])

c1.export_to_json("./tmp/c1.json")
