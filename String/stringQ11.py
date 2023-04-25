# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:25:34 2023

11. Given a paragraph count number of words, sentences. Every sentence ends with either . or ? or !
Print Count of how many normal sentences ending with . , how many interrogative sentences ( ending
with ?) and how many exclamatory sentences ( ending with !).
Ex.
Input : “I am at CDAC. What about you? I am surprised by current weather!”
Normal sentence : 1
Interrogative: 1
Exclamatory : 1

@author: DBDA
"""

str=input("Enter any sentence")
d,q,e=0,0,0
for i in str:
    if (i == '?') :
        q=q+1
    elif i == '.' :
        d=d+1
    elif i == '!':
        e=e+1
print(f"Normal Sentence:{d},\nInterrogative:{q},\nExclamatory:{e}")
