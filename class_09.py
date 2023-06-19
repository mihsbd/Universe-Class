#-# Class #9 - Class, Objects & Inheritance (OOP)


## 1. Class & Objects
# class Student:      # class
#     roll = ""       # attribute
#     subject = ""

# kamal = Student()   # object 
# kamal.roll = 3
# kamal.subject = 'English'
# print("Kamal's Roll is {kamal.roll} and Subject is {kamal.subject}")


## 2. Methods vs Functions & Magic (dunder) Methods
# class Room:
#     length = 0.0
#     width = 0.0

#     def calculate_area(self):
#         print("Area of the Room = ", self.length * self.width)

# room = Room()   # object 
# room.length = 40.5
# room.width = 40.5
# room.calculate_area()

#> Magic (dunder) Methods:-
# __init__()
# __str__()


## 3. Inheritance in Python
# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.year = year

#     def display(self):
#         print("Welcome", self.fname, self.lname, self.year)

#     def roll(self, digit):
#         print(digit)

# obj = Student("Ahsan", "Khan", 2000)
# obj.display()
# obj.roll(25)


## 4. Polymorphism in Python

## 5. Constructors & Destructors in Python
#- class Student():
#     def __init__(self):
#         print("I am constructor")

# std = Student()

# class Student():
#     school = "Agrabad School"           # class variable
#     def __init__(self, roll, name):     
#         self.roll = roll                # instance variable
#         self.name = name
        
#     def display(self):
#         print(f"I am {self.name} and my roll is {self.roll} School: {self.school}")

# std = Student(10, 'Nafisa')
# std.display()
# print(std.school)
# print(Student.school)


# Note: Encapsulation

