import socket

HOST = "127.0.0.1"
PORT = 9091

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = b'Hello'
    s.sendall(message)
    data = s.recv(1024)

print(f"Received {data!r}")
