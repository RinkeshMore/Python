# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 23:42:27 2023

2. Given a dictionary of students and their favourite colours:
people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
a. Find out how many students are in the list
b. Change Lisa’s favourite colour
c. Remove 'Jenny' and her favourite colour

4. Sort and print students and their favourite colours alphabetically by name
@author: DBDA
"""

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

#a. Find out how many students are in the list        
count_students=len(people.keys())

print("Number of students are there:-",count_students,"\n")

#b. Change Lisa’s favourite colour

people['Lisa']='Red'
print("After changing Lisa's favourite color:-\n",people,"\n")

#c. Remove 'Jenny' and her favourite colour

del people['Jenny']
print("After Deliting Jenny:-\n",people,"\n")

#Sort
people_list = list(people.items())
people_list.sort()
 
print("Sorted Dictionary:-\n",people_list)