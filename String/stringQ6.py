# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:54:43 2023

6. Find all occurrences of “USA” from right to left in a given string ignoring the case. also display the
starting position
Given:
str1 = "Welcome to USA. usa awesome, isn't it?
Expected answer : 16, 11

@author: DBDA
"""
str1="Welcome to USA. usa awesome, isn't it?"
str2=str1.upper()
print(str2.rfind('USA'),str2.find('USA'))

