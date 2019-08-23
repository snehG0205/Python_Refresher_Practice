#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:12:54 2019

@author: snehgajiwala
"""

dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print (dict)  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print (dict['a'])

if 'a' in dict: print (dict['a'])

print (dict.get('z')) #'None' because z doesn't exist

#to print keys
for key in dict: print (key)

print (dict.keys()) 

#to print values
for val in dict: print (val)

print (dict.values())

## accessing each key/value in sorted order
for key in sorted(dict.keys()):
    print (key, dict[key])
    

## .items() is the dict expressed as (key, value) tuples
print (dict.items())  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

## This loop syntax accesses the whole dict by looping over the .items() tuple list, accessing one (key, value) pair on each iteration.
for k, v in dict.items(): print (k, '>', v ) ## a > alpha    o > omega     g > gamma


dict = {'a':1, 'b':2, 'c':3}
del dict['b']   ## Delete 'b' entry
print (dict)      ## {'a':1, 'c':3}