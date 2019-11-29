# Example of Creating Server Socket
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import socket			  # Import socket module 
import datetime


s = socket.socket()        # Create a socket object
#host = socket.gethostname()   # Get local machine name
host = 'localhost'
port = 12345      
s.bind((host, port))       
s.listen(5)          
print('Server started at ', port)     

while True:
   c, addr = s.accept() #accept client  

   #receive client message 
   req = c.recv(1024) 
   print('Got from', addr, req.decode("utf-8"))

   #make response
   dt = datetime.datetime.now()
   res = "Hello Client " + dt.strftime("%m/%d/%Y, %H:%M:%S")
   c.send(bytes(res,'utf-8'))
   c.close()
