Here's the code snippet for creating a UDP server socket in Python:

```python
# Example of Creating UDP Server Socket
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
# 

import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the host and port to bind to
udp_host = socket.gethostname()    # Host IP
udp_port = 12345                  # Specified port to listen on

# Bind the socket to the host and port
sock.bind((udp_host, udp_port))

while True:
    print("Waiting for client...")
    # Receive data from the client
    data, addr = sock.recvfrom(1024)
    print("Received Message:", data.decode(), "from", addr)
```

### Key Points:
- **Socket Creation**: `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)` creates a UDP socket.
- **Binding**: `sock.bind((udp_host, udp_port))` binds the socket to the specified host and port so it can listen for incoming messages.
- **Receiving Data**: `data, addr = sock.recvfrom(1024)` waits for data from the client. The method returns the data and the address of the client.
- **Decoding**: `data.decode()` converts the received byte data into a string for display.

This UDP server listens indefinitely for incoming messages and prints the received messages along with the sender's address.
