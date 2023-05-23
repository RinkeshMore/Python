# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:28:58 2023

11. Take a number as input from user. 
Print maximum and minimum integer which can be generated using all the digits in the input number
Ex. Input 3421   : o/p max: 4321, min 1234
Input 7789    : o/p max: 9776   min 6779

@author: DBDA
"""

no=input("Enter a number")
print(list(no))
for digit in no:
     print(digit)
digits_list=list(no)
digits_list.sort(reverse=True)
max_num="".join(digits_list)
max_num=int(max_num)
digits_list.sort()
min_num="".join(digits_list)
min_num=int(min_num)
print("Max number forward is: ",max_num,"\n min number formed is:",min_num)