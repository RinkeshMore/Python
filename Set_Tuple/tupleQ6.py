# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:57:19 2023

6. Modify the first item (22) of a list inside a following tuple to 200
tuple1 = (11, [22, 33], 44, 55)
Expected output:
tuple1: (11, [200, 33], 44, 55)

@author: DBDA
"""

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=200
print(tuple1)