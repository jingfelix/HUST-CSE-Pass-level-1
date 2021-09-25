# socket&tcp server
# client

import socket
import sys

# some variables
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
    sys.exit(1)

print('Socket Created')

try:
    # connect to host given
    s.connect((HOST,PORT))
except socket.error as e:
    PrintError(current_process='Connecting', msg=str(e))
    sys.exit(1)

print('Socket connected')

# message wanted to send
message = 'God created all things.'

try:
    # send message
    s.send(message.encode())
except socket.error as e:
    PrintError(current_process='Sending message', msg=str(e))
    sys.exit(1)

# receive message
reply = s.recv(4096)

print(reply.decode())

s.close()