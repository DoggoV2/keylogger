#/bin/python

# i did this in like half an hour so the code might be messy.

# server side script

import socket
from string import ascii_letters
chars = ascii_letters

socket_family = socket.AF_INET
socket_type = socket.SOCK_STREAM

server = socket.socket(socket_family, socket_type, proto=0)

host = '127.0.0.1'
port = 54321
server.bind((host, port))

server.listen(2)

c, addr = server.accept()
print('connected')


def print_out():
   print(data)

data = []
try:
   switch = 0
   while switch == 0:
      log = str(c.recv(4096).decode('utf-8'))
      print(log)
      if log == '':
         switch += 1
      data.append(log)
except KeyboardInterrupt:
   print_out()

print_out()
