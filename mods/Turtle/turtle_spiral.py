# coding: utf-8

import turtle
turtle.shape('turtle')

i = 0
j = 0
angle = 10

while i < 5:
    r = (1 * (angle + 360*i)) / 360
    while j < 10:
        turtle.forward(r)
        turtle.left(180 - (500-2)*180/500)
        j += 1
    angle += 10
    j = 0
    if angle == 360:
        i += 1
        angle = 10
        continue


    
