# -*- coding: utf-8 -*-
"""
Created on Tue May  2 22:31:56 2023
Armstrong Number.
    It is a number with 'n' digits. Here (sum of every digit ^ n) equal to ( number itself)

    1) 1^3 5^3 3^3=153 ( here number of digits(n) is 3)
    2) 1^1 = 1 ( here number of digits is 1)
    3) 1634 = 1^4 + 6^4 + 3^4 + 4^4 ( here number of digits is 4)

@author: DBDA
"""
#Method 1

def tu_armstrong_no_hai_kya(num1):
    while num1>0:
        sum=0
        digit=num1%10
        sum+=digit**n
        num1//10
        return sum
num1=input("Enter any Number to check whether it is Armstrong or not:-")
n=len(num1)
tu_armstrong_no_hai_kya(int(num1))
if sum==int(num1):
     print("han ji")0
else:
     print("na ji")


""""""""""""""""""
#Method 2


def tu_armstrong_no_hai_kya(num):
        n=len(num)
        sum=0
        for e in num:
            sum+=int(e)**n
        if int(num)==sum:
            print("Han ji Armstrong hu")
        else:
            print("Na ji")
   
num=input("Enter any Number to check whether it is Armstrong or not:-")
tu_armstrong_no_hai_kya(num)














