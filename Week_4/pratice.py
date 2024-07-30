# class Employee:
#     employee_count = 0

#     def __init__(self, name, email, hire_date):
#         self.name = name
#         self.email = email
#         self.hire_date = hire_date
#         Employee.employee_count += 1

#         self.posts = []

#     def post(self, content):
#         new_post = content
#         self.posts.append(new_post)


# e1 = Employee("Mary Major", "mary.major@example.com", "07/12/2021")
# e1.post("hello")


# e2 = Employee("Dina", "d@gmail.com", "11/21/13")
# e2.post("byebye")

# print(e1.posts)
# print(e2.posts)


class BankAccount:

    def __init__(self, opening_deposit, account_number, account_balance=0):
        self.opening_deposit = opening_deposit
        self.account_number = account_number
        self.account_balance = account_balance

    def deposit(self, number):
        deposit_number = number
        self.account_balance += deposit_number

    def withdraw(self, number):
        withdraw_number = number
        self.account_balance -= withdraw_number

    def printTotal(self):
        print(self.account_balance)


b1 = BankAccount("$20", "12345")


# print(b1.account_balance)
b1.deposit(5)
b1.deposit(15)
b1.withdraw(2)
b1.withdraw(1)
b1.printTotal()

# print(b1.account_balance)
