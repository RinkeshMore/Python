# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:12:41 2023

9. Find all mobile number mentioned in given paragraph of text
Mobile number is always a 10 digit number no spaces no special characters
Ex. Input= “this is a good number 9089786756 and 8900000000 is a desired number”
Expected output: 9089786756 , 8900000000

@author: DBDA
"""

str=input('Enter the string with mobile no')
lis=str.split()
print(lis)
list1=[x for x in lis if x.isdigit() and len(x)==10 ]
print(','.join(list1))

