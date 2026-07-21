# write a program to find the euclidian distance between do cordinates

import math

x1 = float(input("enter the x1 coordinate: "))
x2 = float(input("enter the x2 coordinate: "))
y1 = float(input("enter the y1 coordinate: "))
y2 = float(input("enter the y2 coordinate: "))

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

print(f"the distance between ({x1},{y1}) and ({x2},{y2}) is {distance}")