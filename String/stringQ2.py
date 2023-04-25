# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:48:23 2023

2. Given two strings, s1 and s2, create a new string
 by appending s2 in the middle of s1
Given:
s1 = "Ault"
s2 = "Kelly"
Expected Output:
AuKellylt

@author: DBDA
"""
s1=""
s2=""
s1=input("enter 1st string to get it appended with other")
s2=input("2nd string to be appended in 1st")
s3=s1[0:len(s1)//2:]
s4=s1[len(s1)//2:]
s5=s3+s2+s4
print(s5)