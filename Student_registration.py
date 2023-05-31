from asyncore import write
from calendar import c
import datetime
from os import system, name
from time import sleep
from operator import truediv
import random
date=datetime.datetime.now()
def file():
    f = open('Student Registration.txt', 'a')
    f.write("Student Information: ")
    f.write("\nStudent Number: ")
    f.write(std)
    f.write("\nStudent Name: ")
    f.write(inf.name)
    f.write("\nAge: ")
    f.write(inf.age)
    f.write("\nAddress: ")
    f.write(inf.address)
    f.write("\n")
    f.write(c)
def clear():
    if name == 'nt':
        _ = system('cls')
def st_num():
    num = []
    for x in range (5):
        x = random.randrange(1,10)
        num.append(x)
    print("Student ID: ", end = '')
    for i in num:
        f = open('Student Registration.txt', 'a')
        f.write(str(i))
        f.close
        print(i, end = '')
    print()   
        
def display_courses():
    print("1. Bachelor of Science in Information Technology (BSIT)")
    print("2. Bachelor of Science in Computer Science (BSCS)")
    print("3. Bachelor of Science in Software Engineer (BSSE)")
    print("4. Bachelor of Science in Information System (BSIS)")
    print("5. Bachelor of Science in Web Application Development (BSWAD)")
def picked_course(p):
    if p == 1:
        f = open('Student Registration.txt', 'a')
        f.write("Course: Bachelor of Science in Information Technology (BSIT)")
        f.close
    elif p == 2:
        f = open('Student Registration.txt', 'a')
        f.write("Course: Bachelor of Science in Computer Science (BSCS)")
        f.close
    elif p == 3:
        f = open('Student Registration.txt', 'a')
        f.write("Course: Bachelor of Science in Software Engineer (BSSE)")
        f.close
    elif p == 4:
        f = open('Student Registration.txt', 'a')
        f.write("Course: Bachelor of Science in Information System (BSIS)")
        f.close
    elif p == 5:
        f = open('Student Registration.txt', 'a')
        f.write("Course: Bachelor of Science in Web Application Development (BSWAD)")
        f.close
class students:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
rep = True
while rep == True:
    f = open('Student Registration.txt', 'w')
    f.write("")
    f.close
    clear()
    n = input("Enter your name: ")
    a = input("Enter your age: ")
    ad = input("Enter your address: ")
    inf = students(n, a, ad)
    print("Pick a course you want to pursue: ")
    display_courses()
    p = int(input("Pick a course you want to take: "))
    picked_course(p)
    f = open('Student Registration.txt', 'r')
    c = f.readline()
    f.close
    f = open('Student Registration.txt', 'w')
    f.write("")
    f.close
    clear()
    print("You are now successfuly enrolled.")
    print("Here is your information: ")
    print("Name: ", end='')
    print(inf.name)
    print("Age: ", end = '')
    print(inf.age)
    print("Address: ", end = '')
    print(inf.address)
    st_num()
    f = open('Student Registration.txt', 'r')
    std = f.readline()
    f.close
    f = open('Student Registration.txt', 'w')
    f.write("")
    f.close
    file()
    ans = input("Do you want to register again? y/n: ")
    if ans == "y":
        rep = True
    else:
        rep = False
