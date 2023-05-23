# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:00:45 2023

9. Given a Python list, find value 20 in the list,
 and if it is present, replace it with 200.
 Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
output:
list1 = [5, 10, 15, 200, 25, 50, 20]

@author: DBDA
"""

l1=[5,10,15,20,25,50,20]
id=l1.index(20)
l1[id]=200
print(l1)


