#Server UDP
import socket
import sys
import time

                                    #Creates UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#server_address is a 'Tuple' of 2 with values 'localhost' and 10000
server_address = ('localhost', 10000) 

print("starting up on %s port %s \n" %server_address)

message = 'Nothing much, Client. What up with you?'

#Bind the socket to the port
sock.bind(server_address)

'''
recv(size) returns the data received
as well as the address it was sent from.
Hence, 'data, address = sock.recvfrom(4096)'
'''
temp = ''
while (temp != 'Adios, Server'):
    data, address = sock.recvfrom(4096)
    temp = data.decode()
    
    print(data.decode())

    time.sleep(3)
    sock.sendto(message.encode(), address)
   
    time.sleep(1)
    sock.sendto('Bye, Client'.encode(), address)

print('Closing socket')
time.sleep(1)
sock.close()
