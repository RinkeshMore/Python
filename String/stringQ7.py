# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:08:37 2023
7. Find all overlapping occurrences of given substring in given string
Ex.
String = 0111
Substring = 11
Expected answer : 2
String : ANANAAAANNN
Substring: ANA
Expected answer : 2
String : ANANAAAANNN
Substring: AA
Expected answer : 3
@author: DBDA
"""

str="01111"
substr="11"
cnt=0
for idx in range(len(str)):
    if (str.startswith(substr,idx)):
        cnt=cnt+1
print(cnt)
