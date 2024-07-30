# Write a function that takes a numeric argument and returns True if the argument is even, False if it's not even.
def even(num):
    if (num % 2) == 0:
        print(f"{num} is an even number!")
        return True

    else:
        # print(f"{num} is an odd number!")
        return False


# Write a function that takes a numeric argument and returns True if the argument is odd, and False if it's not odd.
def odd(num):
    if (num % 2) != 0:
        print(f"{num} is an odd number!")
        return True

    else:
        # print(f"{num} is an even number!")
        return False


for x in range(1, 14):
    even(x)
    odd(x)
