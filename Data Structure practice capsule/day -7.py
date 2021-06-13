
# -*- coding: utf-8 -*-#!/usr/bin/env python3
"""
Created on Wed Apr  7 18:56:42 2021

@author: quantum

"""


''' 
program-to-find-second-largest-number-in-a-list

'''
arr =  [int(input())for _ in range(int(input('Enter range: ')))]
for i in range(len(arr)):
    min = arr[0]
    for j in range(1,len(arr)):
        if arr[j] <= min:
            min = arr[j]
            arr[j] = min
            
        else:
            min = arr[j]

print(arr)            
