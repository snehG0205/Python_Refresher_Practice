#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:00:52 2019

@author: snehgajiwala
"""

class Circle():
    
    pi = 3.14
    
    def __init__(self, radius=1): #default value of radius is 1
        self.radius = radius
        
    def area(self):
        area = self.radius*self.radius*Circle.pi
        return area
    
    def setRadius(self,new_r):
        self.radius = new_r
        
        
        
        
myCirc = Circle()
print(myCirc.radius)

print('\n')

myCirc = Circle(3)
print(myCirc.radius)
print(myCirc.area())


myCirc.radius = 10
print(myCirc.area())

myCirc.setRadius(20)
print(myCirc.area())