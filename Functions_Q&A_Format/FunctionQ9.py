# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:36:52 2023

9. Create a function "cloth_details" with three arguments, color, shape and size.
 All three are optional and can be passed in any sequence by the user.
 
@author: DBDA
"""

def cloth_details(color='Blue',shape='Slim Fit',size='38'):
    print(f'Color->{color}, Shape->{shape}, Size->{size}')
   
color,shape,size=input("Enter cloth Color,Shape and Size-->").split()
print()
cloth_details(color,shape,size)

cloth_details(color,shape)

cloth_details(color)

cloth_details()