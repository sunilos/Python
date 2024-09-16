Here's a code snippet for creating a client socket in Python:

```python
# Example of Creating Client Socket
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import socket              

# Create a socket object
s = socket.socket()  
host = 'localhost'  # Server hostname or IP address
port = 12345        # Port to connect to

print(host, port)

# Connect to the server
s.connect((host, port))

# Send a message to the server
s.send(b'Hello Server')

# Receive a response from the server
res = s.recv(1024)  # Buffer size is 1024 bytes
msg = res.decode("utf-8")  # Decode bytes to string
print(msg)

# Close the socket
s.close()
```

### Key Points:
- **Socket Creation**: `socket.socket()` creates a new socket object.
- **Connection**: `s.connect((host, port))` connects the client to the server at the specified host and port.
- **Sending Data**: `s.send(b'Hello Server')` sends a message to the server. The message must be in bytes.
- **Receiving Data**: `s.recv(1024)` receives data from the server. The argument specifies the maximum amount of data to be received at once.
- **Decoding**: `res.decode("utf-8")` converts the received bytes object into a string.
- **Closing**: `s.close()` closes the socket connection.

Make sure that a server is running and listening on the specified host and port for the client to connect successfully.
