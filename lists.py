#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:50:24 2019

@author: snehgajiwala
"""

colors = ['red', 'blue', 'green']
print (colors[0])    # red
print (colors[2])    # green
print (len(colors))  # 3


if 'red' in colors:
    print ('found')
    
    
list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print (list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print (list.index('curly'))    ## 2

list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print (list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']


list = ['a', 'b', 'c', 'd']
print (list[1:-1] )  ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print (list)         ## ['z', 'c', 'd']


nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]
print(squares)


fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s ]
print(afruits)


list = ['a', 'b', 'c', 'd']
del list[0]     ## Delete first element
del list[-2:]   ## Delete last two elements
print (list)      ## ['b']