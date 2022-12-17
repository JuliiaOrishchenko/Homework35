import socket

HOST = "127.0.0.1"
PORT = 9091

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    s.sendto(b'Test message')
    