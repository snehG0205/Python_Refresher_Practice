#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:01:31 2019

@author: snehgajiwala
"""

a = [5, 1, 4, 3]
print (sorted(a))  ## [1, 3, 4, 5]
print (a)  ## [5, 1, 4, 3]

strs = ['aa', 'BB', 'zz', 'CC']
print (sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print (sorted(strs, reverse=True))   ## ['zz', 'aa', 'CC', 'BB']

## "key" argument specifying str.lower function to use for sorting
print (sorted(strs, key=str.lower))  ## ['aa', 'BB', 'CC', 'zz']


strs = ['ccc', 'aaaa', 'd', 'bb']
print (sorted(strs, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']