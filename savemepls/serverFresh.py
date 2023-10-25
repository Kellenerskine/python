import json
import socket
from _thread import *
#TODO: reset player_num
server = "192.168.0.106"
port = 5050

player_number = 0

#game_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
game_state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# server setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)
print("Server running, listening for connection...")


def threaded_client(conn, client_num):

    reply = ""
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
                msg = [game_state, client_num]
                msg_json = json.dumps(msg)
                msg_json_bytes = msg_json.encode('utf-8')

                conn.sendall(msg_json_bytes)
            else:
                conn.sendall("wut u want?")

        except:
            break

    print("Lost connection")
    try:
        print("Closing connection")
        # close the connection
    except:
        pass
    player_number = 0
    conn.close()


while True:
    conn, addr = s.accept()
    print(f"Connected to player {player_number} at: ", addr)

    start_new_thread(threaded_client, (conn, player_number))
