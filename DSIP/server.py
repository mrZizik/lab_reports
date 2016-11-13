# Python chat server-side
# by Ali Abdulmadzhidov 
# 13.11.16 23:27
import sys
import socket
import select
import time

HOST = '' 
SOCKETS = {}
logfile = None
SERVER_SOCKET = None
RECV_BUFFER = 4096 
PORT = 35535


def chat_server():
    global SERVER_SOCKET, LOGFILE
    SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    SERVER_SOCKET.bind((HOST, PORT))
    SERVER_SOCKET.listen(10)
    SOCKETS[SERVER_SOCKET] = "RaveServer"
    # LOGFILE = open('log'+str(time.time())+".log","w")
    print "Rave running on " + str(HOST) + ":" + str(PORT)
    # writeToLog("Rave running on " + str(HOST) + ":" + str(PORT))
    while 1:
        ready_to_read,ready_to_write,in_error = select.select(SOCKETS.keys(),[],[],0)
        for sock in ready_to_read:
            if sock == SERVER_SOCKET: 
                sockfd, addr = SERVER_SOCKET.accept()
                nickname = "Random"
                SOCKETS[sockfd] = nickname
                print "%s connected" % nickname
                broadcast(sockfd, "%s entered our rave\n" % nickname)
            else:
                try:
                    nickname = SOCKETS[sock]
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        print "%s" % data
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

# def writeToLog(message):
#     LOGFILE.write(message + "\n")


def getClientBySocket(sock):
    for client in CLIENTS:
        if client.sock == sock:
            return client
            break
        return None
 
if __name__ == "__main__":
    sys.exit(chat_server())





         