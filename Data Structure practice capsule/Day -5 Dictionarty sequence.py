#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:48:59 2021

@author: quantum
"""

''' write a program to generate a dictionary that contains (i, i*i) such that is an integral number
 between 1 and n (both included). and then the program should print the dictionary.
'''

n = int(input('Enter the range: '))

compreDict={ i : i*i for i in range(1,n +1)}

print(compreDict)#compreDict
