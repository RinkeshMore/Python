# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:04:12 2023

1. Add a list of elements to a given set
Given:
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red",”Yellow”,”orange”]

@author: DBDA
"""

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red","Yellow","orange"]
for e in sampleList:
    sampleSet.add(e)
print(sampleSet)


