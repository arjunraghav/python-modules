import socket
import threading

HEADER_LENGTH = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'exit'

print(SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'new connection {addr} connected')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER_LENGTH).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                break
            print(f'{addr} {msg}')
    conn.close()

def start():
    server.listen()
    print(f'listening from {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'active connections {threading.active_count() - 1}')

print('server starting')
start()