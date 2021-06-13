#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 05:01:09 2021

@author: quantum
"""

arr = [int(input()) for _ in range(int(input('Enter range for an array: ')))]

def insertion(arr):
    
    for i  in range(len(arr)):
        
        for j in range(i+1,len(arr)):
             key = arr[j]
             if arr[i] > key:
                 temp = arr[i]
                 arr[i] =  key
                 key = temp
    return arr             
sort = insertion(arr)
print('\n',sort)#sort           