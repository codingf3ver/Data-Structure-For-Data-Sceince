#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 18:40:38 2021

@author: quantum
"""
''' Reverse the string '''

li = [int(input()) for _ in range(int(input('range: ')))]
reverse = []

for i in range((len(li)-1),-1,-1):
    reverse.append(li[i])
print()

print('reverse ',reverse)
    
    