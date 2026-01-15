import math
import random
import time
import pygame
pygame.init()

WIDTH, HEIGHT = 600, 400

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # DISPLAY POPUP
pygame.display.set_caption("Bubble Shooter")

COLOR = ["#fa8154", "#5b61b2", "#2f80e4", "#caa4ad", "#9dcb80"]

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30

BG_COLOR = (0, 25, 40)

LIVES = 10
TOP_BAR = 25

FONT_LABEL = pygame.font.SysFont("sobiscuit", 24)

# CIRCLE TARGETS
class Target:
    MAX_SIZE = 40
    GROWTH_RATE = 0.2
    scn_color = "#f1eae4"

    def __init__(self, x, y):  # POSITION AND SIZE
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
        self.color = random.choice(COLOR)

        self.rgb_color = self.hex_to_rgb(self.color)

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i + 2], 16) for i in range(0, 6, 2))

    def update(self):  # GROWTH OR SHRINKING
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    def draw(self, win): #CIRCLE SHAPE
        pygame.draw.circle(win, self.scn_color, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.rgb_color, (self.x, self.y), self.size * 0.9)
        pygame.draw.circle(win, self.scn_color, (self.x, self.y), self.size * 0.7)
        pygame.draw.circle(win, self.rgb_color, (self.x, self.y), self.size * 0.5)
        pygame.draw.circle(win, self.scn_color, (self.x, self.y), self.size * 0.3)
        pygame.draw.circle(win, self.rgb_color, (self.x, self.y), self.size * 0.2)
        pygame.draw.circle(win, self.scn_color, (self.x, self.y), self.size * 0.1)
        

    def collide(self, x, y):
        distance = math.sqrt((self.x - x) ** 2  + (self.y - y) ** 2)
        return distance <= self.size  

def draw(win, targets):
    win.fill(BG_COLOR)

    for target in targets:
        target.draw(win)


def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000 / 100))
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}:{milli}"

def status_bar(win, elasped_time, target_press, misses): 
    pygame.draw.rect(win, "#f1eae4", (0,0, WIDTH, TOP_BAR))
    time_label = FONT_LABEL.render(
        f"Time: {format_time(elasped_time)}", 1, "#f33f26")
    
    speed = round(target_press / elasped_time, 1) if elasped_time > 0 else 0
    speed_label = FONT_LABEL.render(f"Speed: {speed} t/s", 1, "black")
    hits_label = FONT_LABEL.render(f"Hits: {target_press}", 1, "black")
    lives_label = FONT_LABEL.render(f"Lives: {LIVES - misses}", 1, "black")
    
    win.blit(time_label, (5,5))
    win.blit(speed_label, (200,5))
    win.blit(hits_label, (350,5))
    win.blit(lives_label, (480,5))

def end_screen(win, elasped_time, target_press, clicks):
    win.fill(BG_COLOR)
    time_label = FONT_LABEL.render(
    f"Time: {format_time(elasped_time)}", 1, "white")
    
    speed = round(target_press / elasped_time, 1) if elasped_time > 0 else 0
    speed_label = FONT_LABEL.render(f"Speed: {speed} t/s", 1, "white")
    hits_label = FONT_LABEL.render(f"Hits: {target_press}", 1, "white")
    accuracy = round(target_press / clicks * 100, 1) if clicks > 0 else 0
    accuracy_label = FONT_LABEL.render(f"Accuracy: {accuracy}%", 1, "white")

    win.blit(time_label, (mid_position(time_label),100))
    win.blit(speed_label, (mid_position(speed_label),200))
    win.blit(hits_label, (mid_position(hits_label),300))
    win.blit(accuracy_label, (mid_position(accuracy_label),400))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()



def mid_position(surface): #END SCREEN TEXT SET TO CENTER 
    return WIDTH / 2 - surface.get_width() / 2

# MAIN LOOP OF THE GAME
def main():
    run = True
    targets = []
    clock = pygame.time.Clock()

    target_press = 0
    clicks = 0
    misses = 0
    start_time = time.time()
    
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:
        clock.tick(60)
        elasped_time = time.time() - start_time
        click = False
        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get(): #CLOSE PROGRAM WHEN X
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == TARGET_EVENT: #SIZE OF PYGAME PROGRAM
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN: #CLICK
                click =True 
                clicks += 1

        for target in targets: #SPAWN
            target.update()

            if target.size <= 0: #DISAPPEAR WHEN NO LONGER VISIBLE
                targets.remove(target)
                misses += 1

            if click and target.collide(*mouse_position): #POINTS AFTER CLICKING
                targets.remove(target)
                target_press += 1

        if misses >= LIVES:
            end_screen(WIN, elasped_time, target_press, clicks)

        draw(WIN, targets)
        status_bar(WIN, elasped_time, target_press, misses)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()