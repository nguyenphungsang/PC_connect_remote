import time
import socket
import sys
import os
s = socket.socket()
host = "172.0.0.1"
port = 8080
s.connect((host, port))
print("Connected to SV_PSN.")
command = s.recv(1024)
command = command.decode()
if command == "open":
    print("Command os :", command)
    s.send("Command received".encode())
    os.system('ls')