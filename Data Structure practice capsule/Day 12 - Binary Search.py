#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 22:48:50 2021

@author: quantum
"""

arr = [int(input()) for _ in range(int(input('Enter range for an array: ')))]
num = int(input('Enter element to be searched: '))


def binary(arr,num):
    arr =  sorted(arr)
    low = 0                  #index postion
    high = len(arr)-1        #index postion
    mid = arr[(low+high)//2]
    if num == mid:
        print(f'Element {num} found! at index {(low+high)//2}')
    elif num > mid:
        low = mid + 1
        high = high
    else:
        low = low
        high = mid - 1

binary_out = binary(arr, num)
binary_out     
        
        
        