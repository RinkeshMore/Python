# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:16:58 2023

3. Generate a new set with all items from both sets by 
removing numbers which are in both sets.
set1 = {10, 20, 30, 40, 50,25}
set2 = {30, 40, 50, 60, 70,100}
o/p : order is not important
{70, 10, 20, 60,25,100}

@author: DBDA
"""
set1 = {10, 20, 30, 40, 50,25}
set2 = {30, 40, 50, 60, 70,100}
set1^=set2
print(set1)
