# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:20:20 2023

1. Write a program to create a class song add songid,lyrics,singer name,
create SongService class add function to
addsong() to accept a song details and store it in array
displayAllsongs---- to display all songs
displayByActor(String name) ---- display all songs of a particular singer, pass singername as
-----a parameter to the function

@author: DBDA
"""

class song:
    def addsong(self):
        self.l1=[]
        self.songid=int(input("Enter song id: "))
        self.lyrics=input("Enter lyrics of song: ")
        self.singer_name=input("Enter singer name: ")
        self.l1.append({'songid':self.songid})
        self.l1.append({'lyrics':self.lyrics})
        self.l1.append({'singer_name':self.singer_name})
        
        
    def displayAllsongs(self):
        print("Song id: ",self.songid)
        print("Song Lyrics: ",self.lyrics)
        print("Singer Name : ",self.singer_name)
        print("songs Album:",self.l1)
        
    def displayBySinger(self,name):
        
        if (self.l1[2]['singer_name']==name):
            print(f"Singer with name {name} found: ",self.singer_name)
            print("song lyrics: ",self.lyrics)
            print("song id: ",self.songid)
        else:
            print(f"singer with name {name} not found")
        
song_list=[]
n=int(input("Enter No. of Albums:"))
for i in range(n):
    song_list.append(0)
    song_list[i]=song()
    song_list[i].addsong()
    
print(song_list)
while True:
    print("Total number of albums: ",len(song_list))
    print("1: Add song to the album. ")
    print("2. Display Album. ")
    print("3. Search by name. ")
    print("4. Exit. ")
    print("\n\n")

    try:     
        choice=int(input("Enter choice: "))
        if choice==1:
           for i in range(n):
               song_list[i].addsong()
        elif choice==2:
            for i in range(n):
                song_list[i].displayAllsongs()
        elif choice==3:
            name=input("Enter singer name to be searched:-")
            for i in range(n):
                song_list[i].displayBySinger(name)
        elif choice==4:
             break
        else:
            raise Exception
    except Exception:
        print("you entered invalid choice")
        
        
        
        
        
        
"""
Q2. Write a python program to store information of your friends
id,name,lastname,hobbies,mobno,email,bdate,address
note: hobbies- a friend may have multiple hobbies

Accept all friends details and store it in a list
And do the following.
1. Display All Friend
2. Search by id
3. Search by name
4. Display all friend with a particular hobby
5. Exit
"""

class friends:
    def friend_info(self):
        self.l1=[]
        self.fid=int(input("Enter Friend's id: "))
        self.l1.append({'Fid':self.fid})
        self.fname=input("Enter friend's first name: ")
        self.l1.append({'First Name':self.fname})
        self.lastname=input("Enter friends's last name: ")
        self.l1.append({'Last name':self.lastname})
        self.hobbies=input("Enter friend.s Hobbies: ")        
        self.l1.append({'Hobbies':self.hobbies})
        self.mobno=int(input("Enter Friend's mobile No.: "))
        self.l1.append({'Mobile No ':self.mobno})
        self.email=input("Enter Friend's Email: ")
        self.l1.append({'Email ':self.email})
        self.bdate=input("Enter Friend's Birth Date: ")
        self.l1.append({'Birthdate':self.bdate})
        self.addr=input("Enter Friend's Address: ")
        self.l1.append({'Address':self.addr})
        
    def display_all_friends(self):
        print("Friend's id:",self.fid)
        print("         first name:",self.fname)
        print("         last name:",self.lastname)
        print("         Hobbies:",self.hobbies)
        print("         Mobile Number:",self.mobno)
        print("         Email:",self.email)
        print("         Birth Date:",self.bdate)
        print("         Address:",self.addr)
        print(self.l1)
    def search_name(self,name):
        if self.fname==name:
            print(f"friend's info with friend name:-{name} found as:",self.fname)
            print("         last name:",self.lastname)
            print("Friend's id:",self.fid)
            print("         Hobbies:",self.hobbies)
            print("         Mobile Number:",self.mobno)
            print("         Email:",self.email)
            print("         Birth Date:",self.bdate)
            print("         Address:",self.addr)

a=friends()
a.friend_info()
a.display_all_friends()



"""
3
"""





class Student:
    def student_input(self):
        self.studid=int(input("Enter Student ID:"))
        self.student_name=input('Enter Student name:')
        self.Marks1=int(input("Enter marks of sub1"))
        self.Marks2=int(input("Enter marks of sub2"))
        self.Marks3=int(input("Enter marks of sub3"))
    
    def display_Student(self):
        print("Student ID:",self.studid)
        print("Name of Student:",self.student_name)
        print("Total Marks Of Student",(self.Marks1+self.Marks2+self.Marks3))
    def search_id(self,ID):
        if self.studid==ID:
            print("Student Found",self.studid)
            print("Name OF Student",self.student_name)
            return True
    def Search_name(self,name):
        if self.student_name==name:
            print("Student Found",self.studid)
            print("Name OF Student",self.student_name)
    def Calculate_gpa(self):
        gpa=(1/3)*self.Marks1+(1/2)*self.Marks2+(1/4)*self.Marks3
        return gpa


student_list=[]
n=int(input("Enter No. of Classes:"))
for i in range(n):
    #student_list.append(0)
    student_list.append(Student())
    #student_list[i]=Student()        
    student_list[i].student_input()
    
while True:
    print("\n\n")
    print("Total Number Of student:",len(student_list))
    print("1.Display All Students")
    print("2.Search By ID")
    print("3.Search by Name")
    print("4.calculate student GPA")
    print("5.Exit")
    print("\n\n")
    try:
        choice=int(input("Enter choice"))
        if choice==1:
            for i in range(n):
                student_list[i].display_Student()
        elif choice==2:
            id_no=int(input("Enter search ID number"))
            for i in range(n):
                student_list[i].search_id(id_no)
        elif choice==3:
            stud_name=input("Enter search name")
            for i in range(n):
                student_list[i].Search_name(stud_name)
        elif choice==4:
            ID_student=int(input("Enter ID of student you Want CPG of."))
            for i in range(n):
                if student_list[i].search_id(ID_student)== True:
                    print("CGPA of a Student:",student_list[i].Calculate_gpa())
        elif choice==5:
            break
        else:
            raise Exception
    except Exception:
        print("You Entered Invalid Choice")










