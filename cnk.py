#!/usr/bin/env python3
#coding: UTF-8

def fac(n):
      if n == 0:
           return 1
      else:
           return n * fac(n-1)
      
def C_n_k(n,k):
    return int(fac(n) / (fac(n-k) * fac(k)))
