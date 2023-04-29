# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:06:39 2023

7. given a list of strings.
every string is in format "Emp_name:Emp_id"
Emp_id is always a number
if emp_id is amstrong number then rotate emp_name 1 place to the right -->
 and print the emp_name
if emp_id is a prime no then print vowels from the employee name
in other cases print consonents from the emp name
Finally there should be print of every employee name as per given condition

@author: DBDA
"""
def rotate_r_if_amstrong_no(s):
    s1=s[1:]+s[:1]
    print("Your Emp_id:-{Emp_id} is Amstrong no.,\n So your Emp_name:-{Emp_name} is rotated to right by 1 place:-",s1)

def print_Vow_if_prime(Emp_name):
    vowels="AaEeIiOoUu"
    v= [e for e in Emp_name if e in vowels]
    print("Your Emp_id:-{Emp_id} is Prime no.,\n So vowels from your Emp_name:-{Emp_name} is/are:-",v)

def print_Cons_if_prime(Emp_name):
    consonents="BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"
    c= [e for e in Emp_name if e in consonents]
    print("Your Emp_id:-{Emp_id} is neither Amstrong no. nor Prime no.,\n So Consonents from your Emp_name:-{Emp_name} is/are:-",c)

#Input from the user in the Format-->Emp_name:Emp_id
Emp_name=input("Enter Employee Name: ").title()
Emp_id=int(input("Enter Employee id: "))
print(f"{Emp_name}:{Emp_id}")


#To check whether the no is Amstrong no or not
d1=(Emp_id%10)**(Emp_id%10)
d2=((Emp_id//10)%10)**((Emp_id//10)%10)
d3=((Emp_id//10)//10)**((Emp_id//10)//10)
amstrong_no=d1+d2+d3

#To check no is prime or not
for i in range(1,Emp_id):
    if (i%1==0) & (i%i==0):     
        prime=True 
 
#Function Call
if Emp_id==amstrong_no:
    rotate_r_if_amstrong_no(Emp_name)
elif Emp_id==prime:
    print_Vow_if_prime(Emp_name) 
else:
    print_Cons_if_prime(Emp_name)  












