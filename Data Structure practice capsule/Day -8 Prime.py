#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:56:04 2021

@author: quantum
"""

n = int(input('Enter your number: '))
flag = 1
for i in range(2,n):
    if n%i == 0:
        flag = 0
if flag == 0:
   print(f'{n} is not a prime number')
else:
   print(f'{n} is a prime number')
    