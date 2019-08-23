#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:43:45 2019

@author: snehgajiwala
"""

a=5
b=7
c=3

if a>b & a>c:
    print (str(a)+" is greatest")

elif b>a & b>c:
    print (str(b)+" is greatest")

elif c>a & c>b:
    print (str(c)+" is greatest")
    
else:
    print ("There seems to be some problem")
    
    