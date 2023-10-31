import json
import socket
from _thread import *

# TODO: reset player_num
server = "192.168.0.106"
port = 5001

game_started = False
player_number = 1
turn_counter = 1

# game_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
game_state = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]

# server setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)
print("Server running, listening for connection...")


def threaded_client(conn, client_num, record, ip):
    global game_state, player_number
    global game_started, turn_counter
    game_started = True
    print(f"client number {client_num} has connected!")
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
                reply = encode_stuff([game_state, player_num, turn_counter, record])

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
                    msg = ["yes"]
                else:
                    msg = ["no", game_state]
                reply = encode_stuff(msg)

                conn.sendall(reply)
            elif data[0] == "going_again":
                game_state = data[1]
                reply = encode_stuff(f"go ahead! current SGS: {game_state}")

                conn.sendall(reply)
            elif data[0] == "i won":
                record_win(ip)
            elif data[0] == "i lost":
                pass
                record_loss(ip)

            else:
                pass
        except:
            break

    print("Lost connection")
    print("Closing connection")
    # close the connection
    # TODO: have not tested the line below
    player_number -= 1
    # game_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    game_state = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
    print(f"player num {player_number}")
    conn.close()
    # TODO:reset server player num var when people DC


def get_records(ipaddr):
    user_ip = ipaddr
    user_exists = False
    results = ""
    with open('records.txt', 'r') as f:
        file_data = f.readlines()

        for i in file_data:
            if i[0:13] == user_ip:
                results = str(i[-6:])
                user_exists = True

    if not user_exists:
        with open('records.txt', 'a') as f:
            f.write(f"\n{ipaddr}: 0W0L")
            results = "0W0L"

    return results


def record_loss(user_ip):
    line_count = 0
    f = open('records.txt', 'r')
    file_data = f.readlines()
    for i in file_data:
        if i[0:13] == user_ip:
            break
        else:
            line_count += 1
    f.close()

    f = open('records.txt', 'r+')
    file_data = f.readlines()
    file_as_list = list(file_data)

    f.close()

    z = open('records.txt', 'w').close()

    f = open('records.txt', 'r+')

    for i in file_as_list:
        if i[0:13] == user_ip:
            m = i.strip("\n")
            test = f"{m[0:17]}{str(int(m[17]) + 1)}{m[18]}\n"
            f.write(test)
        else:
            m = i.strip("\n")
            f.write(f"{m}\n")
    f.close()


def record_win(user_ip):
    line_count = 0
    f = open('records.txt', 'r')
    file_data = f.readlines()
    for i in file_data:
        if i[0:13] == user_ip:
            break
        else:
            line_count += 1
    f.close()

    f = open('records.txt', 'r+')
    file_data = f.readlines()
    file_as_list = list(file_data)

    f.close()

    z = open('records.txt', 'w').close()

    f = open('records.txt', 'r+')

    for i in file_as_list:
        if i[0:13] == user_ip:
            m = i.strip("\n")
            test = f"{m[0:15]}{str(int(m[15]) + 1)}{m[16:]}\n"
            f.write(test)
        else:
            m = i.strip("\n")
            f.write(f"{m}\n")
    f.close()


while True:
    conn, addr = s.accept()
    if game_started:
        player_number += 1

    records = get_records(addr[0])

    start_new_thread(threaded_client, (conn, player_number, records, addr[0]))
