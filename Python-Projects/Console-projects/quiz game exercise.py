
questions = ("How many collections in are there? ",
             "What animal that lays the largest egg? ",
             "Other term of withering? ",
             "How many bones in the Human body? ",
             "Which planet is the coldest? ")

options = (("A. 3", "B. 2", "C. 5","D. 4"),
          ("A. Eagle", "B. Whale", "C. Ostrict","D. Chicken"),
          ("A. Recovery", "B. Blooming", "C. Breaking","D. Weakining"),
          ("A. 206", "B. 208", "C. 207","D. 209"),
          ("A. Mercury", "B. Mars", "C. Venus","D. Earth"))

answers = ("A","C","D","A","C")

suggestions = []
score = 0
num_questions = 0

print("------------------------------")
print("Please enter the right letter ")
for question in questions:
    print("------------------------------")

    print(question)
    for option in options[num_questions]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    suggestions.append(guess)
    if guess == answers[num_questions]:
        score += 1
        print("CORRECT ! ! !")
    else:
        print("INCORRECT ! ! ! ")
        print(f"{answers[num_questions]} is the Correct Answer . . .")
    num_questions += 1

print("------------------------------")
print("           RESULTS            ")
print("------------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in suggestions:
    print(guess, end=" ")
print()

score = score/ len(questions) * 100
print(f"Your Score is: {score}%")