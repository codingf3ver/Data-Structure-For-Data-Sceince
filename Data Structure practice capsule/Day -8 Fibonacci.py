#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:17:56 2021

@author: quantum
"""

n = int(input('Enter the threshold for fibonacci: '))

first = 0
second = 1
print(first,end=' ')
while second < n:
    temp =  second
    second = second + first
    first = temp
    print(second, end=' ')
    
inp = int(input('\nEnter the range for fibonacci: '))
f = 0
s = 1
print(f,end=' ')
for _ in range(s,inp):
    t =  s
    s = s + f
    f = t
    print(s, end=' ')    