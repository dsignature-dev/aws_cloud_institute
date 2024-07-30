# import the necessary modules, objects, and functions.

# Cup 1.00
# Cone 1.50
# Scoop 1.50
from datetime import datetime
import json


cup_cost = 1.00
cone_cost = 1.50
scoop_cost = 1.50
# Get the current date, and use it to programmatically generate the file name you want to read.
today = datetime.now()
todays_order = today.strftime("orders_%Y%m%d.txt")

orders = []

total_sales = 0


f = open(todays_order, "r")

for line in f:
    order = json.loads(line)
    orders.append(order)

f.close()

for order in orders:
    order_sale = 0

    for item in order:
        if item['container'] == 'cone':
            order_sale += cup_cost
        else:
            order_sale += cone_cost

        num_scoops = len(item["scoops"])
        order_sale += num_scoops * scoop_cost


print(f"Total cost of order is {order_sale}")
