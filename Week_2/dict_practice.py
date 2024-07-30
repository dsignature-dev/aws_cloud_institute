more_edits = True
inventory = {}

while more_edits:
    choice = int(input("What would you like to do? Please enter a number \n \
    1. Add new item  \n \
    2. Increase qty of existing item \n \
    3. Decrease qty of existing item \n \
    4. Quit \n"))

    if choice == 1:
        item_name = input("What is the name of item? ")
        item_qty = int(input("What is the quantity of this item? "))
        inventory[item_name] = item_qty
        # print(inventory)

    elif choice == 2:
        item_name = input("What is the name of item? ")

        if item_name not in inventory.keys():
            print("This item is not in our inventory, please pick another item" / n/n)
        else:
            qty_increase = int(input("How many would you like to add? "))
            inventory[item_name] += qty_increase
            print(inventory)

    elif choice == 3:
        item_name = input("What is the name of item? ")

        if item_name not in inventory.keys():
            print("This item is not in our inventory, please pick another item" / n/n)
        else:
            qty_decrease = int(input("How many would you like to take away? "))
            inventory[item_name] -= qty_decrease
            print(inventory)
    else:
        more_edits = False

print(inventory)
