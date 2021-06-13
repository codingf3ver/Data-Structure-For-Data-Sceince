#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:11:57 2021

@author: quantum
"""
class Queue:
    
    def __init__(self):
        self.queue =[]
        
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return print('Queue is empty at first')
        else:
            return self.queue.pop(0)
    
        #displaying array elements
    def show(self):
        return self.queue

obj = Queue()

obj.dequeue()

#Enqueuing inside the array
obj.enqueue(10)
obj.enqueue(130)
obj.enqueue(23)
obj.enqueue(34)
obj.enqueue(98)
print('\nQueue after insertion of elements:',obj.show())

#Dequeuing from the array
obj.dequeue()
obj.dequeue()

print('\nQueue after deletion of elements:',obj.show())

