
#Project 1 Part 4
#Experimental Period Calculations
#*****************************************
# YOUR NAME: Victoria Pontikes and Megan Houchin
# NUMBER OF HOURS TO COMPLETE: 5 hours

#NOTE: to plot other experimental data from other lengths, change the fin file

"""
Created on Tue Mar 31 20:01:10 2020

@author: Victoria
"""

#import statements
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.signal as sig
import os
path = "C:/Users/Victoria/Documents/GitHub/project-1-megan-and-tori/Step 4"
os.chdir(path)

#function definitions
def period(count,list):
    #function that finds the difference between each of its values and appends that difference to a blank list
    #takes two arguments, count list and blank list, and returns the filled in list
    #this is used to calculate period because our count list stores the time values that all our peaks occur at
    for i in range(len(count)):
        if i+1 >= len(count):
            break
        else:
            diff = abs(count[i+1] - count[i])
            list.append(diff)
    return list
        
def avg(list):
    #function averages all the components of a list
    #takes one argument, list, and returns average of all the values in the list
    add = 0
    for i in list:
        add = add + i
    return add/(len(list))

def find_angle_from_horizontal(list):
    #function finds the angle from the horizontal based on the x accel, y accel, and z accel
    #takes one argument, a list with all accel values, and returns nothing
    #appends values found in theta to blank list
    #due to our microbit orientation, the horizontal is dependent on y so all calculations will be based on y
    acc_x = float(list[1])
    acc_y = float(list[2])
    acc_z = float(list[3])
    top = acc_y 
    #the equation has the y acceleration on the top, and we are going to index a list with all the original values to find y accel
    #since the original list is [time, x accel, y accel, z accel], we index accordingly
    bottom = math.sqrt((acc_x)**2 +(acc_z)**2)
    tilt_angle = math.atan2(top, bottom)
    tiltY = (tilt_angle * 180) / math.pi
    theta.append(tiltY)
    #blank list theta is initialized above the function call
    

fin = open('length 1.csv',"r") #this is changed for each length

#main code

#initializing lists
timez = []
x_accel = []
y_accel = []
z_accel = []
theta = []

for ln in fin: 
    #putting data into 4 lists (time, x accel, y accel, z accel)
    temp1 = ln.strip()
    temp = ln.split(',')
    timez.append(float(temp[0]))
    x_accel.append(float(temp[1]))
    y_accel.append(float(temp[2]))
    z_accel.append(float(temp[3]))
    
    #finding angle from horizontal at every time
    find_angle_from_horizontal(temp) 

fin.close()


#apply median filter to all waves
x_filt = sig.medfilt(x_accel)
y_filt = sig.medfilt(y_accel)
z_filt = sig.medfilt(z_accel)
          
            
#plot waves of accelerations vs time
plt.figure(1)
plt.plot(np.array(timez), np.array(x_filt,), 'r-')
plt.title('X Acceleration vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('X Acceleration (meters^2/second)')

plt.figure(2)
plt.plot(np.array(timez), np.array(y_filt), 'g-')
plt.title('Y Acceleration vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Y Acceleration (meters^2/second)')

plt.figure(3)
plt.plot(np.array(timez), np.array(z_filt), 'b-')
plt.title('Z Acceleration vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Z Acceleration (meters^2/second)')

#plots theta vs time
plt.figure(4)
plt.plot(np.array(timez), np.array(theta), 'r-')
plt.title('Theta vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Theta (degrees)')

plt.tight_layout()
plt.show()


#find peaks of y wave since y is the direction of motion
#NOTE: height and distance varies based on data (and false peaks in data)
y_pks, _ = sig.find_peaks(y_filt, height = 60, distance = 20)

#finds at what time y_pks occur and stores them in list count_y
#find_pks function returns list of imdices of peaks in y_filt, so we index
#y_pks to find time values where maximums occur
count_y = []
for j in y_pks:
        count_y.append(timez[j])

#finds and prints average period of y wave        
period_y = []
period(count_y, period_y)
print('The average y period is', end = ' ')
print(round(avg(period_y), 2))

    