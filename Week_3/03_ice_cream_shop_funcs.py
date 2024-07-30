"""
This code contains the model solution for one of the lab exercises from
Data Structures and Iterables. Your task is to modify this program so that it 
uses functions to validate user input. 
"""

# Available flavors tuple
flavors = (
    "vanilla",
    "strawberry",
    "chocolate",
    "cherry",
    "mint",
    "peach",
    "grape",
)
# Available containers tuple
containers_types = ("cone", "cup")

# Available number of scoops tuple
scoops = (1, 2, 3)


# Empty list to hold orders
orders = []

# function to get use input and vaildate it; return user input if valid else ask for user input again


def get_input_and_validate(validation_function, prompt, reprompt):
    while True:
        user_input = input(prompt)
        if validation_function(user_input):
            return user_input
        else:
            print(reprompt)

# container type validation


def container_type_validation(user_input):
    if user_input in containers_types:
        return True
    else:
        return False
# number of scoops validation


def number_of_scoops_validation(user_input):
    if user_input.isnumeric() and int(user_input) in scoops:
        return True
    else:
        return False

# flavor type validation


def flavor_type_validation(user_input):
    if user_input in flavors:
        return True
    else:
        return False


def yes_no_validation(user_input):
    if user_input in ('y', 'n'):
        return True
    else:
        return False


# Order loop
while True:

    # 5. ask and validate input for container type in a loop then add it to a order dict
    order = {}
    order['container_type'] = get_input_and_validate(
        container_type_validation, 'What type of container would you like? (cone or cup) ', 'Your input was invalid please enter "cone" or "cup"')
    # 6. ask and validate for being numeric and number of scoops then add it to a order dict
    order['num_scoops'] = int(get_input_and_validate(number_of_scoops_validation,
                              'How many scoops would you like? ', 'Your input was invalid please enter 1, 2, or 3'))
    # 7. ask and validate for flavor type for each scoop then add it to a order dict
    flavor_list = []
    # 8. loop for flavor type for each scoop then add it to a order dict
    for i in range(order['num_scoops']):
        flavor_list.append(get_input_and_validate(
            flavor_type_validation, f'What flavor would you like for scoop {i+1}: vanilla, strawberry, chocolate, cherry, mint, peach, grape? ', 'Your input was invalid please enter "vanilla", "strawberry", "chocolate", "cherry", "mint", "peach", or "grape"'))
    # add flavor list to order dict
    order['flavor_list'] = flavor_list
    # add order to orders list
    orders.append(order)

    # 3 ask and validate if customer wants another order, set orders_complete to true
    orders_complete = True if get_input_and_validate(
        yes_no_validation, 'Would you like to order another ice cream? (y/n) ', 'Your input was invalid please enter "y" or "n"') == 'n' else False

    # 4. if orders_complete == True break out of loop
    if orders_complete == True:
        break

# 9 print orders with formatting
print()
print()
for i, order in enumerate(orders):
    print(
        f'Your order #{i+1} is a {order["container_type"]} with {order["num_scoops"]} scoops of {order["flavor_list"]}')
