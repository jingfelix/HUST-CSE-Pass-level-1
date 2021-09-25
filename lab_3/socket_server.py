# socket&tcp server
# server

import socket
import sys

HOST = '127.0.0.1'
PORT = 8000

def PrintError(current_process: str, msg: str)->None:
    print('Error!')
    print('Current process:' + current_process)
    print('Error message:' + msg)

try:
    # create object
    # AF_INET(IPV4) SOCK_STREAM(TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    PrintError(current_process='Creating socket', msg=str(e))
    sys.exit(0)

print('Socket created')

try:
    # bind and start to listen port
    s.bind((HOST, PORT))
except socket.error as e:
    PrintError(current_process='Binding', msg=str(e))

print('Bind succeed')

# backlog means connecting accounts
s.listen(5)

# addr-> ?:the address connecting with
# conn-> socket:
conn, addr = s.accept()

receive_data = conn.recv(4096)
print(receive_data.decode())

message = 'And human in their places'
conn.sendall(message.encode())

conn.close()
s.close()