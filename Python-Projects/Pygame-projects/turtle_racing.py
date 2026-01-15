import turtle
import time
import random


WIDTH, HEIGHT = 500, 500
COLORS = ['#9b82bc','#cb4a5f','#716965','#737f4b','#dcc57d','#374881','#51d1cb','#122830','#d45220','#a73a44']
COLOR_NAMES = {'#9b82bc' : 'Purple',
               '#cb4a5f' : 'Red',
               '#716965' : 'Brown',
               '#737f4b' : 'Olive',
               '#dcc57d' : 'Gold',
               '#374881' : 'Navy',
               '#51d1cb' : 'Teal',
               '#122830' : 'Dark Blue',
               '#d45220' : 'Orange',
               '#a73a44' : 'Marron'}

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ') 
        if racers.isdigit():
            racers = int(racers)
        else: 
            print('Input is not numeric. . . Please try again.')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Oops! Number is not in range of 2 - 10. Please try again.')

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return turtles.index(racer)
                

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, HEIGHT // -2 + 20) #position calculation of each racer
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Uma-Turtle-usume :D')

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)

colors = COLORS[:racers]

winner_index = race(colors)
winner_color = colors[winner_index]
winner_name = COLOR_NAMES[winner_color]
print(f"Winner: {winner_name} (Racer Num: {winner_index})")
time.sleep(5)