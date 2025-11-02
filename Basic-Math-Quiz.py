import random

print("Welcome to the Ultimate Basic Facts Quiz!")


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



print("\n QUIZ SUMMARY: ")
print(f"Well done, {name}! You got {score}/{total_questions} correct.")
percentage = round((score / total_questions) * 100, 1)
print(f"Your score: {percentage}%")



see_history = input("\nWould you like to see your quiz history? (yes/no): ").strip().lower()
if see_history in ["yes", "y"]:
    print("\nQUIZ HISTORY: ")
    for q_num, q_text, correct, user_ans, correct_flag in history:
        status = "Correct" if correct_flag else "Incorrect"
        print(f"{q_text} Your answer: {user_ans} \n Correct answer: {correct} \n {status}")

print("\nThanks for playing the Ultimate Basic Facts Quiz!")

