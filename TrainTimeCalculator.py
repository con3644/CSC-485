#Max Conroy; Jordan Westfall; Andrew Weaver
#CSC 485; Program 1- Train Problem
#Group 2

#User enters data and program calculates time that trains will meet based on the data entered

import datetime
from datetime import timedelta

# Print welcome messages
print("=================================")
print("  Train Time Calculator Program  ")
print("=================================")
    
# City names    
city1=input('Enter the name of the first city: ')
city2=input('Enter the name of the second city: ')
    
# Distance between cities    
distance=input("Enter the distance between "+city1+" and "+city2+" (miles): ")

# Train 1 information
t1time=input("Enter the time that the first train left " + city1 +" (hh:mm:ss): ")
t1speed=input("Enter the speed of the train that left " + city1 + " (mph): ")
   
# Train 2 Information
t2time=input("Enter the time that the second train left " + city1 + " (hh:mm:ss): ")
t2speed=input("Enter the speed of the train that left " + city1+ " (mph): ")

# Convert strings to floats    
distance = float(distance) 

# Train speeds in miles per hour   
t1speed=float(t1speed) 
t2speed=float(t2speed)


# Convert hh:mm:ss:ff time input to decimal (gives integer seconds from midnight i.e. 0)
(h,m,s) = t1time.split(":")
resultt1 = int(h) * 3600 + int(m) * 60 + int(s)

(h,m,s) = t2time.split(":")
resultt2 = int(h) * 3600 + int(m) * 60 + int(s) 

timeapart = resultt2-resultt1     # Number of seconds the trains are apart
speeddifference = t2speed-t1speed # Difference in speed of the trains

t1distance = (t1speed/3600)*timeapart   #Convert speed to miles per second and multiply by timeapart to get current distance of the first train
timetomeet = t1distance/speeddifference #How long it takes the trains to meet in hours

# Since the trains are parallel heading in the same direction the point at which they meet will cause them to be the same distances on the track therefore only one distance needs to be calculated
distancein = t2speed*timetomeet

percentagein = (distancein/distance)    # Calculate the percentage of voyage

t1speedpercent = (t1speed/t2speed)
t2speedpercent = (t2speed/t1speed)

# Display the full problem to the user
print("========================================================================================================")
print("The Problem:")
print("At "+str(t1time)+" a train left "+str(city1)+" for " +str(city2)+ " at an average speed of "+str(t1speed)+" miles per hour.\n" +str(datetime.timedelta(seconds=timeapart))+ " hours later a second train left "+str(city2)+" for "+str(city1)+", on a parallel track, traveling\nat an average speed of "+str(t2speed)+ " miles per hour. At what distance and time will the two trains meet?")  
print("========================================================================================================")   



# Display outputs
print("The trains will meet in " + str(datetime.timedelta(hours=timetomeet)) + " hours.")
print("At the time the trains meet they will be " + str(format(distancein, '.2f')) + " miles into their journey.")
print("The trains completed " +str(format(percentagein, '.1%'))+" of their journey between the two cities.")
print("The closure speed of the trains are "+ str(format(speeddifference, '.2f')) +" miles per hour")
print("Train 1 is traveling at " + str(format(t1speedpercent, '.1%')) + " of the speed of train 2")
print("Train 2 is traveling at " + str(format(t2speedpercent, '.1%')) + " of the speed of train 1")


    
    
