#Created: 09/14/2023
#Creator: Faa Diallo
#Simple client to send a message to a UDP Server.
import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    msg = bytes(input("What message would you like to echo the server?\n"), "utf-8")
    s.sendto(msg, (HOST, PORT))
    data = s.recvfrom(1024)
    s.sendto(bytes("", "utf-8"), (HOST, PORT))

print(f"Received \"{data[0].decode('utf-8')}\"")

