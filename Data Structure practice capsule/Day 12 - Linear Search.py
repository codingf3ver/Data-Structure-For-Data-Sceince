#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 22:18:41 2021

@author: quantum
"""

arr = [int(input()) for _ in range(int(input('Enter range for an array: ')))]
num = int(input('Enter element to be searched: '))
if num in arr:
    print('\nNumber found!')
else:
    print('\nNot found!')
    
# scond method

def linear(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

output =linear(arr, num)

if output == -1:
    print('Element not found!')
else:
    print(f'Number {num} is found! at index {output} ')    