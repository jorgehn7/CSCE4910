#Server using AF_INET Family

import socket

HOST = '' # Symbolic name meaning all available interfaces 
PORT = 50007 # Arbitrary non-privileged port


#Creates a Socket for our server
sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Our socket will now bind at '' on 50007
sSocket.bind((HOST, PORT))


#Listens for conections
sSocket.listen(1)


#accept() returns a pair. (conn, address)
#conn is a new socket object usable to send and receive data on the connection
#address is the address bound to the socket on the other end of the connection.
conn, addr = sSocket.accept() 

print ('Connected by', addr) 


#Loops forever as long as we have data
temp = 0
while 1:
    
    #RECEIVES DATA IN BYTES
    data = conn.recv(1024) 
    if not data: 
        break 
    print('Client said: ', data.decode(), temp)
    
    #socketObject.sendall(bytes) //encode('utf-8') or just .encode() may be needed
    conn.sendall(data)
    temp = temp + 1
    
#Closes the socketObject connection
conn.close()
