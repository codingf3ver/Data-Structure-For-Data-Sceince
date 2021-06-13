#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 18:30:39 2021

@author: quantum
"""

li = [int(input()) for _ in range(int(input('range: ')))]
s = 0
for i in li:
    s = s + i
print('sum',s)    
