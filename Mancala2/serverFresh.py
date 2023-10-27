import json
import socket
from _thread import *

# TODO: reset player_num
server = "192.168.0.106"
port = 5555

game_started = False
player_number = 1

turn_counter = 1

#game_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
game_state = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]

# server setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)
print("Server running, listening for connection...")


def threaded_client(conn, client_num):
    global game_state
    global game_started, turn_counter
    game_started = True
    print(f"client num: {client_num}")
    player_num = client_num
    # player_num += 1

    while True:
        try:
            # data is exchanged
            encoded_data = conn.recv(1024 * 2)
            data = json.loads(encoded_data.decode('utf-8'))

            def encode_stuff(stuff):
                message = stuff
                message_json = json.dumps(message)
                message_json_bytes = message_json.encode('utf-8')
                return message_json_bytes

            if not data:  # if no data is sent
                break
            # client is asking for game state
            if data[0] == "gimme":
                #print(f"Client {data[1]} says: {data}")
                # sending the client the game state and their player_number
                reply = encode_stuff([game_state, player_num, turn_counter])

                conn.sendall(reply)
            # client is sending the updated game state
            elif data[0] == 10:
                print(f"Client says: {data}")
                game_state = data[1]
                reply = encode_stuff("Updated!")

                if turn_counter == 1:
                    turn_counter = 2
                elif turn_counter == 2:
                    turn_counter = 1

                conn.sendall(reply)
                print(f"game state after update: {game_state}")

            # client is asking if its their turn yet?
            elif (data[0] == "my_turn?"):
                # print(f"client says: {data}")
                if data[1] == turn_counter:
                    msg = "yes"
                else:
                    msg = "no"
                reply = encode_stuff(msg)

                conn.sendall(reply)

            else:
                pass

            # conn.sendall(reply)

        except:
            break

    print("Lost connection")
    try:
        print("Closing connection")
        # close the connection
    except:
        pass
    conn.close()
    # TODO:reset server player num var when people DC


while True:
    conn, addr = s.accept()
    if game_started:
        player_number += 1

    print(f"Connected to player {player_number} at: ", addr)

    start_new_thread(threaded_client, (conn, player_number))
