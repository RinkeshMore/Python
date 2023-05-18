# -*- coding: utf-8 -*-
"""
Created on Wed May  3 22:38:00 2023

          Palindrome

@author: DBDA
"""


#Method 1

check=input("Enter string to check for Palindrome:-")
palin=check[::-1]
if check==palin:
    print("Ha bro Palindrome hu")
else:
    print("Nahi ban paya")
    

#Method 2

check=input("Enter string to check for Palindrome:-")
palin=reversed(check)
if check==palin:
    print("Ha hu Palindrome, to kya karlega?")
else:
    print("Na ji ham kaha Palindrome")


#Method 3

palin=""
check=input("Enter string to check for Palindrome:-")
for e in check:
    palin=e + palin
print(palin)
if palin==check:
   print("Ha bro Palindrome hu")
else:
   print("Na ji ham kaha Palindrome")






















