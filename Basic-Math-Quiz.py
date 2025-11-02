import random

## BASIC FACTS QUIZ ##

print("Welcome to the Ultimate Basic Facts Quiz!")

# Get user name and number of questions
while True:
    name = input("What is your name? ").strip()
    if len(name) == 0:
        print("Please enter your name! (it can’t be blank).")
    elif len(name) > 15:
        print("That name is too long! Please use 15 characters or fewer.")
    else:
        break

while True:
    try:
        total_questions = int(input("How many questions would you like? "))
        if total_questions <= 0:
            print("\nPlease enter a number greater than 0.\n") # If user attempts to enter a number below 1, loops script.
            continue
        elif total_questions > 50:
            print("\nThat is too many questions.\n") # If user attempts to enter a number above 50, loops script.
            continue
        break
    except ValueError:
        print("\nPlease enter a valid whole number.\n") # If user enters decimal or unrecognized symbol, loop script, gives this message.

operations = ["+", "-", "×", "÷"]

# Let the user choose the operation type or mixed all together
print("\nChoose operation type:")
print("1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (×)\n4. Division (÷)\n5. Mixed")
while True:
    choice = input("Enter 1–5: ").strip()
    if choice in ["1", "2", "3", "4", "5"]:
        break
    else:
        print("Invalid choice. Try again.") # if user enters an unrecognized symbol, loops script and gives this message.

## MAIN QUIZ LOOP ##

#Variables
score = 0
history = [] # Used for later when user asks for quiz history

for q_num in range(1, total_questions + 1):
    if choice == "5":
        op = random.choice(operations)
    else:
        op = operations[int(choice) - 1]

# Chooeses a random number between 1 - 12 to ensure randomized questions.   
    a = random.randint(1, 12)
    b = random.randint(1, 12)

# Many Fixes here just in case questions could be negative or not an integer   
    if op == "-":
        if a < b:
            a, b = b, a # swap values if subtraction questions tries to give a negative.
        correct = a - b
    elif op == "+":
        correct = a + b
    elif op == "×":
        correct = a * b
    elif op == "÷":
        
        correct = a 
        a = a * b # Make a equal to itself multiplied by b to avoid a being a decimal but an integer!

# Asks user to enter their number    
    question = f"Q{q_num}: {a} {op} {b} = "
    while True:
        user_input = input(question)
        try: # Fixed here where user can not enter a letter, decimal or unrecognized symbol. (line 64 - 68)
            user_answer = float(user_input)
            break
        except ValueError:
            print("Please enter a valid number.") # If user attempts to input a letter or unrecognized symbol, loop script and give this message.

 # Adds up the score here if user gets answer correct.   
    if abs(user_answer - correct) < 0.0001:
        print("Correct!\n")
        score += 1
        history.append((q_num, question.strip(), correct, user_answer, True)) #Append here for quiz history at the end.
    else:
        print(f"Incorrect. The correct answer was {correct}.\n")
        history.append((q_num, question.strip(), correct, user_answer, False)) #Append here for quiz history at the end.


## Quiz SUMMARY ##
print("\n QUIZ SUMMARY: ")
print(f"Well done, {name}! You got {score}/{total_questions} correct.")
percentage = round((score / total_questions) * 100, 1) # Formula to convert answered questions to a percentage.
print(f"Your score: {percentage}%")


## Quiz HISTORY ##
while True:    
    see_history = input("\nWould you like to see your quiz history? (yes/no): ").strip().lower()
    
    
    if see_history in ["yes", "y"]:
        print("\nQUIZ HISTORY: ")
        for q_num, q_text, correct, user_ans, correct_flag in history:
            status = "Correct" if correct_flag else "Incorrect"
            print(f"{q_text} Your answer: {user_ans} \n Correct answer: {correct} \n {status}") # If user puts 'yes', show quiz history of corrects and incorrects.
            print("\n\nThank you for playing the Ultimate Basic Facts Quiz!")
        break

    elif see_history in ["no", "n"]:
        print("\nNo problem! Thanks for playing the Ultimate Basic Facts Quiz!") # If user puts 'no', end whole script and send a last message.
        break

    else:
        print("Please type 'yes' or 'no'.") # If user tries to input a number or any unrecognized symbol, loop script and send this message.

