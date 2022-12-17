import socket

HOST = "127.0.0.1"
PORT = 9091


def caesar(message):
    result = ''
    for i in message:
        result += chr((i+1-97) % 26 + 97)
    return bytes(result, encoding="utf-8")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(caesar(data))
