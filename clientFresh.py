import json
import socket
import pygame

server = "192.168.0.106"
port = 5050



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server, port))

    # data exchange below

    start_msg = "get_game_state"
    start_msg_json = json.dumps(start_msg)
    start_msg_json_bytes = start_msg_json.encode('utf-8')

    s.sendall(start_msg_json_bytes)

    data_from_server_encoded = s.recv(1024 * 2)
    data_from_server = json.loads(data_from_server_encoded.decode('utf-8'))

    print(data_from_server)





# Define the background colour
# using RGB color coding.
background_colour = (234, 212, 252)

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((300, 300))

# Set the caption of the screen
pygame.display.set_caption('Geeksforgeeks')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

# game loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False





# leaving the with block will auto leave the server
