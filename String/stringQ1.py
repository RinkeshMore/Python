# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:26:18 2023

1. Given a string of odd length greater than 7, return a new string 
made of the middle three characters
of a given String
Given:
str1 = "RakeshzipPetabb"
Output
zip
str2 = "JazzbonAyxx"
Output
bon

@author: DBDA
"""


    
str1=input("enter any string of odd length more than 7 :")  
if len(str1)>7:
    a=str1[len(str1)//2-1:len(str1)//2+2]
    print(a)
else:
    print("please enter a valid string of length >7")