# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:20:22 2023

10. Count occurrence of spaces, and special characters in given string
Ex.
Input: Fgh^f #89
Expected output :
Spaces: 1
Special characters: 2

@author: DBDA
"""
str=input("Enter a string")
space=0
alnum=0
for i in str:
    if i.isspace():
        space=space+1
    elif i.isalnum():
        alnum=alnum+1

print("no of spaces:",space)
print("no of special characters is:",len(str)-space-alnum)

