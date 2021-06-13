#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 08:36:22 2021

@author: quantum
"""

arr = [int(input()) for _ in range(int(input('Enter range for an array: ')))]
print('\n')
def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1] 
                arr[j+1] = temp
    return arr
sort = bubble(arr)
print('Sorted elements: ',sort)