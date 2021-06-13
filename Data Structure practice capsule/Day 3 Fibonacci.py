#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:53:41 2021

@author: quantum
"""
n = int(input('enter range for fibonacci: '))
def fibo(n):
    a = 0
    b = 1
    while n >= 0:
        if a == 0:
             return 0
        elif b == 1:
             return 1
        else:
            return fibo(n - 1) + fibo(n - 2) 

x=fibo(n)  
print(x)      
             