import json
import socket
from _thread import *

# TODO: reset player_num
server = "192.168.0.106"
port = 5001

game_started = False
player_number = 1
records = "4w6l"
turn_counter = 1

# game_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
game_state = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]

# server setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)
print("Server running, listening for connection...")


def threaded_client(conn, client_num):
    global game_state, player_number
    global game_started, turn_counter
    game_started = True
    print(f"client num: {client_num}")
    player_num = client_num

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
            elif data[0] == "my_turn?":
                if data[1] == turn_counter:
                    msg = "yes"
                else:
                    msg = "no"
                reply = encode_stuff(msg)

                conn.sendall(reply)

            else:
                pass
        except:
            break

    print("Lost connection")
    try:
        print("Closing connection")
        # close the connection
    except:
        pass
    # TODO: have not tested the line below
    player_number = 1
    conn.close()
    # TODO:reset server player num var when people DC

def get_records(ipaddr):
    user_ip = ipaddr
    user_exists = False
    with open('records.txt', 'r') as f:
        file_data = f.readlines()
        for i in file_data:
            print("stuff", (i[0:13]))
            if i[0:13] == user_ip:
                records = str(i[-4:])
                user_exists = True

    if not user_exists:
        with open('records.txt', 'a') as f:
            f.write(f"\n{ipaddr}: 1W0L")
            records = "0W0L"


while True:
    conn, addr = s.accept()
    if game_started:
        player_number += 1

    print(f"Connected to player {player_number} at: ", addr)
    print("records are: ", get_records(addr[0]))


    start_new_thread(threaded_client, (conn, player_number))
