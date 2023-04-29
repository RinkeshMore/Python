# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 23:49:01 2023
 5. Take a sentence as input from user. Every word is seperated by space. 
 a. Create a word_count dictionary which will have unique words and their count. 
 b. create suffix_count dictionary which will contain count of words ending with 's', 'es', 'ed', 'y', 'en'
 c. create dictionary word_length_count which will store length of word and count.
 Ex. 
 input_sent= 'CDAC is in Pune'
 There are 2 words of length 4 and 2 words of length 2 so,
 word_length_count = {2:2, 4:2}
@author: DBDA
"""



sentence=input("please type a sentence a please")

list1=sentence.split(" ")
set1=set(list1)

output={}
for word in set1:
    output[word]=list1.count(word)
print(output)




sentence="please types a sentence a please pen pen ted red "
suffix=['s', 'es', 'ed', 'y', 'en']
suffix_count={}
lister=sentence.split(" ")
print(lister)
list_length=[]
list_count=[]
for word in lister:
    if word.endswith('s'):
        if 's' in suffix_count:
            suffix_count['s'] += 1
        else:
            suffix_count['s'] = 1
    if word.endswith('es'):
        if 'es' in suffix_count:
            suffix_count['es'] += 1
        else:
            suffix_count['es'] = 1
    if word.endswith('ed'):
        if 'ed' in suffix_count:
            suffix_count['ed'] += 1
        else:
            suffix_count['ed'] = 1
    if word.endswith('y'):
        if 'y' in suffix_count:
            suffix_count['y'] += 1
        else:
            suffix_count['y'] = 1
    if word.endswith('en'):
        if 'en' in suffix_count:
            suffix_count['en'] += 1
        else:
            suffix_count['en'] = 1

print(suffix_count)


sentence=input("please type a sentence a please")
word_count={}
lister=sentence.split(" ")
print(lister)
list_length=[]
list_count=[]
for i in lister:
    list_length.append(len(i))
print(list_length)
    
set1=set(list_length)
print(set1)

for idx in set1:
    list_count.append(list_length.count(idx))
print(list_count)    

list2=list(set1)


base=dict(zip(list2,list_count))

print(base)

