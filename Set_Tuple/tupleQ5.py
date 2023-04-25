# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:54:18 2023

5. Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
Expected output:
tuple2: (44, 55)

@author: DBDA
"""
tuple1 = (11, 22, 33, 44, 55, 66)
tup=tuple(tuple1[3:5])
print(tup)
