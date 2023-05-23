# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:25:23 2023

5. Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order. It should work for any two lists.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
output:
10 400
20 300
30 200
40 100

@author: DBDA
"""

list3=[]
a=[]
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for e2 in list2[::-1]:
    list3.append(e2)
for e1,e3 in zip(list1,list3):
    print(e1,e3)