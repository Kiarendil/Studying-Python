#!/usr/bin/env python3
#coding: UTF-8

a = int(input())
i = 1
Cond = i ** 2 > a

while Cond != True:
    x = i ** 2
    i = i + 1
    print(x)
    if i ** 2 > a:
        Cond = True
    