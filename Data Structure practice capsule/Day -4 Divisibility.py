#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:13:47 2021

@author: quantum
"""

'''Write a program which will find all such numbers which are divisible by 7 
but are not a multiple of 5, between 2000 and 3200 (both included).'''

list = []
for i in range(2000 ,3201):
    if i % 7 == 0 and i %5 != 0:
        list.append(i)
print(list)        