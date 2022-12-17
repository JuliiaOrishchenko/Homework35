import socket

HOST = "127.0.0.1"
PORT = 9091

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

while True:
    try:
        result = s.recv(1024)
    except KeyboardInterrupt:
        s.close()
        break
    else:
        print('Message', result.decode('utf-8'))
