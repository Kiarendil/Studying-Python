#!/usr/bin/env python3
# coding: utf-8

import turtle as t
import numpy as np
t.shape('turtle')

j = 3

def figure(n):
    i = 0
    an = 180 * (n - 2) / n
    r = 40 + (20 * (n - 3))
    r1 = 40 + (20 * (n - 4))
    an1 = np.sin(np.pi/n)
    a = r * 2 * an1
    t.penup()
    if n == 3:
        t.forward(r)
    else:
        t.forward(r - r1)
    t.pendown()
    t.left(180 - (an)/2)
    while i < n:
        t.forward(a)
        t.left(180 - an)
        t.stamp()
        i += 1
    t.right(180 - (an)/2)
            
n = int(input())   

while j <= n:
    figure(j)
    j += 1

input("vev")
    

        


