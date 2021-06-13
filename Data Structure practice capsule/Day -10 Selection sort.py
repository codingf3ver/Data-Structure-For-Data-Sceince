#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:02:20 2021

@author: quantum
"""

arr = [int(input()) for _ in range(int(input('Enter range for an array: ')))]
print('\n')
def selection(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
            temp = arr[min_ind]
            arr[min_ind] = arr[i]
            arr[min_ind] = temp
    return arr
print(selection(arr))
