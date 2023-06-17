import socket
import threading

HEADER_LENGTH = 64
PORT = 5050
SERVER = '192.168.1.67'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'exit'

print(SERVER)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '*(HEADER_LENGTH - len(send_len))
    client.send(send_len)
    client.send(message)


while True:
    msg = input()
    send_message(msg)