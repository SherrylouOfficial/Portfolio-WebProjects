#this print random number 1-19#
#import random
#number = random.randint(0, 20)

#print(number)

###########################################

import random
lowest = 1
highest = 100
guesses = 0
number = random.randint(lowest, highest)

while True:
    guess = int(input(f"Enter a number between {lowest} and {highest}: "))
    guesses += 1

    if guess < number:
        print(f"{guess} is too low . . .")
    elif guess > number:
        print(f"{guess} is too high . . .")
    else:
        print("______________________________________")
        print(f"{guess} is the Right number ! ! !")
        break
print("______________________________________")
print(f"This round took you {guesses} tries")