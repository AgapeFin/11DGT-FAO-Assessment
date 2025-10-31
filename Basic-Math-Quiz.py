
print("Welcome to the Basic Facts Quiz!")


name = input("What is your name? ").strip()
while True:
    try:
        total_questions = int(input("How many questions would you like? "))
        if total_questions <= 0:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a valid whole number.")
operations = ["+", "-", "×", "÷"]


print("\nChoose operation type:")
print("1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (×)\n4. Division (÷)\n5. Mixed")
while True:
    choice = input("Enter 1–5: ").strip()
    if choice in ["1", "2", "3", "4", "5"]:
        break
    else:
        print("Invalid choice. Try again.")
