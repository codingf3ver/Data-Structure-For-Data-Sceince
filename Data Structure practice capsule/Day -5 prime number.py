#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:50:47 2021

@author: quantum
"""

n = int(input('Enter your num: '))
for i in range(2,n):
    if n % i == 0 :
        print('not prime number ')
    else:
        print('prime number') 
        
    
    
