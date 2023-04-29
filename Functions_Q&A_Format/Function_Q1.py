# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:02:29 2023

1. Write function which takes two parameters account no and name of the user.
Check if the account number is valid. Account no is valid only if it is a 
4 digit number less than 5000
Check if the name is valid. Name is valid if all characters are alphabets and 
no numbers or special chars in the name
If both name and acc no are valid return True 
If acc no is invalid return a message string saying “Account no is invalid”
if name is invalid return None

@author: DBDA
"""
def user(acc_no,user_name):
    if 999 < acc_no < 5000:
        if user_name.isalpha():
            print("True")
        else:
            print("none")
    else:
        print("your entered account no is invalid")
    return
a=int(input("enter user account number"))
u=input("enter user name")
user(a,u)