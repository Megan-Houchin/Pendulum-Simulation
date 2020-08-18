#Project 1 Part 2
#Theoretical Period Calculations
#*****************************************
# YOUR NAMES: Victoria Pontikes and Megan Houchin
# NUMBER OF HOURS TO COMPLETE: 20 minutes

"""
Spyder Editor

This is a temporary script file.
"""
#import statements
import numpy as np
import math
import matplotlib.pyplot as plt

#function definitions
def period(L):
    #function that inputs a length and finds the period of it
    #takes one argument, length, and returns list of theoretically calculated periods
    g = 9.81
    T = 2*math.pi*(math.sqrt(L/g))
    periods.append(round(T,4))
    return periods

def graph():
    #function that graphs periods vs length
    #void function
    plt.figure(1)
    plt.plot(lengths, periods)
    plt.title('Periods (sec) vs Lengths (m)')
    plt.ylabel('Period (seconds)')
    plt.xlabel('Lengths (meters)')
    plt.show
    
    
#main code

#initializes lists
lengths = np.array([0.2070, 0.2710, 0.3140, 0.3750, 0.4130]) #lengths in meters
periods = [] #periods in seconds

#calls period function for each length in lengths list
for i in lengths:
    period(i)

print(periods)
#plots lengths vs periods
graph()

#Write a comment that explains the limits of this model

#The theoretical model is limited because it assumes that motion is frictionless and 
#that the 'string' or whatever tethers the pendulum to its rotational axis (in our
#case the Lego pieces) is massless. Additionally, this simulation assumes smooth, 
#2-dimensional motion when our pendulum moved in 3 dimensions and wobbled into the
#z-axis at times. This theoretical model is extremely simplified, and we would never
#see this in real life because of the constant random motion of particles and 
#because of the fact that everything has mass. If the friction and the mass
#were accounted for, the period would become smaller and smaller until the motion
#stopped because the pendulum begins to lose energy. The theoretical equation 
#does not account for this decrease in energy. Additionally, the numerical 
#values of the periods would be altered by assuming non-ideal motion, but the
#amount of change is dependent on the pendulum.








