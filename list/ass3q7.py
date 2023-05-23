# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:31:58 2023

7. Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
output:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

@author: DBDA
"""

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)