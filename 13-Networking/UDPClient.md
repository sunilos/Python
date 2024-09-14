Here's the code snippet for creating a UDP client socket in Python:

```python
# Example of Creating UDP Client Socket
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the host and port to connect to
udp_host = socket.gethostname()    # Host IP
udp_port = 12345                  # Specified port to connect

# Message to be sent to the server
msg = b'Hello Server!'

print("UDP target IP:", udp_host)
print("UDP target Port:", udp_port)

# Send the message to the server
sock.sendto(msg, (udp_host, udp_port))
```

### Key Points:
- **Socket Creation**: `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)` creates a UDP socket. `AF_INET` is used for IPv4 addresses, and `SOCK_DGRAM` specifies the socket type for UDP.
- **Message Preparation**: The message is created as a byte object (`b'Hello Server!'`).
- **Sending Data**: `sock.sendto(msg, (udp_host, udp_port))` sends the message to the specified host and port.

This UDP client will send a message to a server listening on the specified host and port. UDP is connectionless, so there is no need to establish a connection before sending data.