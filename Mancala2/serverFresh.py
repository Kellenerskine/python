import json
import socket
from _thread import *
#TODO: reset player_num
server = "192.168.0.106"
port = 5050

game_started = False
player_number = 0

turn_counter = 1

game_state = [6, 5, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0]
#game_state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# server setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)
print("Server running, listening for connection...")


def threaded_client(conn, client_num):
    global player_number, game_state
    global game_started
    game_started = True
    print(f"client num: {client_num}")
    player_number = client_num
    player_number += 1

    while True:
        try:
            # data is exchanged
            encoded_data = conn.recv(1024 * 2)
            data = json.loads(encoded_data.decode('utf-8'))

            print(f"Client says: {data}")
            if not data:  # if no data is sent
                break
            if data == "gimme":
                # sending the client the game state and their player_number
                msg = [game_state, player_number]
                msg_json = json.dumps(msg)
                msg_json_bytes = msg_json.encode('utf-8')

                reply = msg_json_bytes
                conn.sendall(reply)
            elif data[0] == 10:
                game_state = data[1]
                msg = "Updated!"
                msg_json = json.dumps(msg)
                msg_json_bytes = msg_json.encode('utf-8')
                reply = msg_json_bytes
                conn.sendall(reply)
                print(f"game state after update: {game_state}")
            elif (data == "change"):
                if turn_counter == 1:
                    turn_counter = 2
                elif turn_counter == 2:
                    turn_counter = 1
                msg = "Updated!"
                msg_json = json.dumps(msg)
                msg_json_bytes = msg_json.encode('utf-8')
                reply = msg_json_bytes
                conn.sendall(reply)
                print(f"turn counter is: {turn_counter}, **************")
            else:
                pass

            #conn.sendall(reply)

        except:
            break

    print("Lost connection")
    try:
        print("Closing connection")
        # close the connection
    except:
        pass
    conn.close()
    #TODO:reset server player num var when people DC
    player_number = 0


while True:
    conn, addr = s.accept()
    if game_started:
        player_number += 1

    print(f"Connected to player {player_number} at: ", addr)

    start_new_thread(threaded_client, (conn, player_number))
