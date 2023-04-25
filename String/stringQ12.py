# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:30:01 2023

12. You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w
Example .
String : “ABCDEFGHIJKLIMNOQRSTUVWXYZ”
Width: 4
Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

@author: DBDA
"""

str="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
for i in range(0,len(str),4):
    print(str[i:i+4])