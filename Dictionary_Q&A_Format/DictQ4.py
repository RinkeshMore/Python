# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 23:45:15 2023

4. Write a program to display following menu and do the following:
a. Add new city and trees commonly found in the city.
b. Display all cities and the list of trees for all cities.
c. Display list of trees of a particular city.
---- Accept a city from user search city and if found display list of trees otherwise
---- Display message not found
d. Display cities which have the given tree.
---- Accept a tree name from user and display all cities in which the tree is found.
e. Delete city ---- Accept city from user and delete the city if found.
---- Prompt user before deletion
f. Modify tree list
---- Accept city and trees to be added in the city. if city exist add trees at the end of the list
---- Otherwise add city and list
g. Exit
@author: DBDA
"""





while True:
    print("Menu:")
    print("a. Add new city and trees commonly found in the city.")
    print("b. Display all cities and the list of trees for all cities.")
    print("c. Display list of trees of a particular city.")
    print("d. Display cities which have the given tree.")
    print("e. Delete city")
    print("f. Modify tree list")
    print("g. Exit")

    choice = input("Enter your choice: ")
tree_dict={}
if choice == "a":
        city = input("Enter city name: ")
        trees = input("Enter comma separated list of trees found in the city: ").split(",")
        tree_dict[city] = trees
        print("City and trees added successfully!")

elif choice == "b":
        if len(tree_dict) == 0:
            print("No cities found!")
        else:
            print("Cities and trees:")
            for city, trees in tree_dict.items():
                print(city + ":", ", ".join(trees))

elif choice == "c":
        city = input("Enter city name: ")
        if city in tree_dict:
            print("List of trees in", city + ":", ", ".join(tree_dict[city]))
        else:
            print("City not found!")

elif choice == "d":
        tree = input("Enter tree name: ")
        cities = []
        for city, trees in tree_dict.items():
            if tree in trees:
                cities.append(city)
        if len(cities) == 0:
            print("Tree not found in any city!")
        else:
            print("Cities where", tree, "is found:", ", ".join(cities))

elif choice == "e":
        city = input("Enter city name: ")
        if city in tree_dict:
            confirm = input("Are you sure you want to delete " + city + " and its tree list? (y/n): ")
            if confirm == "y":
                del tree_dict[city]
                print(city + " and its tree list deleted successfully!")
        else:
            print("City not found!")

elif choice == "f":
        city = input("Enter city name: ")
        trees = input("Enter comma separated list of trees to be added: ").split(",")
        if city in tree_dict:
            tree_dict[city] += trees
            print("Trees added to", city + " successfully!")
        else:
            tree_dict[city] = trees
            print("City and trees added successfully!")

elif choice == "g":
        print("Exiting program...")
    #break

else:
        print("Invalid choice! Please try again.")
