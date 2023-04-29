# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:30:30 2023

2. WA function to calculate total salary given that
1. post      2. basic salary
rules:
total sal = basic + TA + HRA
TA = 5000 for 'manager' and TA = 10,000 for 'employee'
HRA = 20,000 for 'manager' and HRA = 12,000 for 'employee'

return total salary based on two parameters
@author: DBDA
"""

def salary(post,basic_salary):
    if post=='employee':
        ta=10000
        hra=12000
        sal=basic_salary + ta + hra
        print(sal)
    elif post=="manager":
        ta=5000
        hra=20000
        sal=basic_salary + ta + hra
        print(sal)
    return

post=input("enter your post-> employee/manager-->")
basic_salary=int(input("enter basic salary-->"))
salary(post,basic_salary)