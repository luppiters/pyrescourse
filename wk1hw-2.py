#The ratio of the areas of a circle and the square inscribing it is pi / 4. 
#In this six-part exercise, we will find a way to approximate this value.

#2a

"""Using the math library, calculate and print the value of pi / 4"""

import math
print( math.pi / 4)

#2b
"""Using random.uniform, create a function rand() that generates a single float between -1 and 1.
Call rand() once. So we can check your solution, we will use random.seed to fix the value called by your function."""

import random
import math
import numpy as np

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand():
   # define `rand` here!
   return np.random.uniform(-1.0,1.0)

rand()

#2c
"""The distance between two points x and y is the square root of the sum of squared differences along
each dimension of x and y. Create a function distance(x, y) that takes two vectors and outputs the distance between them.
Use your function to find the distance between x=(0,0) and y=(1,1).
Print your answer."""

import math
import numpy as np

x = np.array([0,0])
y = np.array([1,1])
    
def distance(x, y):
    return np.sqrt(sum(y - x))
   
print(distance(x,y))   

#2d
"""distance(x, y) is pre-loaded from part 2c. Write a function in_circle(x, origin) that determines whether
a two-dimensional point falls within a unit circle surrounding a given origin. Your function should return a boolean
that is True if the distance between x and origin is less than 1, and False otherwise.
Use your function to determine whether the point (1,1) lies within the unit circle centered at (0,0).
Print your answer."""

import random, math

random.seed(1)

def in_circle(x, origin = [0]*2):
   #if point inside return true
    if distance(x, origin) < 1:
        return True
    else:
        return False

print(in_circle((1, 1)))
   

#2e
"""Create a list of R=10000 booleans called inside that determines whether each point in x falls
within the unit circle centered at (0,0). Make sure to use in_circle.
Find the proportion of points within the circle by summing the count of True in inside, and dividing by R.
Print your answer. This proportion is an estimate of the ratio of the two areas!"""

R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    # Enter your code here! #
    inside.append(in_circle(point, [0,0]))
# Enter your code here! #
proportion = inside.count(True) / R
print(proportion)

#2f
"""Note: inside and R are defined as in Exercise 2e. Recall that the true ratio of the area of the unit circle
to the area to the inscribing square is pi / 4.
Find the difference between your estimate from part 2e and math.pi / 4.
Print your answer."""

# write your code here!
random.seed(1)

proportion = inside.count(True) / R
difference = abs(proportion - (math.pi/4))

print(difference)





