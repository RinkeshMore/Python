# -*- coding: utf-8 -*-
"""
Created on Wed May 17 01:08:04 2023

@author: DBDA
"""

"""
1. Write a Python function to find the maximum of three numbers. 

"""
def maximum(n1,n2,n3):
    m=max(n1,n2,n3)
    print(m)

n1,n2,n3=input("Enter 3 no:").split()
print(f"1st no is {n1},2nd no is {n2}, 3rd no is {n3}")
maximum(n1,n2,n3)

"""
2. Write a Python function to sum all the numbers in a list. 
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""

def add(l1):
    sum=0
    for i in l1:
        sum+=i
    return sum

l1=[8, 2, 3, 0, 7]
print("sum of list elements:",add(l1))

"""
3. Write a Python function to multiply all the numbers in a list. 
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""

def add(l1):
    product=1
    for i in l1:
        product*=i
    return product

l1=[8, 2, 3, -1, 7]
print("product of list elements:",add(l1))


"""
4. Write a Python program to reverse a string. 
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""
st="1234abcd"
rev=st[::-1]
print(rev)

"""
5. Write a Python function to calculate the factorial of a number (a non-negative integer).
 The function accepts the number as an argument. 

"""
def fact(num):
    
    if (num==1 or num==0):
       return 1
    
    return (num*fact(num-1))

num=int(input("Enter no for factorial:"))
print(fact(num))

"""
6. Write a Python function to check whether a number falls within a given range. 
"""
def check(num,r):
    for i in range(r):
        if num==i:
            print("no is present in this range")
        else:
            print("not present")
num,r=input("Enter num and range in which it has to be searched").split()
check(int(num),int(r))
































