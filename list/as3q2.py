# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:22:07 2023

2. take a list 'l1' of even nos between 150 to 250. Print its length.
Then create another list 'l2' using 'l1', containing only nos divisible by 4 from 'l1'.


@author: DBDA
"""

l1=[]
l2=[]
for i in range(150,251,2):
    l1.append(i)
print(l1)
print("length of l1",len(l1))

for e1 in l1:
    if e1%4==0:
       l2.append(e1)
print(l2)