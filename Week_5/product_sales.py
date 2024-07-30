"""
This module contains classes for tracking 
product and sales data.
"""


class Product:
    def __init__(self, name, price, inventory):
        self.name = name
        self.price = price
        self.inventory = inventory

    def __str__(self):
        return f"{self.name} (${self.price})"

    # def string(self):
    #     return f"{self.name} (${self.price})"


prod1 = Product("WidgetA", 1.26, 50)


print(prod1.name)
print(prod1.price)
print(prod1.inventory)
print(prod1)
