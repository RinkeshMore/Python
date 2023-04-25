# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:39:10 2023

@author: DBDA
"""






"""
#1
set = {"Yellow", "Orange", "Black"}
set.add("Blue")
set.remove("Black")
print(set)

#2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection(set2)

#3

set1 = {10, 20, 30, 40, 50,25}
set2 = {30, 40, 50, 60, 70,100}

set3=set1 ^ set2
print(set3)

#4

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1^set2

#5
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1 ^=set2
print(set1)

#6
sen=input("enter a sentence")
sen2=sen.split()
print(sen2)
words = set(sen2)
print(words)

#Tuple

#1
aTuple = (10, 20, 30, 40, 50,60)
print(aTuple[::-1])

#2
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])

#3

aTuple = (10, 20, 30, 40)
a,b,c,d=aTuple
print(a,b,c,d)

#4
tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1,tuple2=tuple2,tuple1
print(tuple1,tuple2)

#5
tuple1 = (11, 22, 33, 44, 55, 66)
tup=tuple(tuple1[3:5])
print(tup)

#6
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=200
print(tuple1)

#7
a=10
b=23
#with 3rd variable
c=a
a=b
b=c
print(a,b)
# without third variable
a=10
b=23
a=a+b
b=a-b
a=a-b
print(a,b)

#with tuple
a=(10,)
b=(20,)
a,b=b,a
print(a,b)















tuple.py
Displaying string.py.