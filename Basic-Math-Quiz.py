import random

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


score = 0
history = []

for q_num in range(1, total_questions + 1):
    if choice == "5":
        op = random.choice(operations)
    else:
        op = operations[int(choice) - 1]

   
    a = random.randint(1, 12)
    b = random.randint(1, 12)

   
    if op == "-":
        if a < b:
            a, b = b, a
        correct = a - b
    elif op == "+":
        correct = a + b
    elif op == "×":
        correct = a * b
    elif op == "÷":
        
        correct = a
        a = a * b

    
    question = f"Q{q_num}: {a} {op} {b} = "
    while True:
        user_input = input(question)
        try:
            user_answer = float(user_input)
            break
        except ValueError:
            print("Please enter a valid number.")

    
    if abs(user_answer - correct) < 0.0001:
        print("Correct!\n")
        score += 1
        history.append((q_num, question.strip(), correct, user_answer, True))
    else:
        print(f"Incorrect. The correct answer was {correct}.\n")
        history.append((q_num, question.strip(), correct, user_answer, False))

