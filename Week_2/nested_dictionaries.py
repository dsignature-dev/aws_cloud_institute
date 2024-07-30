employees = {
    '001': {
        'name': 'John',
        'age': 35,
        'position': 'Manager',
        'department': 'Sales'
    },
    '002': {
        'name': 'Ana',
        'age': 28,
        'position': 'Engineer',
        'department': 'IT'
    },
    '003': {
        'name': 'Carlos',
        'age': 42,
        'position': 'Director',
        'department': 'Operations'
    }
}
print(employees['001']["name"])


employees = {
    "001": {
        "name": "John",
        "age": 35,
        "position": "Manager",
        "department": "Sales",
        "location": {
            "street_address": "123 Main Street",
            "city": "Anytown",
            "country": "USA",
        },
    },
    "002": {
        "name": "Ana",
        "age": 28,
        "position": "Engineer",
        "department": "IT",
        "location": {
            "street_address": "456 Any Ave",
            "city": "Anyville",
            "country": "USA",
        },
    },
}


print(employees["002"]["location"]["street_address"])
