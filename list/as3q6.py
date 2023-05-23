# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:31:02 2023

Remove empty strings from the list of strings
list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
output:
["Ashish", "Atharva", "Amit", "Revati"]

@author: DBDA
"""

list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
for e1 in list1:
    if e1=="":
        list1.remove(e1)
print(list1)