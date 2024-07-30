# How to write tuples
tuple_w_brackets = (2, 3, 4)
print(type(tuple_w_brackets))

tuple_no_brackets = 2, 3, 4
print(type(tuple_no_brackets))

tuple_w_brackets = (1,)
print(type(tuple_w_brackets))

tuple_no_brackets = 1,
print(type(tuple_no_brackets))

tuple_constr = tuple()
print(type(tuple_constr))

convert_to_tuple = tuple([1, 2, 3])
print(type(convert_to_tuple))

# how to index tuples

new_tuple = ("zero", "one", "two", "three", "four")

print(new_tuple[0])

print(new_tuple[-1])

# how to count or show index of first occurence

my_tuple = (1, 2, 3, 4, 1, 2, 3, 4)

print(my_tuple.count(1))  # the number of times 1 appears in the tuple
print(my_tuple.index(2))   # the index of the first occurence of a 2


# unpacking tuples
"""
Each transaction record includes:
item name (str)
quantity (int)
date (str)
price (float)
"""

purchase = ("product-1", 2, "6-1-2023", 5.99)

item = purchase[2]
quantity = purchase[0]

print(item)
print(quantity)

# You can also unpack all elements of a tuple with a single line of code. The order of your assigned variables should match the order of the items in the tuple.
purchase = ("product-1", 2, "6-1-2023", 5.99)

item, quantity, date, price = purchase

print(item)
print(quantity)
print(date)
print(price)

# Joining tuples
# You can use addition and multiplication operators to join different tuples or repeat an existing tuple, respectively.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combo_tuple = tuple1 + tuple2
print(combo_tuple)

# Repeat Tuples
# To repeat the elements in a tuple, use the multiplication (*) operator as follows.


tuple1 = (1, 2, 3)
repeat_tuple = tuple1*2
print(repeat_tuple)


names = ["Alejandro", "Ana", "carlos", "john", "Jane", "Paulo"]


for name in names:
    name = name.title()
    print(f"Hello, {name}!")

convert_to_set = set(names)

for name in convert_to_set:

    print(f"Hello, {name.title()}!")


names = ["Alejandro", "Ana", "carlos", "john", "Jane", "Paulo"]

for i in range(len(names)):
    print(f"{names[i]} is at position {i}")
