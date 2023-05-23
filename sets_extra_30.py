# -*- coding: utf-8 -*-
"""
Created on Wed May 17 21:01:12 2023


24. Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.









27. Write a Python program to find all the anagrams in a given list of strings and then group them together. Use the Python data type.



28. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.






@author: DBDA
"""
"""
1. Write a Python program to create a set.
"""

s1=set(x for x in range(1,20))
print(s1)


"""
2. Write a Python program to iterate over sets.
"""

s1={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
print(s1)
for i in s1:
    print(i)


"""
3. Write a Python program to add member(s) to a set.
"""

s1=set(x for x in range(1,20))
print(s1)
s1.add((22,44,66,88))
print(s1)


"""
4. Write a Python program to remove item(s) from a given set.
"""

s1={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
s1.remove(15)
print(s1)
s1.discard(20)
print(s1)


"""

5. Write a Python program to remove an item from a set if it is present in the set.
"""
s1={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
s1.remove(15)
print(s1)


"""
6. Write a Python program to create an intersection of sets.
"""
s1=set(x for x in range(0,5,1))
print(s1)
s2=set(x for x in range(1,10,1))
print(s2)

#s1.intersection(s2)
#print(s1)

s1 &= s2
print(s1)

"""
7. Write a Python program to create a union of sets.
"""
s1=set(x for x in range(0,5,1))
print(s1)
s2=set(x for x in range(1,10,1))
print(s2)

s1 |= s2
print(s1)


"""8. Write a Python program to create set difference.
"""

s1=set(x for x in range(0,5,1))
print(s1)
s2=set(x for x in range(1,10,1))
print(s2)

s1 -=s2
print(s1)

"""
9. Write a Python program to create a symmetric difference.
"""


s1=set(x for x in range(0,5,1))
print(s1)
s2=set(x for x in range(1,10,1))
print(s2)

s1 ^=s2
print(s1)


"""
10. Write a Python program to check if a set is a subset of another set.
"""

s1=set(x for x in range(1,4,1))
print(s1)
s2=set(x for x in range(1,10,1))
print(s2)

print(s1.issubset(s2))
print(s1<s2)

print(s1.issuperset(s2))
print(s2>s1)

"""
11. Write a Python program to create a shallow copy of sets.

Note : Shallow copy is a bit-wise copy of an object. 
A new object is created that has an exact copy of the values in the original object.
"""

s1=set(x for x in range(1,4,1))
print(s1)
s2=set(x for x in range(1,10,1))
print(s2)

s3=s1.copy()
print(s3)

"""
12. Write a Python program to remove all elements from a given set.
"""
s1=set(x for x in range(1,4,1))
print(s1)
s1.clear()
print(s1)

"""
13. Write a Python program that uses frozensets.
Note: Frozensets behave just like sets except they are immutable.

"""

s1=set(x for x in range(1,4,1))
f=frozenset(s1)
print(f)


"""
14. Write a Python program to find the maximum and minimum values in a set.
"""

s1=set(x for x in range(1,4,1))
print(max(s1))
print(min(s1))


"""
15. Write a Python program to find the length of a set.
"""
s1=set(x for x in range(1,15))
print(len(s1))

"""
16. Write a Python program to check if a given value is present in a set or not.
"""
s1=set(x for x in range(1,15))
print(12 in s1)
print(16 in s1)
print(17 not in s1)
print(12 not in s1)


"""
17. Write a Python program to check if two given sets have no elements in common.
"""
s1=set(x for x in range(1,5))
s2=set(x for x in range(15,20))
if (s1-s2)!=0:
    print("nothing common")
else:
    print("have common elements")


"""
18. Write a Python program to check if a given set is a superset of itself and a superset of another given set.

"""
s1=set(x for x in range(1,4,1))
print(s1)
s2=set(x for x in range(1,10,1))
print(s2)
print(s1>s1)
print(s2>s1)


"""
19. Write a Python program to find elements in a given set that are not in another set.

"""
s1=set(x for x in range(1,7))
s2=set(x for x in range(4,20))
print(s1)
print(s2)
s1 -=s2
print(s1)

"""
20. Write a Python program to remove the intersection of a second set with a first set.
"""
s1=set(x for x in range(1,7))
s2=set(x for x in range(4,20))
print(s1)
print(s2)
s2 &=s1
print(s2)


"""
21. Write a Python program to find all the unique words and count the frequency of occurrence
 from a given list of strings. Use Python set data type.
"""


def word_count(w):
    unique_w=set(w)
    w_count={}
    for word in unique_w:
        w_count[word]=w.count(word)
    print(w_count)
        
list_of_words=['vision','drishti','vision','sriram','shankar','shankar','vision']
word_count(list_of_words)


"""
22. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

"""

def pairs_sum(num,sum_value):
    unique_num=set(num)
    pairs=[]
    for n1 in unique_num:
       n2 =sum_value - n1
       if n2 in unique_num:
           pairs.append((n1,n2))
    return pairs 

list1=[23,34,66,75,25,30,60,70,40,77]
sum_value=100
pairs_sum(list1,sum_value)



"""
23. Write a Python program to find the longest common prefix of all strings. Use the Python set.

"""



"""
25. Given two sets of numbers, write a Python program to find the missing numbers
 in the second set as compared to the first and vice versa. Use the Python set.

"""

def missing_num(set1,set2):
    return set(set1)-set(set2),set(set2)-set(set1)

set1={1,2,3,4,5}
set2={4,5,6,7,8}
res=missing_num(set1, set2)
print(res)
print(res[0])
print(res[1])


"""
26. Write a Python program to find all the anagrams and group them together from a given list of strings. Use the Python data type.

"""


def group_anagrams(strs):
    result = {}
    for s in strs:
        sorted_string = ''.join(sorted(s))
        if sorted_string in result:
            result[sorted_string].append(s)
        else:
            result[sorted_string] = [s]
    return list(result.values())

strs = ['eat', 'cba', 'tae', 'abc', 'xyz']
print("Original list of strings:") 
print(strs)
print("Find and group all anagrams in the said list:")
print(group_anagrams(strs))



"""
29. Write a Python program to find the third largest number from a given list of numbers.
Use the Python set data type.

"""

list1=[23,34,66,75,25,30,60,70,40,77]
num=set(list1)
print(num)
num=list(num)
num.sort(reverse=True)
print(num)
print("3rd largest no:",num[2])
    


"""
30. Write a Python program to remove all duplicates from a given list of strings 
and return a list of unique strings. Use the Python set data type.
"""
list_of_strings=['vision','drishti','vision','sriram','shankar','shankar','vision','levelUp','vajiram-ravi']

unique_strings=set(list_of_strings)
print(unique_strings)
print(list(unique_strings))










