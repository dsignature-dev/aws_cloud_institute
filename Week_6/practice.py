# # Create a file and write a welcome message to it.
# import os


# f = open("welcome.txt", "w")
# f.write("Hello! Welcome to the Python 1 module. This file is for testing purposes. Hope you are enjoying this module so far.")
# f = open("welcome.txt", "a")
# f.write("Add new line")
# f = open("welcome.txt", "r")
# print(f.read(8))

# # Open the file and print its contents.
# f = open("welcome.txt", "r")
# print(f.read())
# f.close()
# if os.path.exists("welcome.txt"):
#     os.remove("welcome.txt")
# else:
#     print("The file does not exist")

# Import the JSON module
import jsonschema
import json

# Define a JSON-formatted string.
x = '{ "name":"John", "lastname":"Stiles", "city":"Seattle"}'

# Convert the JSON string into a Python object.
y = json.loads(x)

# Print the value of 'city'.

print(y)


# import json

# # Open the JSON file.
# f = open('mydata.json', 'r')

# # Convert the JSON data into Python.
# mydata = json.load(f)

# # Close file.
# f.close()

# # The variable now contains a Python object representing the JSON file data.
# print(mydata['movie'])


# # Define a dictionary with three key-value pairs.
# x = {
#     "dog": "Jack",
#     "breed": "Golden Retriever",
#     "city": "Albuquerque"
# }

# # Convert dictionary into a JSON string using json.dumps().
# y = json.dumps(x, indent=4, separators=(". ", " = "))

# # Print output.
# print(y)


# Import the JSON module

# # Define JSON string
# x = '{"name": "John", "lastname": "Stiles", "city": "Seattle"}'

# # Parse JSON data into a Python dictionary
# py_dict = json.loads(x)

# # Loop through the Python dictionary
# for key, value in py_dict.items():
#     print(key, ":", value)


# Define a JSON schema.
schema = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string"},
        "lastname": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["firstname", "lastname", "age"]
}
# Validate a JSON document against the schema.
document = {
    "firstname": "John",
    "lastname": "Stiles",
    "age": "28"
}
try:
    jsonschema.validate(document, schema)
except jsonschema.exceptions.ValidationError as x:
    print(x)
