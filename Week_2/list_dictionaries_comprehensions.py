numbers = [4, 15, 12, 16, 2, 6, 10, 2, 7, 11]

doubled_numbers = []  # initialize an empty list to hold new values

for n in numbers:
    doubled_numbers.append(n*2)

print(doubled_numbers)
# Expected output:

[8, 30, 24, 32, 4, 12, 20, 4, 14, 22]


# Another way to complete this task is to use a list comprehension. A list comprehension creates a new list and populates it with the new calculated numbers in a single line of code. The following image shows the syntax associated with a basic list comprehension.
numbers = [4, 15, 12, 16, 2, 6, 10, 2, 7, 11]

doubled_numbers = [n*2 for n in numbers]

print(doubled_numbers)


# Using list comprehensions with conditions
numbers = [4, 15, 12, 16, 2, 6, 10, 2, 7, 11]


doubled_highs = [n*2 for n in numbers if n*2 >= 20]
print(doubled_highs)


# Dictionary comprehensions are very similar to list comprehensions.

# dictionary = {key: value for temp_variable in iterable}

# list = [value for temp_variable in iterable]


# Creating a dictionary from two lists
# zip() function to create a tuple from two lists.
names = ["Alice", "Bob", "Carlos", "Olivia", "Jane"]
ages = [27, 32, 56, 47, 29]

people = {key: value for key, value in zip(names, ages)}

print(people)
