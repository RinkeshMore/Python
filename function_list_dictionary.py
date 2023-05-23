# -*- coding: utf-8 -*-
"""
Created on Mon May 22 17:07:58 2023

@author: DBDA
"""

'''wap assume list as input to the function list contains data of student information
similar to mongodb 
structure of every obj
studid:123
mark:[32,54,76]
Qualification:{10:90,12:65,Btech:89}
find the second toppper in all qualification
(take avg of all the marks)
'''

#stud_info=[{"studid":0,"marks":[0],"qualification":{"10th":0,"12th":0,"BTech:":0}}]

stud_info=[]
avg=0
avrage=[]
avg_dict={}
def stud_details(n):
    stud_dict={}
    
    for i in range(1,n+1):
        print("student=",i)
        id=int(input("enter studid "))
        m=input("enter marks giving spaces")
        marks=m.split(" ")
        ssc=int(input("enter 10th marks"))
        hsc=int(input("enter 12th marks"))
        BTech=int(input("enter Btech marks"))
        avg=(ssc+hsc+BTech)//3
        avrage.append(avg)
        avg_dict[id]=avg
        qual={"10th":ssc,"12th":hsc,"B_Tech":BTech}
        stud_dict={"studid":id,"marks":marks,"Qualification":qual}
        stud_info.append(stud_dict)

n=int(input("enter number of students"))

stud_details(n)

print(stud_info)

print(avrage)

avrage.sort()

print(avrage)


second_topper=avrage[-2]

print(avg_dict)

e= iter(avg_dict)

for i in e:
    if avg_dict[i]==second_topper:
        print("second topper id :",i)


        
        
        


        
        













