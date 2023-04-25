# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:56:14 2023

7. Take two integer values in a & b. Swap their values using tuple, using temparary variable and without tuple and without temparary variable.
Ex. a=10 b=23
After swapping a=23 b=10

@author: DBDA
"""
print("using 3rd variable")
a=10
b=23

c=a
a=b
b=c
print(a,b)
print("without using third variable")
a=10
b=23
a=a+b
b=a-b
a=a-b
print(a,b)

print("using tuple")
a=(10,)
b=(23,)
a,b=b,a
print(a,b)