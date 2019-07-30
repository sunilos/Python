# Example of Creating Server Socket
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import socket			  # Import socket module 

s = socket.socket()        # Create a socket object
host = socket.gethostname()   # Get local machine name
port = 12345               # Reserve a port for your service.
s.bind((host, port))       
s.listen(5)                 
while True:
   c, addr = s.accept()    
   print('Got connection from', addr)
   c.send(b'Thank you for connecting')
   c.close()
