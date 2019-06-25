# Example of Creating Client Socket
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
s.connect((host, port))
print(s.recv(1024)) 
s.close()  
