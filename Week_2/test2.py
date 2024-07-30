 # Allow customers to order multiple cones or cups, with a different flavor possible for each scoop. 
 # If a customer enters an invalid option, notify them of the error and prompt them again. 
 
container = ("cone", "cups")
num_of_scoops = (1,2,3)
flavor = ("vanilla", "strawberry", "chocolate", "cherry", "mint", "peach", "grape")
orders = []
another_order = ''
 
  # Write a program that greets customers and takes their ice cream order. 
print("Welcome to the ice cream shop!")

# Allow customers to order multiple cones or cups, with a different flavor possible for each scoop. 
while True:
 
     while True: 
        answer = input("Would you like to place another order? (y/n):")
      if answer.lower() == 'y':
   another_order = 'y'
      break
     elif answer.lower() == 'n':\
         print("Thank you for your orders!")
  else:
   print("Invalid input. Please enter 'y" or 'no'."")
    
    
 if another_order == 'n':
     break