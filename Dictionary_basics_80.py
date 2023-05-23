# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:15:39 2023
Dictionary practice from extra assignments
@author: DBDA
"""
"""
1. Write a Python script to sort (ascending and descending) a dictionary by value.

"""
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

sorted_d=sorted(d.values())
print(sorted_d)
sorted_d=sorted(d.values(),reverse=True)
print(sorted_d)

"""
2. Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""
d1={0: 10, 1: 20}
d1.update({2:30})
print(d1)

"""
3. Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dict4={}
for d in (dic1,dic2,dic3):
    dict4.update(d)
print(dict4)

"""
4. Write a Python script to check whether a given key already exists in a dictionary.
"""
d5={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_present(e):
    if e in d5:
        print(f"{e} is present in dictionary")
    else:
        print(f"{e} is not present in dictionary")

is_present(3)
is_present(8)


"""
6. Write a Python script to generate and print a dictionary that contains 
   a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
n=int(input("Enter"))
d={x:x*x for x in range(1,n+1) if x%2==0}
print(d)


"""
7. Write a Python script to print a dictionary where the keys are numbers 
between 1 and 15 (both included) and the values are the square of the keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
"""

dict_square={x:x*x for x in range(1,16)}
print(dict_square)

"""
8. Write a Python script to merge two Python dictionaries.
"""
di1={1:10, 2:20}
di2={3:30, 4:40}
di3={}
for e in (di1,di2):
    di3.update(e)
print(di3)

"""
10. Write a Python program to sum all the items in a dictionary.

"""
dict_square={x:x*x for x in range(1,16)}
print(dict_square)
key_sum=0
values_sum=0
sum_items={}
for x,y in dict_square.items():
    key_sum+=x
    values_sum+=y
#print(key_sum)
#print(values_sum) 
sum_items.update({key_sum:values_sum})
print(sum_items)   


"""
11. Write a Python program to multiply all the items in a dictionary.

"""
dict_square={x:x*x for x in range(1,16)}
print(dict_square)
key_mul=1
values_mul=1
mul_items={}
for x,y in dict_square.items():
    key_mul*=x
    values_mul*=y
#print(key_sum)
#print(values_sum) 
mul_items.update({key_mul:values_mul})
print(mul_items)   


"""
12. Write a Python program to remove a key from a dictionary.

"""
dict_square={x:x*x for x in range(1,16)}
print(dict_square)
dict_square.pop(5)
print(dict_square)

"""
13. Write a Python program to map two lists into a dictionary.

"""
l1=[1,2,3,4,5,6,7,8,9]
l2=[10,20,30,40,50,60,70,80,90]
d={}
mapped_2_lists=dict(zip(l1, l2))
print(mapped_2_lists)

"""
14. Write a Python program to sort a given dictionary by key. And output should be a dictionary.

"""
d1={'adfdf':4654,'dfsf':897,'rtet':1321,'oiuio':3545,'vnmbn':3639}
sorted_keys=sorted(d1.keys())
print(sorted_keys)

"""
15. Write a Python program to get the maximum and minimum values of a dictionary.

"""
d1={'adfdf':4654,'dfsf':897,'rtet':1321,'oiuio':3545,'vnmbn':3639}
print("Maximum value:",max(d1.values()))
print("Maximum value:",min(d1.values()))

"""
19. Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

"""
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
#counter_d={}
for k1,v1 in d1.items():
    for k2,v2 in d2.items():
        if k1==k2:
            v1+=v2
            print(v1)
            counter_d.update({k1:v1})
            print(counter_d)

"""
20. Write a Python program to print all distinct values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

"""
#Method 1
list1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
s1=set()
for dictionary in list1:
    for value in dictionary.values():
        s1.add(value)
print(s1)

#Method 2
list1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
d2=set([value for dictionary in list1 for value in dictionary.values()])
print(d2)

"""
21. Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
"""
l1=[]
dict1={'1':['a','b'], '2':['c','d']}
l1=list(dict1.values())
for i in l1[0]:
    for j in l1[1]:
        print(i+j)
            
"""
22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
"""
d1={'adfdf':4654,'dfsf':897,'rtet':1321,'oiuio':3545,'vnmbn':3639}
d1_sorted=sorted(d1.values(),reverse=True)
print(d1_sorted)
max_3_values=d1_sorted[:3]
print(max_3_values)


"""
23. Write a Python program to combine values in a list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})
"""
l1=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
key=[k,v for d in l1 for k,v in d ]
print(key)


a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
cp={}
val=0
for d in a:
    if d['item'] not in cp:
        cp[d['item']]=d['amount']
    else:
        cp[d['item']]+= d['amount'] 
print(cp)

"""
24. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

"""

st='w3resource'
dic = {} 
for ch in st:
    if ch in dic:
        dic[ch] += 1
    else:
        dic[ch] = 1 
print(dic)




"""
80. Write a Python program to find the key of the maximum and minimum value in a dictionary.
Sample Output:
Original dictionary elements:
{'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
Finds the key of the maximum and minimum value of the said dictionary:
('Roxanne', 'Theodore')
"""
d1={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
print(d1['Theodore'])

m=max(d1.values())
small=min(d1.values())
print("max",m)
print("min",small)
t=[]
for x,y in d1.items():
    if y==m:
       t.append(x) 
    elif y==small:
        t.append(x)
print(tuple(t))            
    



