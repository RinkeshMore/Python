# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:15:21 2023

6. WAP to count number of passengers in every airline. Here we are given 
dictionary of passanger id and airline id
Ex
input_dir ={'p1':'a1','p2':'a10','p89':'a1','p5':'a10'}
output: {'a1':2, 'a10':2}

@author: DBDA
"""
input_dir ={'p1':'a1','p2':'a10','p89':'a1','p5':'a10'}

s1=list(input_dir.values())

a=set(s1)

b={}

for i in a:
    b[i]=s1.count(i)
    
print(b)    
    
