class Customer:
    _customer_count = 0

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name should be a string.")
        self._name = name
        Customer._customer_count += 1
        self._identifier = Customer._customer_count

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name should be a string.")
        self._name = value

    def get_identifier(self):
        return self._identifier

    def full_info(self):
        return f"{self._identifier} - {self._name}"


c1 = Customer("Jonas Jonaitis")
c2 = Customer("Petras Petraitis")
c3 = Customer("Lukas Lukauskas")

print(c1.get_identifier())
print(c2.get_identifier())
print(c3.get_identifier())


print(c1.full_info())
print(c2.full_info())
print(c3.full_info())
