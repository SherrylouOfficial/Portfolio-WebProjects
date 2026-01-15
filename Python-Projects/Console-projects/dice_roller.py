import random

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

#############horizontal output#################
for rays in range(5):
    for x in dice:
        print(dice_pic.get(x)[rays], end="")
    print()

for x in dice:
    total += x
# total will add all dice variables



print(f"Total: {total}")

