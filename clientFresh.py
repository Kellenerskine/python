import json
import socket
import pygame

pygame.font.init()

server = "192.168.0.106"
port = 5555
game_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
client_num = 0
my_turn = True
# TODO: make client constantly request updated list and turn_state until my_turn = True


height = 400
width = 900

# Define the background colour using RGB color coding.
background_colour = (0, 102, 0)

# Define the dimensions of screen object(width,height)
screen = pygame.display.set_mode((width, height))

# Set the caption of the screen
pygame.display.set_caption('Mancala Client')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

game_winner = 0
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

# redraws window -> while !my_turn ask if its my turn -> when my turn, get_game_state() -> redraw

top_row_color = (153, 0, 76)
bot_row_color = (102, 51, 0)
goal_color = (0, 51, 102)


def update_buttons():
    global btns
    btns = [Button(str(game_state[0]), center_x - 300, center_y, bot_row_color),
            Button(str(game_state[1]), center_x - 200, center_y, bot_row_color),
            Button(str(game_state[2]), center_x - 100, center_y, bot_row_color),
            Button(str(game_state[3]), center_x, center_y, bot_row_color),
            Button(str(game_state[4]), center_x + 100, center_y, bot_row_color),
            Button(str(game_state[5]), center_x + 200, center_y, bot_row_color),
            Button(str(game_state[6]), center_x + 300, center_y - 100, goal_color, 75, 150),
            Button(str(game_state[7]), center_x + 200, center_y - 100, top_row_color),
            Button(str(game_state[8]), center_x + 100, center_y - 100, top_row_color),
            Button(str(game_state[9]), center_x, center_y - 100, top_row_color),
            Button(str(game_state[10]), center_x - 100, center_y - 100, top_row_color),
            Button(str(game_state[11]), center_x - 200, center_y - 100, top_row_color),
            Button(str(game_state[12]), center_x - 300, center_y - 100, top_row_color),
            Button(str(game_state[13]), center_x - 425, center_y - 100, goal_color, 75, 150),
            ]


def redrawWindow(window):
    global client_num, my_turn
    loopy = 0
    pygame.display.set_caption(f"Mancala Client {client_num}")
    update_buttons()
    window.fill((128, 128, 128))
    font = pygame.font.SysFont("comicsans", 20)

    if client_num == 1:
        text = font.render("You are: ", 1, (0, 0, 0))
        text2 = font.render("brown", 1, (102, 51, 0))
        screen.blit(text, ((width / 2 - text.get_width() / 2) - 400, (height / 2 - text.get_height() / 2) - 150))
        screen.blit(text2, ((width / 2 - text.get_width() / 2) - 300, (height / 2 - text.get_height() / 2) - 150))
    if client_num == 2:
        text = font.render("You are: ", 1, (0, 0, 0))
        text2 = font.render("pink", 1, (153, 0, 76))
        screen.blit(text, ((width / 2 - text.get_width() / 2) - 400, (height / 2 - text.get_height() / 2) - 150))
        screen.blit(text2, ((width / 2 - text.get_width() / 2) - 300, (height / 2 - text.get_height() / 2) - 150))

    if not check_win():
        if my_turn:
            text = font.render("Your move", 1, (0, 102, 51))
            screen.blit(text, (width / 2 - text.get_width() / 2, (height / 2 - text.get_height() / 2) - 150))
        else:
            text = font.render("Opponent move", 1, (102, 0, 0))
            screen.blit(text, (width / 2 - text.get_width() / 2, (height / 2 - text.get_height() / 2) - 150))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        win_message = font.render("You Win!", 1, (0, 0, 0))
        lose_message = font.render("You Lose :(", 1, (0, 0, 0))
        if game_winner == 1:
            if client_num == 1:
                screen.blit(win_message, (
                (width / 2 - win_message.get_width() / 2), (height / 2 - win_message.get_height() / 2) - 150))
                pygame.display.update()
                pygame.time.delay(30000)
                pygame.quit()
            else:
                screen.blit(lose_message, (
                (width / 2 - lose_message.get_width() / 2), (height / 2 - lose_message.get_height() / 2) - 150))
                pygame.display.update()
                pygame.time.delay(30000)
                pygame.quit()
        elif game_winner == 2:
            if client_num == 2:
                screen.blit(win_message, (
                (width / 2 - win_message.get_width() / 2), (height / 2 - win_message.get_height() / 2) - 150))
                pygame.display.update()
                pygame.time.delay(30000)
                pygame.quit()
            else:
                screen.blit(lose_message, (
                (width / 2 - lose_message.get_width() / 2), (height / 2 - lose_message.get_height() / 2) - 150))
                pygame.display.update()
                pygame.time.delay(30000)
                pygame.quit()


    loopy += 1
    # else: text = their move


    for btn in btns:
        btn.draw(window)

    pygame.display.update()


# sending and receiving from server the initial game_state
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))


