# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:24:06 2023

3. Given a Python list of numbers. Turn every item of a list into its square root
aList = [1, 4, 9, 16, 25, 36, 49] 
output:
[1, 2, 3, 4, 5, 6, 7]

@author: DBDA
"""
output=[]
aList = [1, 4, 9, 16, 25, 36, 49]
for e1 in aList:
        output.append(e1**0.5)
print(output)

