import random
# ●, ┌, ─, ┐, │, └, ┘
#used as reference
#"┌─────────┐"
#"│         │"
#"│    ●    │"
#"│         │"
#"└─────────┘"

dice_pic = {
    1 : ("┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"),
    2 : ("┌─────────┐",
         "│ ●       │",
         "│         │",
         "│      ●  │",
         "└─────────┘"),
    3 : ("┌─────────┐",
         "│ ●       │",
         "│    ●    │",
         "│      ●  │",
         "└─────────┘"),
    4 : ("┌─────────┐",
         "│  ●   ●  │",
         "│         │",
         "│  ●   ●  │",
         "└─────────┘"),
    5 : ("┌─────────┐",
         "│  ●   ●  │",
         "│    ●    │",
         "│  ●   ●  │",
         "└─────────┘"),
    6 : ("┌─────────┐",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "└─────────┘"),

}

dice = []
total = 0


number_dice = int(input("Dice ? 1 to 6: "))

for x in range(number_dice):
    dice.append(random.randint(1, 6))

############verical output#####################
#for x in range(number_dice):
    #    for rays in dice_pic.get(dice[x]):
#        print(rays)
###############################################

#############horizontal output#################
for rays in range(5):
    for x in dice:
        print(dice_pic.get(x)[rays], end="")
    print()

for x in dice:
    total += x
# total will add all dice variables


print(f"Total: {total}")