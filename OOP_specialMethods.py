#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:14:56 2019

@author: snehgajiwala
"""

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        
        
    def __str__(self):  #string representation of the object. this is printed in the print statement when you print the object
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)
        
    
    def __len__(self):
        return self.pages #shows length of book (the pages)



b = Book("Random", "Me", 200)
print(b)

print(len(b))



 