# PROJECT 1: PART 3 LOGGER--- ES2
#*****************************************
#
# YOUR NAME: Megan Houchin and Victoria Pontikes
# NUMBER OF HOURS TO COMPLETE: 2 hours (please estimate how long this homework takes you to complete).
#*****************************************
#this script collects data about the microbit's acceraltions in the x, y, and z directions at specific times and sends them as a string to another microbit
#on the same channel using radio
#import statements
import microbit as mb
import radio

#main
radio.on()  # Turn on radio
radio.config(channel=14, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_b.is_pressed():  # wait for button B to be pressed to begin logging
    mb.sleep(10)

time0 = mb.running_time() #get the current running time
radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging


# Read and send accelerometer data repeatedly until button B is pressed again
while not mb.button_b.is_pressed():
    # Send the string of accelerometer and time measurements over the radio
    message = str(mb.running_time()-time0) + ', ' + str(mb.accelerometer.get_x()) + ', ' + str(mb.accelerometer.get_y()) + ', ' + str(mb.accelerometer.get_z())
    radio.send(message)
    mb.sleep(10)



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends