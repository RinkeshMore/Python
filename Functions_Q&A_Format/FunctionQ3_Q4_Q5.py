# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:42:59 2023

3.  WA function to rotate given string by 2 positon to right

Ex.
s1=”IACSD”
Rotate by 2 place to right
“SDIAC”

4.  Generalize above function to rotate string to right by n

5.  Generalize above function to rotate string by n to right or left

@author: DBDA
"""

#Q3 WA function to rotate given string by 2 positon to right
def rot_r_by_2(s):
        s1= s[2:] + s[:2]
        print(s1)
string1=input("enter string to be rotated to right by 2-->")

rot_r_by_2(string1)

#*****************************************************************

#Q4  Generalize above function to rotate string to right by n

def rot_r_by_n(s):
       
        s1= s[n:] + s[:n]
        print(s1)
string1=input("Enter string to be rotated to right by 'n' position-->")
n=int(input("Enter no of positions-->"))
rot_r_by_n(string1)

#*******************************************************************
#Q5.  Generalize above function to rotate string by n to right or left

def rot_by_n(s):
   if left_or_right=='r':
        s1= s[n:] + s[:n]
        print(s1)
        
   elif left_or_right=='l':
        s1= s[-n:] + s[:-n]
        print(s1)
        
string1=input("Enter string to be rotated by 'n' position-->")
n=int(input("Enter no of positions-->"))
left_or_right=input("rotate to left or right(r/l)?")
rot_by_n(string1)
















