from pass_module import check_password_strength


while True:

    password = input("Please enter a password ")
    score = check_password_strength(password)

    if score >= 20:
        print(f"Your password is strong ")
        break
    elif score == 4:
        print(f"Pass word is good but not strong enough")

    else:
        print("Password is not strong enough, please try again ")
