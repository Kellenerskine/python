import json
import socket
import pygame
pygame.font.init()

server = "192.168.0.106"
port = 5050
game_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
client_num = 0

height = 400
width = 900

# Define the background colour using RGB color coding.
background_colour = (234, 212, 252)

# Define the dimensions of screen object(width,height)
screen = pygame.display.set_mode((width, height))

# Set the caption of the screen
pygame.display.set_caption('Mancala Client')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

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
        text = font.render(self.text, 1, (255,255,255))
        window.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

def redrawWindow(window):
    window.fill((128,128,128))



    font = pygame.font.SysFont("comicsans", 20)
    # if your move:
    text = font.render("Your move", 1, (255, 0, 0))
    #else: text = their move
    screen.blit(text, (width / 2 - text.get_width() / 2, (height / 2 - text.get_height() / 2) - 150))


    for btn in btns:
        btn.draw(screen)

    pygame.display.update()

def hole_chosen():
    pass




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server, port))

    # data exchange below

    start_msg = "gimme"
    start_msg_json = json.dumps(start_msg)
    start_msg_json_bytes = start_msg_json.encode('utf-8')

    s.sendall(start_msg_json_bytes)

    data_from_server_encoded = s.recv(1024 * 2)
    data_from_server = json.loads(data_from_server_encoded.decode('utf-8'))

    game_state = data_from_server[0]
    client_num = data_from_server[1]


    print(f"server sent: {data_from_server}")


center_x = width / 2
center_y = height / 2


btns = [Button(str(game_state[0]), center_x - 300, center_y - 100, (0, 0, 0)),
        Button(str(game_state[1]), center_x - 200, center_y - 100, (0, 0, 0)),
        Button(str(game_state[2]), center_x - 100, center_y - 100, (0, 0, 0)),
        Button(str(game_state[3]), center_x, center_y - 100, (0, 0, 0)),
        Button(str(game_state[4]), center_x + 100, center_y - 100, (0, 0, 0)),
        Button(str(game_state[5]), center_x + 200, center_y - 100, (0, 0, 0)),
        Button(str(game_state[6]), center_x + 300, center_y - 100, (0, 0, 0), 75, 150),
        Button(str(game_state[7]), center_x + 200, center_y, (0, 0, 0)),
        Button(str(game_state[8]), center_x + 100, center_y, (0, 0, 0)),
        Button(str(game_state[9]), center_x, center_y, (0, 0, 0)),
        Button(str(game_state[10]), center_x - 100, center_y, (0, 0, 0)),
        Button(str(game_state[11]), center_x - 200, center_y, (0, 0, 0)),
        Button(str(game_state[12]), center_x - 300, center_y, (0, 0, 0)),
        Button(str(game_state[13]), center_x - 425, center_y - 100, (0, 0, 0), 75, 150),
        ]



# Variable to keep our game loop running


def main():
    # game loop
    running = True

    while running:

        redrawWindow(screen)



        # for loop through the event queue
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            btn_counter = -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    btn_counter += 1
                    if btn.click(pos):
                        #TODO:check to make sure its that client's turn
                        if True:
                            print(f"This is the button that was pressed: {btns[btn_counter].text}")
                            print(game_state[btn_counter])



    # leaving the with block will auto leave the server

main()
