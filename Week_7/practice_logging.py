import logging


# logging.basicConfig(level=logging.ERROR)

# logging.debug("This is a buggy message")
# logging.info("This is an information message")
# logging.warning("This is a warning111 message")
# logging.error("This is an errorr message")
# logging.critical("This is a critical message YIKES ")


# logging.basicConfig(level=logging.DEBUG)


def add_numbers(x, y):
    """Adds two numbers and returns the sum"""
    try:
        return x + y
    except:
        return (f"Cannot add {type(x)} and {type(y)}")


print(add_numbers("2", 3))

# def main():
#     add_numbers(2, 2)


# if __name__ == "__main__":
#     main()


# logging.basicConfig(filename="example.log", filemode='w',
#                     level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# logging.basicConfig(filename="example2.log",
#                     format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO,)


# def process_data():
#     number_list = []
#     customer_input = input("Please input numbers separated by commons.")
#     number_list.append(customer_input)
#     if "," not in customer_input:
#         logging.error("User did not enter a common between numbers")
#         logging.info("Function returns Try again")
#         return "Try again"

#     str_list = customer_input.split(',')

#     logging.info("user input is %i items long", len(str_list))
#     num_list = [int(x) for x in str_list]
#     logging.info("function returns %s", num_list)
#     # return (num_list)


# print(process_data())
