# PROJECT 1: PART 3 RECIEVER--- ES2
#*****************************************
#
# YOUR NAME: Megan Houchin and Victoria Pontikes
# NUMBER OF HOURS TO COMPLETE: 2 hours (please estimate how long this homework takes you to complete).
#*****************************************
#This script recieves the data sent from another microbit about the accerlerations in the x, y, and z directions at certain times and when
#logger is running as this program runs, it creates a CSV file containing these values
#import statements
import microbit as mb
import radio  # Needs to be imported separately

#main
radio.on()  # Turn on radio
radio.config(channel=14, length =100) #set to same channel as logger

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)

# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive() # Read from radio
    # Incoming is string sent from logger
    # Need to parse it and reformat as a tuple for the MU plotter
    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        cut = incoming.split(',')
        #putting in tuple
        thing0 = int(cut[0])/1000 #in seconds
        thing1 = int(cut[1])
        thing2 = int(cut[2])
        thing3 = int(cut[3])
        hold = (thing0, thing1, thing2, thing3)
        print(hold)
        mb.sleep(10)