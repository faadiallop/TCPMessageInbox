#Created 09/14/2023
#Creator: Faa Diallo
#This is a TCP server that receives a message and echos it back to
#ths client. After that it closes the connection.
import socket

HOST = ""
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print(f"Listening on port {PORT} for packets.")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
print("The message has been echoed")
