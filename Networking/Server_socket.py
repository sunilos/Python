# Example of Creating Server Socket
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import socket			 

s = socket.socket()       
host = socket.gethostname() 
port = 12345               
s.bind((host, port))       
s.listen(5)                 
while True:
   c, addr = s.accept()    
   print('Got connection from', addr)
   c.send(b' Thank you for connecting')
   c.close() 
