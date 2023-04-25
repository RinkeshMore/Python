# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:21:00 2023

4. set of all elements in either A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:
{20, 70, 10, 60}

@author: DBDA
"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference_update(set2)
print(set1)
