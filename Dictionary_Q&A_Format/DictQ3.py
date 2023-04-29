# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 22:18:24 2023

3. Write a menu driven program to practice Dictionary functions.
Write a program to accept name of a person and their vehicle and store it in a dictionary.
Ask user if they want to continue to accept multiple values.
Display following menu:
    
a. Add new person name and a vehicle name.
b. Delete a person name and vehicle name from the dictionary.
----Accept person name from user.
----Check whether person name exists in the dictionary.
----If exists show person name and vehicle name to the user.
----Confirm for deletion, if user enters y
then delete otherwise no. Display appropriate message.
c. Modify vehicle name for the person
----Accept a person name from user.
----Check whether the person’s name exists.
----If the name exists, show the person’s name and vehicle name to user.
  Ask for new value and then overwrite the old value.
d. Search vehicle for the given person’s name.
e. Search list of people, who have given a vehicle
f. Display all person names.
g. Display all vehicle names.
h. Exit


@author: DBDA
"""
person_vehicle= {}
name = input('Enter name of a person-')
vehicle = input('Enter name of  their vehicle-')
person_vehicle[name] = vehicle
print(person_vehicle)

print("       a: Add new person name and a vehicle name. \n \
        b: Delete a person name and vehicle name from the dictionary.\n \
        c: Modify vehicle name for the person. \n \
        d: Search vehicle for given person's name. \n \
        e: Search list of people, who have given a vehicle. \n \
        f: Display all person names.\n \
        g: Display all vehicle names.\n \
        h: Exit \n ")
choice=input("Enter your choice from above: ")

if choice=='a':
    
    name = input('Enter name of a person-')
    vehicle = input('Enter name of  their vehicle-')
    person_vehicle[name] = vehicle
    print(person_vehicle)

elif choice=='b':
       name = input('Enter name of a person-')
       if name in person_vehicle:
            print(person_vehicle[name])
            ch = input("Enter 'y' to conform deletion")
            if ch == "y":
                del person_vehicle[name]
                print("deleted.")
            else:
                print("No such name exists.")
elif choice == 3:
        name = input('Enter name you want to modify:')
        if name in person_vehicle:
            vehicle = input('Enter new vehicle :')
            person_vehicle[name]=vehicle
            print(person_vehicle)
        else:
            print("No such name exists.")
elif choice == 4:
        name = input('Enter name you want to search:')
        if name in person_vehicle:
            print(name,person_vehicle[name])
        else:
            print("No such name exists.")
elif choice == 5:
        vehicle = input('Enter vehicle :')
        name = [i for i in person_vehicle if person_vehicle[name]==vehicle]
        print(name)
elif choice == 6:
        print(person_vehicle.keys())
elif choice == 7:
        print(person_vehicle.values())
elif choice == 8:
        print("Exit!")
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    