# Creating Tuples and lists 
questions = (("What is the color of sky?", 
              "What you can eat?",
              "What you can wear?",
              "How many bones does human body have?"))

options = (("A. Red", "B. Green", "C. Blue", "D. White"), 
           ("A. Banana", "B. Pajama", "C. Mic", "D. Book"),
           ("A. Pen", "B. Lighter", "C. Cable", "D. Kurta"),
           ("A. 106", "B. 206", "C. 345", "D. 523"))

answers = (("C", "A", "D", "B"))


guesses = []

# Creating a score variable
score = 0
# creating a counter for questions
q_num = 0


name = input("Enter your name: ")
print()
print(f"Hello {name}, Welcome to Quiz Game")


for question in questions:

    print("----------------")
    print(f"{q_num+1}. {question}")

    for option in options[q_num]:
        print(option)

    guess = input("Write the correct option: ").upper()
    guesses.append(guess)

    if guess == answers[q_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"The right answer is {answers[q_num]}")

    q_num = q_num + 1

print(q_num)
score = (score/q_num) * 100
score = int(score)

print("_____________")
print("|           |")
print("|   SCORE   |" ) 
print(f"|    {score}%    |")
print("|___________|")   
    




