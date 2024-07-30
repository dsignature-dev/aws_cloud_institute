"""
This module contains classes for tracking 
product and sales data.
"""


class Sales:
    def _init__(self):
        self.sales_data = []

    def add_sale(self, product, quantity):
        sale = {'product': product, 'quantity': quantity}
        self.sales_data.append(sale)

# Loop through the sales_data list to accumulate the total value of all sales in the list. Remember that each sales record includes a Product object from which you can extract the price. Also, each sales record includes a quantity that should be factored into the total sale amount.


def generate_report(self):
    total_sale = 0
    for sale in self.sales_data:
        total_sale += sale['product'].price * sale['quantity']


# Initialize an empty string that will hold the final report.
    report = ""


# Create a collection that holds the unique products from the sales_data list. Loop through that collection and the associated sales data to determine to quantity of each product sold.
    product_set = set([sale['product'] for sale in self.sales_data])


#  As you loop through the set of unique products, use the price and quantity to calculate the total revenue from each product. Round revenue to the nearest cent.
    for product in product_set:
        quants = [sale['quantity']
                  for sale in self.sales_data if sale['product'] == product]
        quantity_sold = sum(quants)
        revenue = round(product.price * quantity_sold, 2)
        report += f"{product}: {quantity_sold} sold for a total revenue of ${revenue}\n"

    report += f"Total Sales: ${total_sale}\n"

# Report each product and quantity on a new line of the report. Use the "\n" newline character and the "+=" operator to add new lines to the report.
    return report

# The final line of the report should list the total sales for the object. Return the report.


def test_classes():
    prod1 = Product("WidgetA", 10.99, 100)
    prod2 = Product("WidgetB", 19.99, 50)
    prod3 = Product("WidgetC", 7.99, 150)
    prod4 = Product("WidgetD", 3.99, 500)

    sales = Sales()
    sales.add_sale(prod1, 15)
    sales.add_sale(prod2, 30)
    sales.add_sale(prod3, 45)
    sales.add_sale(prod1, 30)
    sales.add_sale(prod4, 100)

    print(sales.generate_report())
