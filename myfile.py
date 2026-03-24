# coding python
#------------CLASS 1----------------------#
# print("Hello Aditya singh","You are a coder")
# print(88+99)
# name = "Aditya"
# a =26
# print(name  +" Age   "+  str(a))
# print(type(name))
# print(type(a))
# a=None
# print(type(a))
# a=100
# b=400
# c=a+b
# print(c)
#-----------------------
# a=35
# b=97
# c=a%b
# print(c )
# ---------------------

# a=551
# b=5
# c=a%b
# print(c)
# -------------------------

# name1 ="Aditya"
# name2 ="Singh"
# print(name1+ "   "+name2)
# --------------------------


# a =22
# b=11
# c=9
# print(a>b or c>a)
# ---------------------------


#Typecasting
# a = 4.5
# b=(int)("7")
# print(a+b)


#-------------------
# Conversion
# a=5
# b=99.99
# print(a+b)



#----------------------------

######INPUT IN PYTHON######
# input is always string we have to convert explicitely
# a=input("Enter your num     ")
# print(type(a))

# name =input("Enter name")
# age = input("Enter age")
# marks = input("Enter marks")

# print("Name is "+name ,"Age is "+ age ,"Marks is" + marks)



#----------------Class 2--------------------#

#String and conditional Statements

# str1 ='String1'
# str2 ="String2"
# str3 ='''String3'''

#Escape Secquance
# str1 ="Aditya singh is code .\nhe is working"
# print(str1)

#Operation on String
# str1="Aditya"
# str2="Singh"
# str3 =str1+"  "+str2
# print(str3)

# str ="Aditya      singh"
# print(len(str))  op 17


# str = "Adityasingh"
# print(str[4])   only acces allowed not modify

#Slicing in string
# str ="Aditya singh is a coder"
# print(str[1:5])


# str ="Adityasingh is king "
# print(str[0:len(str)])

#--------------------------------------

#String Functions

# str ="i am studing python"
# print(str)
# print(str.endswith("on"))
# print(str.capitalize())
# str1= str.replace("am","yes")
# print(str1)

# str ="Aditya"
# print(str)

# str ="Singh"
# print(str)


#----------------Conditional Statements--------------#

#voting 18 and 18+

# age =(int) (input("Enter age    "))

# if (age < 18):
#     print("Minor")
# elif (age == 18):
#     print("Just Adult")
#     print("Vote")
# else:
#     print("Adult")
#     print("Vote")


# In python there is no concept of {  } block for multiple lines of code 
# here we use proper spacing which is known as INDUCTATION in python for multi line of code 
# This is very important concept in python 

# marks = int(input("Enter marks: "))

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 60:
#     print("Grade: C")
# elif marks >= 40:
#     print("Grade: D")
# else:
#     print("Grade: F")

#------------NESTING----------------#


# marks = int(input("Enter marks: "))

# if marks >= 40:
#     print("Pass")
    
#     if marks >= 60:
#         print("1st div")
#     else:
#         print("2nd div")
# else:
#     print("Fail")



# num = int( input("Enter the number  "))
# if(num==0):
#     print("Number is zero 0")
# elif(num%2==0):
#     print("Even")
# else:
#     print("NOt a even number")
#--------------------------------------------

#---------------CLASS 3-------------------#
    #LIST AND TUPLES
    #1 List   =  Mutabble
# marks1 = 99
# marks2 =77
# marks3 =45
# marks4= 79

# marks=[44,6,56,5,65,7,6,7]
# print(marks[3])  
# print(type(marks))  

# java k list m same type ka values hota hai string integer int
# Lekin python m ye alag alag type ka ho sakta hai 
# Jse String int float

# student =["Aditya",25,"Bsp"]
# print(student[2])  # if we give out of range  - show out of range exception

#Muttable
# student =["Aditya",25,"Bsp"]
# student[0]="Akhilesh"
# print(student[0]) 

#in list slicing is also possible
# Slicing with negative indexing is also there

      #Methods in List#
      
      # List methods in Python

# List methods in Python

# lst = [1, 2, 3]
# print("Initial List:", lst)

# # append()
# lst.append(4)
# print("After append:", lst)

# # insert()
# lst.insert(1, 10)
# print("After insert:", lst)

# # extend()
# lst.extend([5, 6])
# print("After extend:", lst)

