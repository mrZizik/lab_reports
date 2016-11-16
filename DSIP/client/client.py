# Python chat client
# by Ali Abdulmadzhidov 
# 14.11.16 15:50
import sys
import socket
import select
 
def chatClient():
    host = raw_input("Host: ")
    port = 35535
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to the rave. You can start sending messages'
    sys.stdout.write('[Me] '); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]  
        read, write, error = select.select(socket_list , [], [])        
        for sock in read:            
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] '); sys.stdout.flush()     
            
            else :
                # user entered a message
                msg = sys.stdin.readline()
                if len(msg.strip())>0:
                    s.send(msg)
                sys.stdout.write('[Me] '); sys.stdout.flush() 

if __name__ == "__main__":
    sys.exit(chatClient())
