# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 22:20:05 2023


8. Given a string in format Emp_name:Emp_id
If emp_i is perfect square -- > Print only vowels from emp_name
Else if emp_id is prime -- > print alternate characters from emp_name
Else if emp_id is odd -- > print sum of ascii values of characters in emp_name
Else print None

@author: DBDA
"""

import sympy
str=input('Enter a string in format Emp_name:Emp_id')
name,id=str.split(':')
idx=int(id)
if (idx**0.5).is_integer():
    vowel=['a','e','i','o','u']
    for i in name:
        name1=''
        if i.lower() in vowel:
            name1=name1+i
            print(name1,end='')
elif sympy.isprime(idx):
    print(name[::2])
    
elif idx % 2 == 0:
    sum=0
    for i in name:
        sum=sum+ord(i)   
    print(sum)
else:
    print('None')
    

































