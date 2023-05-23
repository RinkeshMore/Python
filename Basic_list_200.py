# -*- coding: utf-8 -*-
"""
Created on Wed May  3 21:57:40 2023
1. Write a Python program to sum all the items in a list.
@author: DBDA
"""
l1=[]
n=int(input("Enter no of elements to be added in list:"))
for idx in range(n):
    e=int(input(f"Enter element at index.:{idx}-->"))
    l1.append(e)
print(l1)

add=0
for e1 in l1:
    add=add+e1
print("Addition:"+add)


"""
2. Write a Python program to multiply all the items in a list.
"""

l1=[]
n=int(input("Enter no of elements to be added in list:"))
for idx in range(n):
    e=int(input(f"Enter element at index.:{idx}-->"))
    l1.append(e)
print(l1)

mul=1
for e1 in l1:
    mul*=e1
print("Multiplication :",mul)


"""
3. Write a Python program to get the largest number from a list
"""
#Method 1
def largest(l1):
    largest=l1[0]
    for e in l1:
       if e>largest:
           largest=e
    return largest
               
l1=[]
n=int(input("Enter no of elements to be added in list:"))
for idx in range(1,n+1):
    e=int(input(f"Enter element at index.:{idx}-->"))
    l1.append(e)
print(l1)

print("largest element from a list is:",largest(l1))

#Method 2
"""
l1.sort()
print(l1)
print("largest element in list l1 is:",l1[-1])

"""
#Method 3
"""
print("largest element from a list is:",max(l1))

"""
"""
4. Write a Python program to get the smallest number from a list.

"""
l1=[]
n=int(input("Enter no of elements to be added in list:"))
for idx in range(1,n+1):
    e=int(input(f"Enter element at index.:{idx}-->"))
    l1.append(e)
print(l1)

#Method 1
l1.sort()
print("sorted_list:",l1)
print("Smallest number from the list is:",l1[0])

#Method 2
print("Smallest number from the list is:",min(l1))


"""
5. Write a Python program to count the number of strings from a given list of strings. 
The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""
l1=[]
n=int(input("Enter no of elements to be added in list:"))
for idx in range(n):
    e=input(f"Enter element at Index.:{idx}-->")
    l1.append(e)
print(l1)

count=0
for e in l1:
    if (e[0]==e[-1]) & (len(e)>=2):
        count+=1
print("Number of such strings:",count)    


"""
6. Write a Python program to get a list, sorted in increasing order
 by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

"""
#Method1
list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list1.sort(key=lambda x: x[1])
print(list1)

#Method2
list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l=sorted(list1,key=lambda x: x[1])
print(l)

"""
def list_order(x):
    return x[1]

list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l=sorted(list1,key=list_order(x))
print(list1)
"""


"""
7. Write a Python program to remove duplicates from a list

"""

l1=[]
n=int(input("Enter no of elements to be added in list:"))
for idx in range(1,n+1):
    e=int(input(f"Enter element at index.:{idx}-->"))
    l1.append(e)
print(l1)

s1=set(l1)
print("Afetr removing dublicates:",list(s1))


"""
8. Write a Python program to check if a list is empty or not.
"""
l1=[12,15,46,78]
l2=[]
if len(l1)==0:
    print("list l1 is empty")
elif len(l2)==0:
    print("list l2 is empty")    

"""
9. Write a Python program to clone or copy a list.
"""
l1=[12,15,46,78]
l2=l1.copy()
print("Copied List:l2-->",l2)


"""
10. Write a Python program to find the list of words that are longer than n from a given list of words.

"""
def longer_than_n(n):
    l3=[]
    for e in l1:
        if len(e)>n:
            l3.append(e)
    return l3

l1=[]
n=int(input("Enter no of elements to be added in list:"))
for idx in range(n):
    e=input(f"Enter element at Index.:{idx}-->")
    l1.append(e)
print(l1)
n=int(input("Enter length of word "))
print(longer_than_n(n))


"""
11. Write a Python function that takes two lists and returns True if they have at least one common member.
"""

def common_member(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                return True

l1=[]
n1=int(input("Enter no of elements to be added in list l1:"))
for idx in range(n1):
    e1=int(input(f"Enter element at index.:{idx}-->"))
    l1.append(e1)
print(l1)

l2=[]
n2=int(input("Enter no of elements to be added in list l2:"))
for jdx in range(n2):
    e2=int(input(f"Enter element at index.:{idx}-->"))
    l2.append(e2)
print(l2)

print("is there any common element:",common_member(l1,l2))


"""
12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

"""

l_c=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del l_c[0],l_c[3],l_c[3]
print("After removing:",l_c)

"""
13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""
#Method 1
list_3D=[]
for i in range(3):
   for j in range(4):
       for k in range(6):
           list_3D.append('*')
print(list_3D)
    
#method 2
list_3D=[[['*' for i in range(6)] for j in range(4)] for k in range(3)]
print(list_3D)


"""
14. Write a Python program to print the numbers
 of a specified list after removing even numbers from it.
"""
#def remove_even_no(l3):
    l4=[]
    for e1 in l3:
        if e1%2!=0:
            l4.append(e1)
    return l4

def maximum(l5):
    a=max(l5)
    return a
l2=[]
n=int(input("Enter no of elements to be added in list:"))
for idx in range(n):
    e=int(input(f"Enter element at index.:{idx}-->"))
    l2.append(e)
print(l2)
#print("After removing even elements:",remove_even_no(l2))
maximum(l2)
print("After removing even elements:",a)

"""
15. Write a Python program to shuffle and print a specified list
"""

l5=[]
n=int(input("Enter no of elements to be added in list:"))
for idx in range(n):
    e=int(input(f"Enter element at index.:{idx}-->"))
    l5.append(e)
print(l5)

shuffle=set(l5)

print(list(shuffle))

"""

"""






