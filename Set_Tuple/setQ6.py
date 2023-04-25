# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 01:05:31 2023

6. Take a sentence as input from user.
 Every word is seperated by space. Print all unique words from the sentence.
@author: DBDA

"""

sentence=input("enter a sentence")
sentence1=sentence.split()
print(sentence1)
words = set(sentence1)
print(words)
