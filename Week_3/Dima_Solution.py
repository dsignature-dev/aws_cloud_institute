# Task 2: Automated order-taker

# For this task, imagine that you are the proud owner of an ice cream shop.  As an entrepreneur, you know that increased efficiency can be the thing that sets you apart from other stores. With all that you now know about iterables, data types, conditionals, and user input, you're ready to build the logic for an application that can automatically take customer orders.

# To create a complete order, your order-taker needs to know how the ice cream should be served, the number of scoops requested, and the flavor of ice cream for each scoop. The following table includes the suggested options.
# Option	            Available choices
# container type      cone or cup
# Number of scoops    1, 2, or 3
# Flavor types        vanilla, strawberry, chocolate, cherry, mint, peach, or grape

# Write a program that greets customers and takes their ice cream order. Allow customers to order multiple cones or cups, with a different flavor possible for each scoop. If a customer enters an invalid option, notify them of the error and prompt them again.

# Consider the following questions as you plan your program:

#     1. Each of the available choices should be stored as a collection. Which type of collection might work the best for storing data that is unlikely to change, like menu data?
#     2. Control the flow of your program using loops and conditionals. Remember that your order-taker should keep asking for orders until the customer is finished ordering. Also, each input the customer enters should be checked for validity before being accepted as an answer.
#     3. Check user input before you try to process it in your program. If your program expects an integer, but gets a string instead, the whole order could crash. Refer to the Python documentation(opens in a new tab) about the built-in isnumeric() method. Try using it to help you validate numeric user input without errors.

# 1. data structure for vars
# list of container types
container_types = ('cone', 'cup')
# list of flavors
flavors = ('vanilla', 'strawberry', 'chocolate',
           'cherry', 'mint', 'peach', 'grape')
# number of scoops
scoops = (1, 2, 3)
# list of order
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
    if user_input in container_types:
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

# yes no validation


def yes_no_validation(user_input):
    if user_input in ('y', 'n'):
        return True
    else:
        return False


# 2. control loop for order
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
