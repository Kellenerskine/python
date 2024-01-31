import json
import socket
import pygame

pygame.font.init()
# pygame.mixer.init()


height = 400
width = 900


# Define the background colour using RGB color coding.
background_colour = (0, 102, 0)

# Define the dimensions of screen object(width,height)
screen = pygame.display.set_mode((width, height))

# Set the caption of the screen
pygame.display.set_caption('Study Timer')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

game_winner = 0

#TODO: use this snippet for playing sounds
# def greeting(file):
#     greeting = pygame.mixer.Sound(file)
#     pygame.mixer.Sound.play(greeting)
#     pygame.mixer.music.stop()


class Button:
    def __init__(self, text, x, y, color, width=50, height=50):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255, 255, 255))
        window.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                           self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


center_x = width / 2
center_y = height / 2

btns = [Button("btn1", center_x - 300, center_y, (0, 0, 0)),
        Button("btn2", center_x, center_y, (0, 0, 0)),
        Button("btn3", center_x + 300, center_y, (0, 0, 0)),
        ]

# redraws window -> while !my_turn ask if its my turn -> when my turn, get_game_state() -> redraw

top_row_color = (153, 0, 76)
bot_row_color = (102, 51, 0)
goal_color = (0, 51, 102)


def update_buttons():
    global btns
    btns = [Button("btn1", center_x - 300, center_y, bot_row_color),
            Button("btn2", center_x, center_y, bot_row_color),
            Button("btn3", center_x + 300, center_y, bot_row_color),
            ]


def redrawWindow(window):
    loopy = 0

    update_buttons()
    window.fill((128, 128, 128))
    font = pygame.font.SysFont("comicsans", 20)

    text = font.render(f"Record:", 1, (0, 0, 0))
    screen.blit(text, ((width / 2 - text.get_width() / 2) - 400, (height / 2 - text.get_height() / 2) + 150))

    loopy += 1

    for btn in btns:
        btn.draw(window)

    pygame.display.update()


def click():
    update_buttons


def watch_buttons():
    for event in pygame.event.get():

        btn_counter = -1
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for btn in btns:
                btn_counter += 1
                if btn.click(pos):
                    print("clicked: ", btn)



def main():
    global client_num
    # game loop
    running = True
    clock = pygame.time.Clock()
    loop_counter = 1
    while running:
        clock.tick(60)
        loop_counter += 1

        redrawWindow(screen)
        watch_buttons()

        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


main()
