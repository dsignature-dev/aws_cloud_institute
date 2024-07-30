# integer = 50
# string = "The number is"


# try:
#     expression = string + integer
# except:
#     print("Exception occured")
#     expression = string + str(integer)

# print(expression)


# def divide_numbers():

#     try:
#         dividend = int(input("Enter the integer to divide: "))
#         divisor = int(input("Enter the integer to divide by: "))
#         return (dividend/divisor)

#     except Exception as e:
#         print(type(e))
#         print(e)


# print(divide_numbers())


# def divide_numbers():

#     try:
#         dividend = int(input("Enter the integer to divide: "))
#         divisor = int(input("Enter the integer to divide by: "))
#         return (dividend/divisor)
#     except ValueError:
#         print("Enter an integer.")
#     except ZeroDivisionError:
#         print("Cannot divide by zero.")
#     except Exception as e:
#         print(type(e))
#         print(e)
#     else:
#         return (result)


# print(divide_numbers())


# try:
#     file = open("myfile.txt", "r")
#     # Perform some operations on the file
# except FileNotFoundError:
#     print("The file could not be found.")
# except IOError:
#     print("An error occurred while reading the file.")
# else:
#     print("File contents:", file.read())
# finally:
#     if 'file' in locals():
#         file.close()
#         print("File closed.")


# def create_profile(username, age):
#     """Creates dictionary with user details
#     and calls function to create homepage """
#     try:
#         if age < 13:
#             raise Exception("Account holders must be 13 or older.")
#         user_dict = {"name": username, "age": age}
#         print(user_dict)
#         create_homepage(user_dict)
#     except Exception as e:
#         print(e)


# create_profile("dina", 15)


def create_profile(username, age):
    """Creates dictionary with user details
    and calls function to create homepage """
    try:
        if age < 13:
            raise ValueError("Account holders must be 13 or older.")
        user_dict = {"name": username, "age": age}
        print(user_dict)
        create_homepage(user_dict)
    except Exception as e:
        print(type(e))
        print(e)


create_profile("dina", 5)
