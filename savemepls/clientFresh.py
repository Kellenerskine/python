import json
import socket
import pygame

server = "192.168.0.106"
port = 5050
game_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        window.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

def redrawWindow(window, client_num):
    window.fill((128,128,128))


    font = pygame.font.SysFont("comicsans", 60)
    text = font.render("Your Move", 1, (0, 255,255))
    window.blit(text, (80, 200))

    text = font.render("Opponents", 1, (0, 255, 255))
    window.blit(text, (380, 200))

    for btn in btns:
        btn.draw(window)

    pygame.display.update()

r = game_state[0]


btns = [Button(str(game_state), 50, 500, (0, 0, 0)),
        Button(str(game_state[1]), 150, 500, (0, 0, 0)),
        Button(str(game_state[2]), 150, 500, (0, 0, 0)),
        Button(str(game_state[3]), 150, 500, (0, 0, 0)),
        Button(str(game_state[4]), 150, 500, (0, 0, 0)),
        Button(str(game_state[5]), 150, 500, (0, 0, 0)),
        Button(str(game_state[6]), 150, 500, (0, 0, 0)),
        Button(str(game_state[7]), 150, 500, (0, 0, 0)),
        Button(str(game_state[8]), 150, 500, (0, 0, 0)),
        Button(str(game_state[9), 150, 500, (0, 0, 0))
        # Button(str(game_state[10]), 150, 500, (0, 0, 0)),
        # Button(str(game_state[11]), 150, 500, (0, 0, 0)),
        # Button(str(game_state[12]), 150, 500, (0, 0, 0)),
        ]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server, port))

    # data exchange below

    start_msg = "gimmo"
    start_msg_json = json.dumps(start_msg)
    start_msg_json_bytes = start_msg_json.encode('utf-8')

    s.sendall(start_msg_json_bytes)

    data_from_server_encoded = s.recv(1024 * 2)
    data_from_server = json.loads(data_from_server_encoded.decode('utf-8'))

    print(data_from_server)



# Define the background colour using RGB color coding.
background_colour = (234, 212, 252)

# Define the dimensions of screen object(width,height)
screen = pygame.display.set_mode((300, 300))

# Set the caption of the screen
pygame.display.set_caption('Geeksforgeeks')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running


def main():
    # game loop
    running = True

    while running:

        # for loop through the event queue
        for event in pygame.event.get():

            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

    # leaving the with block will auto leave the server
