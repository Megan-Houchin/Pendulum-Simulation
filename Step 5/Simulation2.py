#Project 1 Part 5
#Numerical Simulation Model
#*****************************************
# YOUR NAME: Victoria Pontikes and Megan Houchin
# NUMBER OF HOURS TO COMPLETE: 2.5 hours
"""
Created on Sun Mar 22 14:03:04 2020

@author: Victoria
"""
#import statements
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.signal as sig

#global variables
length = 0.207 #0.270 .314 .3750 .413

#function definitions
def update_system(acc,pos,vel,time1,time2):
    #updates position, velocity, and acceleration based on timestep and old position, velocity, and acceleration values
    #takes 5 arguments, acceleration, position, velocity, time1 and time2
    #returns new position, new velocity, and new acceleration
    global length
    dt = time2-time1
    posNext = pos+vel*dt
    velNext = vel+acc*dt
    accNext = (-9.81/length)*math.sin(pos) 
    return posNext,velNext, accNext

def print_system(time,pos,vel):
    #function prints time, position, and velocity after every update
    #takes 3 arguments, time, position, and velocity
    #returns nothing
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel, "\n")

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


# initial conditions
pos = [-math.pi/4]
vel = [0]
acc = [0]
time = np.linspace(0,10,100000)


i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    posNext, velNext, accNext = update_system(acc[i-1],pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    acc.append(accNext)
    i += 1

#plots position, velocity, and acceleration vs time
plt.figure(1)
plt.plot(time, pos, 'r-')
plt.title('Position vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Position (radians)')

plt.figure(2)
plt.plot(time, vel, 'b-')
plt.title('Velocity vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Velocity (radians/seconds)')

plt.figure(3)
plt.plot(time, acc, 'g-')
plt.title('Acceleration vs Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acceleration (radians/seconds^2)')

plt.tight_layout()
plt.show()

#finds peaks of position function
pos_pks, _ = sig.find_peaks(pos)

#finds at what time y_pks occur and stores them in list count_y
#find_pks function returns list of imdices of peaks in y_filt, so we index
#y_pks to find time values where maximums occur
count_pos = []
for j in pos_pks:
        count_pos.append(time[j])

#finds and prints average period of pos wave        
period_pos = []
period(count_pos, period_pos)
print('The average y period is', end = ' ')
print(round(avg(period_pos), 2))
    