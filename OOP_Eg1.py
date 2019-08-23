#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 17:19:46 2019

@author: snehgajiwala
"""

#object oriented example 1

class Sample():
    pass


x = Sample()
print(type(x))


class Dog():
#    class object attributes => common for all objects in class
    species = 'mammals'
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    
    
    

myDog = Dog(breed='Lab',name='Mark')
#print(type(myDog))
print(myDog.breed)
print(myDog.name)
print(myDog.species)

print('\n')

otherDog = Dog('Retriever', 'Jamie')
print(otherDog.breed)
print(otherDog.name)
print(otherDog.species)