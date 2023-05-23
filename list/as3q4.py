# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:16:46 2023

4. Print two lists in the following order
list1 = [5, 6,7]
list2 = [0, 1]
output:
50,51,60,61,70,71

@author: DBDA
"""

list1 = [5,6,7]
list2 = [0, 1]
for e1 in list1:
    for e2 in list2:
       print(e1,e2,',',sep="", end="")
        