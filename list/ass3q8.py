# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:45:02 2023

8. Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Sub List to be added = ["h", "i", "j"]
output:
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n'] 

@author: DBDA
"""

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2= ["h", "i", "j"]
for e1 in list2:
    list1[2][1][2].append(e1)
print(list1)
