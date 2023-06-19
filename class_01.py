#-#  Class #1 - Environment Setup, Variable, Data Type & Type Casting


## 1. Python Environment Setup
# Downloading and Installation of Python and VS Code


## 2. Basic Syntax of Python (Statements, Indentation, Comments)
#> Statements:-
# print("Hello World")

#> Indentation:-
# a = 10
# b = 5
# if a > b:
#     print("A is big")     # indented

#> Comments:-
# Hiding code or writing documentation


## 3. Python Variable
# zara = 10       # can start with alphabet/letter
# _zara = 20      # can start with underscore
# 1zara = 25      # can't start with number
# zara12 = 30     # can contain alpha-numeric characters and underscores

#- variables names are case-sensitive 
#- (age Age, AGE are three different variables)
# age = 20
# Age = 25
# AGE = 30
# print(age, Age, AGE)

#- variables name can't be any python keywords
#- such as- print, del, class etc

# a = 10, 20, 30      # can assign multiple data
# print(a)

# a = b = c = 20      # can assign single data to multiple var
# print(a, b, c)

# a, b, c = 10, 20, 30    # can assign multiple data to multiple var at a time
# print(a, b, c)


## 4. Data Type in Python
#> Built-in Data Types:-
#- Text Type        : str
#- Numeric Types    : int, float, complex
#*- Sequence Types   : list, tuple, range
#*- Mapping Type     : dict
#*- Set Types        : set, frozenset
#- Boolean Type     : bool
#*- Binary Types     : bytes, bytearray, memoryview
#*- None Type        : NoneType

#> Numeric Types:-
# fahim = 40    # <class 'int'>
# fahim = 40.5  # <class 'float'>
# fahim = 40j   # <class 'complex'>
# print(type(fahim))

#> Text Type:-
# jahan = "Bangladeshi 17 years old @dhaka"     # using double quote
# jahan = 'Bangladeshi 17 years old @dhaka'     # using single quote
# print(type(jahan))  # <class 'str'>

#> Boolean Type:-
# mostaq = True
# print(type(mostaq))  # <class 'bool'>

## 5. Type Casting in Python
#- From W3Schools:-
#- Type Casting means Specifying a Variable Type
#- Casting in python is done using constructor functions:

#> Integers:-
# x = int(1)        # x will be 1
# y = int(2.8)      # y will be 2
# z = int("3")      # z will be 3
# w = int(True)     # w will be 1

#> Floats:-
# x = float(1)      # x will be 1.0
# y = float(2.8)    # y will be 2.8
# z = float("3")    # z will be 3.0
# w = float("4.2")  # w will be 4.2

# x = str("s1")     # x will be 's1'
# y = str(2)        # y will be '2'
# z = str(3.0)      # z will be '3.0'
# w = str(True)     # w will be 'True'
# print(x, y, z, w)