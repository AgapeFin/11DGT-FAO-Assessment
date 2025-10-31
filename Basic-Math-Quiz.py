

print("Welcome to the Basic Maths Quiz for Dummies!")


name = input("What is your name? ").strip()
while True:
    try:
        total_questions = int(input("How many questions would you like? "))
        if total_questions <= 0:
            print("Please enter a number that is greater then 0. ")
            continue
        break
    except ValueError:
        print("Please enter a valid number (no decimals). ")
