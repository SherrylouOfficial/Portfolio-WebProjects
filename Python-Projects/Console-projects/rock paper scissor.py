import random
options = ("ROCK", "PAPER", "SCISSORS")
playing = True

print("________ROCK, PAPER, SCISSORS________")

while playing:
    user = None
    computer = random.choice(options)

    while user not in options:
        user = input("Enter any of the three: ").upper()
        
    print(f"Player: {user}")
    print(f"Computer: {computer}")

    if user == computer:
        print("It's a Tie ! ! !")
    elif user == "SCISSORS" and computer == "PAPER":
        print("You Win ! ! !")
    elif user == "ROCK" and computer == "SCISSORS":
        print("You Win ! ! !")
    elif user == "PAPER" and computer == "ROCK":
        print("You Win ! ! !")
    else:
        print("You Lose . . .")

    #retry = input("Play again ? (Y/N): ").upper()
    #if not retry == "Y":
        #playing = False
    #############shorter code###########
    if not input("Play Again ? (Y/N): ").upper() == "Y":
        playing = False

print()
print("Thanks for Playing !!")