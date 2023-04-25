# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:11:49 2023

4. Given an input string with the combination of the lower and upper case arrange characters in such a
way that all lowercase letters should come first.

@author: DBDA
"""
lower=""
upper=""
s1=input("enter a string with combination of lower and uppercase characters")
for i in s1:
    if i.islower():
        lower+=i
    else:
        upper+=i
s3=lower+upper
print(s3)