# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:27:35 2023

10. Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
output:
[5, 15, 25, 50]

@author: DBDA
"""

list1 = [5, 20, 15, 20, 25, 50, 20]
for e1 in list1:
    if e1==20:
        list1.remove(e1)
print(list1)
