#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:30:53 2021

@author: quantum
"""

def uniqueStr(string):
    
    temp = set()
    for i in string:
        
        if i in temp:
            return False
            
        else:
            temp.add(i)
    return True       
            
print(uniqueStr('abcdef'))    