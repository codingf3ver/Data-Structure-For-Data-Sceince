#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 08:23:24 2021

@author: quantum
"""

arr=[1,3,2,2,4,0]
k=4

def arrays(arr,k):
    if len(arr)<2:
        return print('Not a valid size')
    
    check=set()
    op=set()
    
    for i in arr:
        target = k - i
        
        if target not in check:
            check.add(i)
        
        else:
            op.add((min(i,target),max(i,target)))
    
    print('\n'.join(map(str,list(op))))
    
arrays(arr,k)    
