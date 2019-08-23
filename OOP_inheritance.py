#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:07:14 2019

@author: snehgajiwala
"""

class Animal():
    def __init__(self):
        print("Animal created") #just fr demo
        
    def whoAmI(self):
        print('Animal')
        
    def eat(self):
        print('Eating')
        
        
class Dog(Animal):
    def __init__(self):
#        Animal.__init__(self)   optional initialisation
        print('Dog Created')
        
    def bark(self):
        print('WOOF!!')
        
    def eat(self): #overridding a method
        print('Dog eating')
        
        
myA = Animal()
myA.whoAmI()
myA.eat()

print('\n')

myDog = Dog()
myDog.whoAmI()
myDog.eat()
myDog.bark() 


