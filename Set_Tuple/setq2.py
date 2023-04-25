# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:15:33 2023


2. display common elements from the given set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

@author: DBDA
"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)