# # remove()
# lst.remove(10)
# print("After remove:", lst)

# # pop()
# lst.pop()
# print("After pop (last):", lst)

# lst.pop(1)
# print("After pop (index 1):", lst)
 

# # count()
# print("Count of 2:", lst.count(2))

# # sort()
# lst.sort()
# print("After sort:", lst)

# lst.sort(reverse=True)
# print("After sort (descending):", lst)

# # reverse()
# lst.reverse()
# print("After reverse:", lst)

# # copy()
# new_lst = lst.copy()
# print("Copied List:", new_lst)

# # clear()
# lst.clear()
# print("After clear:", lst)



#------------Tupples-------------#\
    #Same as List But List is mutable where as Tupples are immutable#
    
# tup =(3,54,5,46,99)
# print(type(tup))    
# tup=("Aditya",17,False)
# print(tup[0])
# tup[0] ="Adi"  -- NOt allowed

#Methods in tuples

# t = (10, 20, 30, 20)

# print(t.index(20))  # Output: 1
# len(t)
# max(t)
# min(t)
# sum(t)

#-----------------Class4--------------#
# Dictionary And sets
# Dictonary is muttable
# key- value pair 
# search by Key
# In majority keys are String
# No order
# No Duplicate Key

# dict ={
#     "Name":"Aditya",
#     "Age":"25",
#     "Language": "Java"
# }

# print(dict["Language"])
# print(dict)
# dict["Name"] ="Adi"
# print(dict["Name"])


# Empty dictonary

# dect ={}
# print(dect)

# Student ={
#     "Name" : "Aditya",
#     "Marks":{
#         "Phy":"88",
#         "che":89,
#         "Maths":98
#     },
#     "School":"Vita"
#     }
# print(Student)
# print(Student["Marks"]["Phy"])

# # Sample dictionary
# d = {"name": "Aditya", "age": 23, "city": "Pune"}

# # 1. keys() -> returns all keys
# print(d.keys())

# # 2. values() -> returns all values
# print(d.values())

# # 3. items() -> returns key-value pairs
# print(d.items())

# # 4. get() -> get value by key (safe way)
# print(d.get("name"))

# # 5. update() -> update dictionary
# d.update({"age": 24})
# print(d)

# # 6. pop() -> remove element by key
# d.pop("city")
# print(d)

# # 7. popitem() -> removes last inserted item
# d.popitem()
# print(d)

# # 8. clear() -> removes all items
# d.clear()
# print(d)

# # 9. copy() -> creates a copy of dictionary
# d1 = {"a": 1, "b": 2}
# d2 = d1.copy()
# print(d2)

# # 10. setdefault() -> returns value of key, if not present inserts it
# d1.setdefault("c", 3)
# print(d1)

# # 11. fromkeys() -> create new dictionary from keys
# keys = ("x", "y", "z")
# new_dict = dict.fromkeys(keys, 0)
# print(new_dict)

#-------------Set--------------#
# Unique
# Immutable
# Unorder

# nums ={"Aditya",21,"Singh",True,21}
# print(nums)
# --op is not in proper odere
# - length not count duplicate

#-----EmptySet

#std ={}  ye bydefault dectionary hoga empty dictonary  to create empty set

# collection =set()
# print(type(collection))  op set

# # Sample sets
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}

# # 1. add() -> adds one element
# s1.add(10)
# print(s1)

# # 2. update() -> adds multiple elements
# s1.update([20, 30])
# print(s1)

# # 3. remove() -> removes element (error if not present)
# s1.remove(2)
# print(s1)

# # 4. discard() -> removes element (no error if not present)
# s1.discard(100)

# # 5. pop() -> removes random element
# s1.pop()
# print(s1)

# # 6. clear() -> removes all elements
# temp = {1, 2}
# temp.clear()
# print(temp)

# # 7. union() -> combines sets
# print(s1.union(s2))

# # 8. intersection() -> common elements
# print(s1.intersection(s2))

# # 9. difference() -> elements in s1 but not in s2
# print(s1.difference(s2))

# # 10. symmetric_difference() -> elements not common
# print(s1.symmetric_difference(s2))

# # 11. issubset() -> check subset
# print({1, 2}.issubset(s1))

# # 12. issuperset() -> check superset
# print(s1.issuperset({1, 2}))

# # 13. isdisjoint() -> no common elements
# print(s1.isdisjoint({100, 200}))

