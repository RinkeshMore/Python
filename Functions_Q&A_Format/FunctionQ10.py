# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 00:27:02 2023

10. Create a calculator.py file 
Create add(), subtract(), multiply(), divide(), power(), log() functions
Create a menu driven program to take values and operation as input from user 
and print result using these functions


@author: DBDA
"""
import math
def add(num1,num2):
    addition=num1+num2
    print("num1 + num2 =",addition)
def subtract(num1,num2):
    subtract=num1-num2
    print("num1 - num2 =",subtract)
def multiply(num1,num2):
    multiply=num1*num2
    print("num1 * num2 =",multiply)
def divide(num1,num2):
    division=num1/num2
    print("num1 / num2 =",division)
def power(num1,num2):
    power=num1**num2
    print("num1 raised to the power num2 =",power)
def log(num1,num2):
    logm=math.log(num1,num2)
    print(logm)

choice=input("Enter your choice \n a: Addition \n b: Substraction \n c: Multipliction \n d:Division \n e:Power \n f: Log-->")  

if  choice=="a":
    num1=int(input("Enter 1st number="))
    num2=int(input("Enter 2nd number="))
    add(num1,num2)
elif choice=="b":
    num1=int(input("Enter 1st number="))
    num2=int(input("Enter 2nd number="))
    subtract(num1,num2)
elif choice=="c":
    num1=int(input("Enter 1st number="))
    num2=int(input("Enter 2nd number="))
    multiply(num1,num2)
elif choice=="d":
    num1=int(input("Enter 1st number="))
    num2=int(input("Enter 2nd number="))
    divide(num1,num2)
elif choice=="e":
    num1=int(input("Enter base number="))
    num2=int(input("Enter power="))
    power(num1,num2)
elif choice=="f":
    num1=int(input("Enter number="))
    num2=int(input("Enter base="))
    log(num1,num2)
    
else:
    print("Invalid Input")






    