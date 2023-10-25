import socket
from _thread import *
import pickle


#server = "192.168.0.146" #rpi
server = "192.168.0.106" #macbook
#server = socket.gethostbyname(socket.gethostname()) #better way to get server IP
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

game_state_list = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
game_state = pickle.dumps(game_state_list)




def threaded_client(conn, p, gameId):
    global idCount
    # conn.send(str.encode(str(p)))
    # print(str(p))
    # print("\n")
    # print(str.encode(str(p)))

    conn.send(game_state)
    print(bytes(game_state_list))
    print("\n")
    print(game_state_list)



    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            #game_state_from_client =

            if gameId in games:
                game = games[gameId]

                if not data: #if nothing received disconnect
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))