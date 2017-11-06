# Echo server program
import socket
import sys
# The remote host
# The same port as used by the server


HOST = None     # Symbolic name meaning all available interfaces
PORT = 50007    # Arbitrary non-privileged port 
s = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
   
    af, socktype, proto, canonname, sa = res
 
    #print('for: ', res)
    #print('af: ', af)
    #print('socktype: ', socktype)
    #print('proto: ', proto)
    #print('canonname: ', canonname)
    #print('sa: ', sa)
    
    try:
        print ('Creating Socket...')
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        print ('first except')
        s = None
        continue 
    try:
        print ('Binding...')
        s.bind(sa)
        print ('Listening...')
        s.listen(1)
    except socket.error as msg:
        print ('second except')
        s.close() 
        s = None 
        continue
    break
if s is None:
    print ('could not open socket')
    sys.exit(1)
print ('Accepting...')
conn, addr = s.accept() 
print ('Connected by', addr) 
    
while 1:
    data = conn.recv(1024) 
    if not data: 
        break 
    print('Client said: ', data.decode())
    conn.send(data)
conn.close()
