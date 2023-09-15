#Created 09/14/2023
#Creator: Faa Diallo
#This is a UDP server that receives a message and echos it back to
#ths client. .
import socket

HOST = ""
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Listening on port {PORT} for packets.")
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Received some data from {addr}")
        if not data:
            break
        s.sendto(data, addr)
print("The message has been echoed")
