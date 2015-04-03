__author__ = 'leahscott'
from graphics import *
import random
import time

window = GraphWin("Visualisation", 800, 600)
datafile = open("data.txt", 'r')
for line in datafile:
#generate random positions for the squares
    x = random.randrange(10,700)
    y = random.randrange(10,500)
#Split the numbers into two by the decimal place
    size, colour = line.split(".")
#convert to intergers
    size = int(size)
    x = int(x)
    y = int(y)
#getting the co-ordinates of the second 'point' by adding the size to the starting point.
    xend= x+size
    yend=y+size
    shade = int(colour)
#get the colour to be a number between 0-255
    shade = shade * 2.55

#draw the squares
    box = Rectangle(Point(x, y), Point(xend, yend))
    box.setFill(color_rgb(shade, shade, shade))
    box.setOutline(color_rgb(shade, shade, shade))
    box.draw(window)
#convert to strings to print (to check all is well)
    colour = str(colour)
    shade = str(shade)
    size = str(size)
    x = str(x)
    y = str(y)
    print("Data: " + line + " Size: " + size + " x " + x + " y " + y + " Colour:" + colour + "Shade:" + shade)
#delay drawing of squares - cause it's pretty
    time.sleep(1)



window.getMouse()