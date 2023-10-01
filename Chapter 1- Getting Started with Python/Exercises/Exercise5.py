#Write a Python program which accepts the radius of a circle from the user and compute the area.

import math 
r= input ("Enter the radius of the circle:")
radius= float(r)
area = math.pi*(radius**2)
print (f"The area of the circle with radius {radius} is {area}")
