Here's the code snippet for creating a server socket in Python:

```python
# Example of Creating Server Socket
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import socket              # Import socket module
import datetime            # Import datetime module for timestamps

# Create a socket object
s = socket.socket()        
# Define the host and port
host = 'localhost'        
port = 12345              

# Bind the socket to the address and port
s.bind((host, port))       
# Listen for incoming connections
s.listen(5)              

print('Server started at', port)     

while True:
   # Accept a connection from a client
   c, addr = s.accept() 

   # Receive message from the client
   req = c.recv(1024) 
   print('Got from', addr, req.decode("utf-8"))

   # Prepare a response message with the current date and time
   dt = datetime.datetime.now()
   res = "Hello Client " + dt.strftime("%m/%d/%Y, %H:%M:%S")
   # Send the response to the client
   c.send(bytes(res, 'utf-8'))
   # Close the connection
   c.close()
```

### Key Points:
- **Socket Creation**: `socket.socket()` creates a new socket object.
- **Binding**: `s.bind((host, port))` binds the socket to a specific host and port.
- **Listening**: `s.listen(5)` sets the socket to listen for incoming connections, with a backlog of 5 connections.
- **Accepting Connections**: `c, addr = s.accept()` accepts an incoming connection from a client. `c` is the new socket object used for communication with the client, and `addr` is the client's address.
- **Receiving Data**: `c.recv(1024)` receives data from the client. The argument specifies the maximum amount of data to receive.
- **Sending Data**: `c.send(bytes(res, 'utf-8'))` sends a response to the client. The response message is encoded in bytes.
- **Closing**: `c.close()` closes the connection with the client.

This server will keep running and handling multiple client connections one at a time, sending a greeting message along with the current date and time to each connected client.
