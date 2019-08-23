#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:50:40 2019

@author: snehgajiwala
"""

numbers = [1, 4, 9, 16]
sum = 0
for num in numbers:
    sum += num

print (sum)  ## 30


## print the numbers from 0 through 9
for i in range(10):
    print (i)
    
#printing elements in numbers   
i=0   
while i < len(numbers):
    print (numbers[i])
    i = i + 1