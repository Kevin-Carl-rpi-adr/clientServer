import socket   #for sockets
import sys  #for exit
 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
print ('Socket Created')
 
host = "192.168.1.14"
port = 1001

print ('Ip address ' + host)
 
#Connect to remote server
s.connect((host , port))
 
print ('Socket Connected to' + host)

theFirst = s.recv(512)
print (theFirst)
s.send('Hello, world')
data = s.recv(1024)
print 'Received', repr(data)
s.close()
