# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:35:26 2023

8. Write a function which takes all details of a person as input in sequence
 and prints details as follows
(Hint: Think which type of parameter to be used for every option)
a. Take name and Print it in Camel Case
b. Take 10 digit Mobile No and print it appending +91
c. Take location as optional value. If not given then print India
d. Take Qualifications. Qualifications can be 1 or 2 or many.
Print all the passed qualifications one by one. Default qualification is "Human"

@author: DBDA
"""

def person_details(name,mb,/,loc="India",qal="Human"):
    camel_case=name.title().replace(" ","")
    Mobile_no='+91'+mb
    location=loc
    Qualifications=qal
    print(f' Person Details-->Name:-{camel_case},\n Mobile_no:-{Mobile_no},\n location:-{location},\n Qualifications:-{Qualifications}\n\n')
    
name=input(" Enter name of a person-->")
mb=input(" Enter mobile number-->")
qal=input(" Enter Qualifications of a person-->")
loc=input(" Enter location of a person-->")
print()

person_details(name,mb)




