# data exchange below
def get_game_state():
    global game_state, my_turn, client_num
    start_msg = ["gimme", client_num]
    start_msg_json = json.dumps(start_msg)
    start_msg_json_bytes = start_msg_json.encode('utf-8')

    s.sendall(start_msg_json_bytes)

    data_from_server_encoded = s.recv(1024 * 2)
    data_from_server = json.loads(data_from_server_encoded.decode('utf-8'))

    game_state = data_from_server[0]
    client_num = data_from_server[1]


def my_turn_yet():
    global my_turn, client_num
    redrawWindow(screen)
    # constantly asking server if its my turn yet
    while not my_turn:
        if check_win():
            break
        msg = ["my_turn?", client_num]
        # print("client num: ", client_num)
        msg_json = json.dumps(msg)
        msg_json_bytes = msg_json.encode('utf-8')

        s.sendall(msg_json_bytes)

        turn_state_encoded = s.recv(1024 * 2)
        turn_state = json.loads(turn_state_encoded.decode('utf-8'))
        if turn_state == "yes":
            my_turn = True
        elif turn_state == "no":
            my_turn = False

            # print(f"{turn_state}, not your turn yet!")

    # redrawWindow(screen)


def my_turn_yet_single():
    global my_turn, client_num
    redrawWindow(screen)
    # constantly asking server if its my turn yet
    if not my_turn:
        msg = ["my_turn?", client_num]
        # print("client num: ", client_num)
        msg_json = json.dumps(msg)
        msg_json_bytes = msg_json.encode('utf-8')

        s.sendall(msg_json_bytes)

        turn_state_encoded = s.recv(1024 * 2)
        turn_state = json.loads(turn_state_encoded.decode('utf-8'))
        if turn_state == "yes":
            my_turn = True
        elif turn_state == "no":
            my_turn = False




def check_win():
    global game_winner
    if game_state[0] == 0 and game_state[1] == 0 and game_state[2] == 0 and game_state[3] == 0 and game_state[4] == 0 and game_state[5] == 0:
        for i in range(7, 13):
            game_state[13] += game_state[i]
            game_winner = 1
            return True
    elif game_state[7] == 0 and game_state[8] == 0 and game_state[9] == 0 and game_state[10] == 0 and game_state[11] == 0 and game_state[12] == 0:
        for i in range(0, 6):
            game_state[6] += game_state[i]
            game_winner = 2
            return True
    else:
        return False








def update_server_game_list():
    global game_state, my_turn
    # send game_state to server
    sending_game_state = [10, game_state]
    sending_game_state_json = json.dumps(sending_game_state)
    sending_game_state_json_bytes = sending_game_state_json.encode('utf-8')
    s.sendall(sending_game_state_json_bytes)

    updated_game_list_encoded = s.recv(1024 * 2)
    updated_game_list_reply = json.loads(updated_game_list_encoded.decode('utf-8'))

    # sets my_turn to false
    my_turn = False
    redrawWindow(screen)


def hole_chosen(hole):
    global my_turn

    marbles = game_state[hole]
    game_state[hole] = 0
    next_hole = hole + 1
    # avoid/enter end-goals
    while marbles > 0:
        if next_hole == 14:
            next_hole = 0
        if (next_hole == 6) and client_num == 2:
            # player 2 shouldn't score for player 1
            next_hole += 1
        elif (next_hole == 13) and client_num == 1:
            next_hole += 1
        else:
            game_state[next_hole] += 1
            next_hole += 1
            marbles -= 1


# Variable to keep game loop running
def click(btn):
    hole_chosen(btn)
    update_buttons()
    update_server_game_list()
    my_turn_yet()
    update_buttons()


def watch_buttons():
    my_turn_yet_single()
    for event in pygame.event.get():

        btn_counter = -1
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for btn in btns:
                btn_counter += 1
                if btn.click(pos):
                    print("clicked", my_turn)
                    if my_turn:
                        print(f"This is the button that was pressed: {btn_counter}")
                        print(f"marbles in button: {game_state[btn_counter]}")
                        # cannot click goals
                        if (
                                btn_counter == 0 or btn_counter == 1 or btn_counter == 2 or btn_counter == 3 or
                                btn_counter == 4 or btn_counter == 5) and (
                                btn_counter != 6 or btn_counter != 13):
                            if client_num == 1:
                                click(btn_counter)
                        elif (
                                btn_counter == 7 or btn_counter == 8 or btn_counter == 9 or btn_counter == 10 or
                                btn_counter == 11 or btn_counter == 12) and (
                                btn_counter != 6 or btn_counter != 13):
                            if client_num == 2:
                                click(btn_counter)
                    else:
                        break


def starting_positions():
    global my_turn
    if client_num == 1:
        my_turn = True
    if client_num == 2:
        my_turn = False

    print("my turn value: ", my_turn)


def main():
    global client_num
    # game loop
    running = True
    clock = pygame.time.Clock()
    loop_counter = 1
    client_num -= 1
    while running:
        clock.tick(60)
        get_game_state()
        if loop_counter == 1:
            starting_positions()
        loop_counter += 1

        redrawWindow(screen)
        watch_buttons()


        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


main()
