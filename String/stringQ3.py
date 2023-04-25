# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:01:31 2023

3. two strings, s1, and s2 return a new string made of the first, middle, and last characters of each input
string
Given:
s1 = "America"
s2 = "Japan"
Expected Output:
AJrpan

@author: DBDA
"""

s1=input("enter string 1st")
s2=input("enter string 2nd")
print(s1[0]+s2[0]+s1[len(s1)//2]+s2[len(s2)//2]+s1[-1]+s2[-1])