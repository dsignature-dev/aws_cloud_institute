
names = ["Alejandro", "Ana", "carlos", "john", "Jane", "Paulo"]


for name in names:
    name = name.title()
    print(f"Hello, {name}!")

convert_to_set = set(names)

for name in convert_to_set:

    print(f"Hello, {name.title()}!")


# using range and index

names = ["Alejandro", "Ana", "carlos", "john", "Jane", "Paulo"]

for i in range(len(names)):
    print(f"{names[i] } is at position {i+1}")

# or use enumerate method
for i, name in enumerate(names):
    print(f"{i}: {name.title()}")

# looping through dictionaries ..The most basic for loop to loop through a dictionary exposes the dictionary's keys by default. For this dictionary, the keys are days of the week.
sales_wk1 = {
    "Monday": 10,
    "Tuesday": 10,
    "Wednesday": 5,
    "Thursday": 5,
    "Friday": 15,
    "Saturday": 20,
    "Sunday": 15
}
# for x in sales_wk1:
#     print(x)

# or use keys()
for x in sales_wk1.keys():
    print(x)

# to get value use values()
for x in sales_wk1.values():
    print(x)

# accessing by values key

sales_wk1 = {
    "Monday": 10,
    "Tuesday": 10,
    "Wednesday": 5,
    "Thursday": 5,
    "Friday": 15,
    "Saturday": 20,
    "Sunday": 15
}

total_sales = 0

for k in sales_wk1:
    total_sales += sales_wk1[k]

print(total_sales)


sales_dict = {'2022-03-01': 100,
              '2022-03-02': 200, '2022-03-03': 150,
              '2022-03-04': 300, '2022-03-05': 250,
              '2022-03-06': 175, '2022-03-07': 225}

best_sales = 0
total_sales = 0

for k, v in sales_dict.items():
    total_sales += v

if v > best_sales:
    best_sales = v
    best_day = k

wk_avg = total_sales/len(sales_dict.keys())
print(f"The best sales day is {best_day}. The weekly aveerage is {wk_avg}")


# Accessing nested items
employees = [
    {"name": "John", "age": 35, "position": "Manager", "department": "Sales"},
    {"name": "Ana", "age": 28, "position": "Engineer", "department": "IT"},
    {"name": "Carlos", "age": 42, "position": "Director",
        "department": "Operations"}
]

for emp in employees:
    print(f'{emp["name"]} is {emp["age"]} years old.')


# Using a list of dictionaries with lists

students = [
    {'name': 'Alice', 'age': 20, 'grades': [90, 85, 95]},
    {'name': 'Bob', 'age': 21, 'grades': [80, 75, 70]},
    {'name': 'Charlie', 'age': 19, 'grades': [95, 90, 92]},
]

for student in students:
    # grades holds the grades list for the loops current iteration
    grades = student['grades']
    # sum of grades divided by length of list is an average calculation
    avg_grade = sum(grades) / len(grades)
    # creates a new key-value for each student
    student['avg_grade'] = round(avg_grade, 2)

print(students)

# Challenge

responses = [
    {"question": "What is your name?", "response_time": 12},
    {"question": "What is your age?", "response_time": 10},
    {"question": "What is your favorite color?", "response_time": 15},
    {"question": "What is your favorite animal?", "response_time": 15},
    {"question": "What is your favorite joke?", "response_time": 14},
    {"question": "Where were you born?", "response_time": 11},
    {"question": "What is your shoe size?", "response_time": 18},
    {"question": "What is your education level?", "response_time": 13},
    {"question": "What is your dream job?", "response_time": 9}
]

total_time = 0

for r in responses:
    total_time += r["response_time"]

    avg_time = (total_time/len(responses))

    print(f"the average time is {avg_time}")
