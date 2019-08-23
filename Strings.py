#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:32:05 2019

@author: snehgajiwala
"""

s = "hi"
print (s[1]) #will print 'i'

print (len(s)) #will print 2

print (s+" there") #concatenate -> will print 'hi there'

pi = 3.14

print ("The value of pi is "+str(pi)) #typcasting

print ("This is a \t tab")

print ("This is a \n newline")

print (""" This adds all    formating
       by default""")  

 # % operator %d=int %s=string, %f=loating point
text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house') 
print (text)

#other methods
#s.lower(), s.upper() -- returns the lowercase or uppercase version of the string

#s.strip() -- returns a string with whitespace removed from the start and end

#s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes

#s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string

#s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found

#s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'

#s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.

#s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
