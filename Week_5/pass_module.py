

# Create the module file. Define functions to check if the user included special characters, uppercase letters, lowercase letters, and numbers. Each check should add a point to the overall strength score if the check is successful.


# Define the string that contains all the special characters
special_characters = "`~!@#$%^&*()_-+={}[]:;\"'\"<,>.?/"


# create a function that returns True if a character in the given string is a number

def contains_number(str):
    for i in str:
        if i.isnumeric():
            return True
    return False

# create a function that returns True if a character in the given string is in Uppercase


def contains_upper(str):
    for i in str:
        if i.isupper():
            return True
    return False

# create a function that returns True if a character in the given string is in Lowercase


def contains_lower(str):
    for i in str:
        if i.islower():
            return True
    return False


# create a function that returns True if a character in the given string belongs to the set of special characters defined above
def contains_special(str):
    for i in str:
        if i in special_characters:
            return True

    return False


# Password strength calculator function that calls the above functions to calculate and return the strength score of the given password string

def check_password_strength(password):
    strength_score = 0

    if contains_number(password):
        strength_score += 5

    if contains_lower(password):
        strength_score += 2

    if contains_upper(password):
        strength_score += 3

    if contains_special(password):
        strength_score += 10

    return strength_score


if __name__ == "__main__":

    print(check_password_strength("DoT#2"))
