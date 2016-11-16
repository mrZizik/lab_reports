# Python chat server-side
# by Ali Abdulmadzhidov 
# 13.11.16 23:27
import sys
import socket
import select
import time
import hashlib
import random

nick1 = ("Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Gray", "Black", "White")
nick2 = ("Knight", "Alice", "Bob", "Eve", "Trudy", "Badman", "Harley", "Joker", "Pepe", "Clay")
HOST = '' 
SOCKETS = {}
logfile = None
SERVER_SOCKET = None
RECV_BUFFER = 4096 
PORT = 35535
PASSWORD = "b1eb218b924fcaf6f4689ed34e566484965ead698d0f324c3507044e09aab144" 


def chatServer():
    global SERVER_SOCKET
    SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    SERVER_SOCKET.bind((HOST, PORT))
    SERVER_SOCKET.listen(5)
    SOCKETS[SERVER_SOCKET] = ["RaveServer",0]
    print "Rave running on " + str(HOST) + ":" + str(PORT)
    while 1:
        read,write,error = select.select(SOCKETS.keys(),[],[],0)
        for sock in read:
            if sock == SERVER_SOCKET:
                sockfd, addr = SERVER_SOCKET.accept()
                nickname = nick1[random.randint(0, len(nick1)-1)] + " " + nick2[random.randint(0, len(nick2)-1)]
                SOCKETS[sockfd] = [nickname,0]
                broadcast(sockfd, "%s entered our rave\n" % nickname)
            else:
                try:
                    nickname = SOCKETS[sock][0]
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        if not checkPassword(sock, data) and not processCommands(sock,data):         
                            broadcast(sock, "\r" + nickname + ":" + data)
                    else:
                        if sock in SOCKETS.keys():
                            del SOCKETS[sock]
                            broadcast(sock, "%s is offline\n" % nickname) 
                except:
                    broadcast(sock, " %s is offline\n" % nickname)
                    continue
    SERVER_SOCKET.close()
    
def broadcast (sock, message):
    for socket in SOCKETS.keys():
        if socket != SERVER_SOCKET and socket != sock :
            try :
                socket.send(message)
            except:
                socket.close()
                if socket in SOCKETS.keys():
                    del SOCKETS[socket]

def send(sock, nickname, message):
    try:
        sock.send("\r" + nickname + ":" + message + "\n")
    except:
        sock.close()
        if socket in SOCKETS.keys():
            del SOCKETS[socket]

def checkPassword(sock, data):
    global SOCKETS
    if hashlib.sha256(data).hexdigest() == PASSWORD:
        SOCKETS[sock][1] = 1
        send(sock, SOCKETS[SERVER_SOCKET][0] ,"Admin access granted")
        return True
    return False


def processCommands(sock, data):
    if "listall" == data.strip():
        message = ""
        for s in SOCKETS:
            if sock == s:
                message+= "(You)"
            if SOCKETS[s][1]:
                message+= "[ADMIN]"
            message += SOCKETS[s][0] + "\n"
        message = message[:len(message)-1]
        send(sock, SOCKETS[SERVER_SOCKET][0] , "\n" + message)
        return True
    if "exit" == data.strip():
        sock.close()
        del SOCKETS[sock]
    if SOCKETS[sock][1] == 1 and "kick" in data:
        nickname = data[5:]
        kickUser(nickname)
        return True
    return False


def kickUser(nick):
    for sock in SOCKETS:
        if SOCKETS[sock][0] == nick.strip() and sock != SERVER_SOCKET:
            broadcast(None, SOCKETS[sock][0] + " was kicked by Admin< \n")
            sock.close()
            del SOCKETS[sock]
 
if __name__ == "__main__":
    sys.exit(chatServer())





         