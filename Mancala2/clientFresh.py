import json
import socket
import pygame

pygame.font.init()

server = "192.168.0.106"
port = 5555
#game_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
client_num = 0
my_turn = True
#TODO: make client constantly request updated list and turn_state until my_turn = True



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


def redrawWindow(window):

    window.fill((128, 128, 128))

    font = pygame.font.SysFont("comicsans", 20)
    if my_turn:
        text = font.render("Your move", 1, (0, 200, 10))
    else:
        text = font.render("Opponent move", 1, (255, 0, 0))
    # else: text = their move
    screen.blit(text, (width / 2 - text.get_width() / 2, (height / 2 - text.get_height() / 2) - 150))

    for btn in btns:
        btn.draw(window)

    pygame.display.update()


#sending and receiving from server the initial game_state
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))


# data exchange below
def get_game_state():
    global game_state, my_turn, client_num
    start_msg = "gimme"
    start_msg_json = json.dumps(start_msg)
    start_msg_json_bytes = start_msg_json.encode('utf-8')

    s.sendall(start_msg_json_bytes)

    data_from_server_encoded = s.recv(1024 * 2)
    data_from_server = json.loads(data_from_server_encoded.decode('utf-8'))

    game_state = data_from_server[0]
    client_num = data_from_server[1]

    if client_num == 1:
        my_turn = True
    else:
        my_turn = False

    print(f"server sent: {data_from_server}")

#gets the initial game state from server
get_game_state()

# auto-closes connection
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
def my_turn_yet():
    global my_turn
    redrawWindow(screen)
    #constantly asking server if its my turn yet
    while my_turn == False:
        msg = ["my_turn?", client_num]
        msg_json = json.dumps(msg)
        msg_json_bytes = msg_json.encode('utf-8')

        s.sendall(msg_json_bytes)

        turn_state_encoded = s.recv(1024 * 2)
        turn_state = json.loads(turn_state_encoded.decode('utf-8'))
        if turn_state == "yes":
            my_turn = True
        else:
            pass
            #print(f"{turn_state}, not your turn yet!")

    get_game_state()



def change_turn():
    global my_turn
    if my_turn == False:
        my_turn = True
    else:
        my_turn = False

    sending_turn_change = "change"
    sending_turn_change_json = json.dumps(sending_turn_change)
    sending_turn_change_json_bytes = sending_turn_change_json.encode('utf-8')
    s.sendall(sending_turn_change_json_bytes)

    turn_change_conf_encoded = s.recv(1024 * 2)
    print("here")
    turn_change_conf = json.loads(turn_change_conf_encoded.decode('utf-8'))
    print(f"turn change conf: {turn_change_conf}")
    my_turn_yet()


def check_win():
    pass

def update_server_game_list():
    global game_state
    # send game_state to server
    sending_game_state = [10, game_state]
    sending_game_state_json = json.dumps(sending_game_state)
    sending_game_state_json_bytes = sending_game_state_json.encode('utf-8')
    s.sendall(sending_game_state_json_bytes)

    updated_game_list_encoded = s.recv(1024 * 2)
    updated_game_list_confirmation = json.loads(updated_game_list_encoded.decode('utf-8'))
    print(f"updated game list: {updated_game_list_confirmation}")

    change_turn()



center_x = width / 2
center_y = height / 2

btns = [Button(str(game_state[0]), center_x - 300, center_y, (0, 0, 0)),
        Button(str(game_state[1]), center_x - 200, center_y, (0, 0, 0)),
        Button(str(game_state[2]), center_x - 100, center_y, (0, 0, 0)),
        Button(str(game_state[3]), center_x, center_y, (0, 0, 0)),
        Button(str(game_state[4]), center_x + 100, center_y, (0, 0, 0)),
        Button(str(game_state[5]), center_x + 200, center_y, (0, 0, 0)),
        Button(str(game_state[6]), center_x + 300, center_y - 100, (0, 0, 0), 75, 150),
        Button(str(game_state[7]), center_x + 200, center_y - 100, (0, 0, 0)),
        Button(str(game_state[8]), center_x + 100, center_y - 100, (0, 0, 0)),
        Button(str(game_state[9]), center_x, center_y - 100, (0, 0, 0)),
        Button(str(game_state[10]), center_x - 100, center_y - 100, (0, 0, 0)),
        Button(str(game_state[11]), center_x - 200, center_y - 100, (0, 0, 0)),
        Button(str(game_state[12]), center_x - 300, center_y - 100, (0, 0, 0)),
        Button(str(game_state[13]), center_x - 425, center_y - 100, (0, 0, 0), 75, 150),
        ]

def update_buttons():
    global btns
    btns = [Button(str(game_state[0]), center_x - 300, center_y, (0, 0, 0)),
            Button(str(game_state[1]), center_x - 200, center_y, (0, 0, 0)),
            Button(str(game_state[2]), center_x - 100, center_y, (0, 0, 0)),
            Button(str(game_state[3]), center_x, center_y, (0, 0, 0)),
            Button(str(game_state[4]), center_x + 100, center_y, (0, 0, 0)),
            Button(str(game_state[5]), center_x + 200, center_y, (0, 0, 0)),
            Button(str(game_state[6]), center_x + 300, center_y - 100, (0, 0, 0), 75, 150),
            Button(str(game_state[7]), center_x + 200, center_y - 100, (0, 0, 0)),
            Button(str(game_state[8]), center_x + 100, center_y - 100, (0, 0, 0)),
            Button(str(game_state[9]), center_x, center_y - 100, (0, 0, 0)),
            Button(str(game_state[10]), center_x - 100, center_y - 100, (0, 0, 0)),
            Button(str(game_state[11]), center_x - 200, center_y - 100, (0, 0, 0)),
            Button(str(game_state[12]), center_x - 300, center_y - 100, (0, 0, 0)),
            Button(str(game_state[13]), center_x - 425, center_y - 100, (0, 0, 0), 75, 150),
            ]



def hole_chosen(hole):
    # TODO: if clicked empty hole blit: "empty hole clicked"
    print(f"client number: {client_num}")

    marbles = game_state[hole]
    game_state[hole] = 0
    next_hole = hole + 1
    # TODO: avoid/enter endgoals
    while marbles > 0:
        if (next_hole == 6) and client_num == 2:
            # player 2 shouldn't score for player 1
            next_hole += 1
        elif (next_hole == 13) and client_num == 1:
            next_hole += 1
        else:
            game_state[next_hole] += 1
            next_hole += 1
            marbles -= 1

        if (next_hole == 6) and (client_num == 1) and marbles == 1:
            #reset turn
            change_turn()
        if (next_hole == 13) and (client_num == 2) and marbles == 1:
            change_turn()


    print(f"this is current game state: {game_state}")
    update_buttons()
    update_server_game_list()



# Variable to keep our game loop running


def main():
    # game loop
    running = True
    patience_counter = 0
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        if my_turn:
            pass


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
                        # TODO:check to make sure its that client's turn
                        if my_turn:
                            print(f"This is the button that was pressed: {btn_counter}")
                            print(f"marbles in button: {game_state[btn_counter]}")
                            hole_chosen(btn_counter)
                        else:
                            patience_counter += 1
                            # print(f"patience tested x{patience_counter}")
                            # font = pygame.font.SysFont("comicsans", 50)
                            # text = font.render("Not your turn!", 1, (200, 0, 200))
                            # screen.blit(text, (width / 2 - text.get_width() / 2, (height / 2 - text.get_height() / 2)))
                            # redrawWindow(screen)
                            # pygame.display.flip()

        redrawWindow(screen)



    # leaving the with block will auto leave the server

main()
