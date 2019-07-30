# Example of Creating UDP Client Socket
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#
 
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # For UDP

udp_host = socket.gethostname()		# Host IP
udp_port = 12345			        # specified port to connect

msg = b'Hello Server!'
print("UDP target IP:", udp_host)
print("UDP target Port:", udp_port)

sock.sendto(msg,(udp_host,udp_port))	
