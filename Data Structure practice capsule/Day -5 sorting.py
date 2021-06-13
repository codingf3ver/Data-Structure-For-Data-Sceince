#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 00:15:59 2021

@author: quantum
"""
li = [int(input()) for _ in range(int(input('enter range: ')))]
min = li[0]
newli = []
for i in range(1,len(li)):
    if li[i] <= min:
        temp = li[i]
        li[i]=  min
        min = temp
print()        
print('minimum number in an array is : ' ,newli)    