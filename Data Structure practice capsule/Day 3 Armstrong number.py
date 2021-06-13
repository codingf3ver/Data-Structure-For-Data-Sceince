#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:16:58 2021

@author: quantum
"""

n=int(input('enter the number: '))

def Armstrong(n):
    temp = n
    sum = 0
    while n != 0:
        rem = n % 10
        sum = sum + rem ** 3
        n = n // 10

    if temp == sum:
        return 'Armstrong'
        
    else:
        return 'Not Armstrong'
    
print(Armstrong(n))    
    
    
    

