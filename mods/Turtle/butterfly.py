#!/usr/bin/env python3
#coding: UTF-8

import turtle as t
import numpy as np


def figure_l(n, r):
    i = 0
    an = 180 * (n - 2) / n
    an1 = np.sin(np.pi/n)
    a = r * 2 * an1
    t.left(180 - (an)/2)
    while i < n:
        t.forward(a)
        t.left(180 - an)
        i += 1
    t.right(180 - (an)/2)
    
def figure_r(n, r):
    i = 0
    an = 180 * (n - 2) / n
    an1 = np.sin(np.pi/n)
    a = r * 2 * an1
    t.left(180 - (an)/2)
    while i < n:
        t.forward(a)
        t.right(180 - an)
        i += 1
    t.right(180 - (an)/2)

            
n = 50
r = 50
j = 0

while j < 8:
    figure_l(n, r + 10*j)
    figure_r(n, r + 10*j)
    j += 1


 
input()