#------------Class5-----------------#
#Loops Repatative task
# types of Look
# 1- for
# 2- While loop
# while True:
#     print("Hello")

# count = 1
# while (count <= 10):
#     print("Aditya", count)
#     count = count + 1

# Table
# count = 1
# num = int(input("Enter num    "))
# while (count <= 10):
#     print(num* count)
#     count = count + 1


#-- Break and continue



#FOR LOOP IN JAVA
# num=[4,34,35,4,645,65,9]
# for var in num:
#     print(var)

#Range in py
# for i in range(10):
#     print(i)

#range(start, stop, step)

# Empty Loop
# for a in range(10):
#     pass 


# print("Hello")
#--------------------Class 6 (Function)------------------#
# Use for repatative task

#function definat
# def fun(a,b=99):
#     sum = a+b 
#     return sum

#function call
# n = fun(3)
# print(n)

#types of function
#Built in function and user define function
 
 
#-------Class_8---OPPS CONCEPTS----------------#
#Functio - reduce redudency and inc code re-uslbility

# class student:
#     name ="Aditya"
#     age =12
    
# s1 = student()
# ans =s1.name
# print(ans)

# class car:
#     colour ="White"
#     Brand ="Benz"
#     cost =100000000
    
# c1 = car()
# print(c1.colour)

# class k andar methods and attributes

# class Student:
    
#     @staticmethod  // Decorater
#     def greet():
#         print("Hello, this is a static method")

# # calling static method
# Student.greet() 

#Piller of Opps 
# 1- Abstraction
# 2- Encpulation
# 3- Inheritence
# 4- Polymoriphism


#                  del keyword

# class Student:
#     name = "Aditya"
#     age = 12

# s1 = Student()

# del s1   # object deleted

# print(s1) 


# VVIP (Access specifier in python )

#1- Private   ==    __name    (abb ye private ban jaayega)

# class person:
#     __name ="Aditya"
    
# p1 = person()
# print(p1.__name)



# inheritence 
#   1 - Single
#   2 - Multiple
#   3 - Multilevel

# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):   # inheritance
#     def bark(self):
#         print("Dog barks")

# d = Dog()
# d.sound()   # inherited method
# d.bark()

#Yes, static methods are inherited in Python.


# Super keyword in python

# class Parent:
#     def __init__(self):
#         print("Parent constructor")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()   # calling parent constructor
#         print("Child constructor")

# c = Child()

#        CLASS METHOD DECORATOR
# def my_decorator(cls):
#     cls.new_attr = "Added by decorator"
#     return cls

# @my_decorator
# class Student:
#     name = "Aditya"

# s1 = Student()
# print(s1.name)
# print(s1.new_attr)



#-------------------------------Class , instance , and static method in same class------------------#
# class Student:
    
#     school = "ABC School"   # class variable
    
#     def __init__(self, name, age):
#         self.name = name    # instance variable
#         self.age = age

#     #  Instance Method
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("School:", Student.school)

#     #  Class Method
#     @classmethod
#     def change_school(cls, new_name):
#         cls.school = new_name

#     #  Static Method
#     @staticmethod
#     def greet():
#         print("Welcome to Student Class")

# # object
# s1 = Student("Aditya", 22)

# # calling instance method
# s1.display()

# # calling class method
# Student.change_school("XYZ School")

# # calling static method
# Student.greet()

# # check updated value
# s1.display()
 
# @property is used to convert a method into a variable-like attribute.
#@getter and Setter decorater
 
# class Student:
    
#     def __init__(self, marks):
#         self.marks = marks

#     @property
#     def percentage(self):
#         return (self.marks / 500) * 100

# s1 = Student(400)

# print(s1.percentage)   

#--------------Polymorphism----------------#
#Operator overloading is support in python



#-------FILE IO---------#

# file =open("my.txt","r")
# data = file.readline()
# print(data)
# file.close

# Writing

# ip = input(print("TYPE "))
# with open("my.txt", "w") as file:
#     file.write(ip)

# # Reading
# with open("my.txt", "r") as file:
#     content = file.read()
#     print(content)

#----AUTO CLOSE-----#
# with open("my.txt","r") as f:
#    data = f.read()
#    print(data)

#--------MODULE IN PYTHON------------#
# import os
# os.remove("my.txt")
    
    
    