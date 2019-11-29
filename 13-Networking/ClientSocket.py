# Example of Creating Client Socket
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import socket              

s = socket.socket()  # craete socket    
host = 'localhost'
#socket.gethostname()
port = 12345               
print (host,port)

s.connect((host, port))

s.send(b'Hello Server')
res = s.recv(1024) #byte object
msg = res.decode("utf-8") 
print(msg) 
s.close() 
