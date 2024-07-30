"""
Using the Account class example from the beginning of the Week 4 module, define a child class that represents a savings account.  Provide a means for calculating the interest in the savings account and applying the interest to the balance.  Add a summary method that prints the details of the account on one line.

Write a program that processes a small number of accounts in a loop, applies interest where applicable, and prints the account summary.

Hint:  You may need to use the isinstance() method to determine which class you are working with.
"""


class Account:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def summary(self):
        return f"Account Number: {self.account_number} Balance: ${round(self.balance, 2)}"


a1 = Account("12345", "0")
print(a1.balance)


#  class BankAccount:

#     def __init__(self, opening_deposit, account_number, account_balance=0):
#         self.opening_deposit = opening_deposit
#         self.account_number = account_number
#         self.account_balance = account_balance

#     def deposit(self, number):
#         deposit_number = number
#         self.account_balance += deposit_number

#     def withdraw(self, number):
#         withdraw_number = number
#         self.account_balance -= withdraw_number

#     def printTotal(self):
#         print(self.account_balance)


# b1 = BankAccount("$20", "12345")


# # print(b1.account_balance)
# b1.deposit(5)
# b1.deposit(15)
# b1.withdraw(2)
# b1.withdraw(1)
# b1.printTotal()

# # print(b1.account_balance)
