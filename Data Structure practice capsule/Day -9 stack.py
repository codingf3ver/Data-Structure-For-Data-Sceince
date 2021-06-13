#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:18:46 2021

@author: quantum
"""


def stack():
    array = []
    return array

def pop(array):
    if isEmpty(array):
        return print('\nStack is empty')
    else:
        return print(f'\n{array.pop()} is popped form the array')
    

def push(array,element):
    array.append(element)
    print(f'\n{element} is pushed into the array')
    

def isEmpty(array):
    return len(array) == 0
    

obj = stack()
pop(obj)
push(obj,39)
push(obj,90)
push(obj,190)
push(obj,76)
push(obj,42)
pop(obj)
print(f'\nArray after popping {obj} ')
push(obj,15)
push(obj,78)
pop(obj)
print(f'\nArray after popping {obj} ')
print(f'\nArray after pushing and popping {obj} ')
pop(obj)
pop(obj)
pop(obj)
pop(obj)
print(f'\nArray after popping {obj} ')
pop(obj)
pop(obj)
pop(obj)


