#-# Class #6 - Functions in Python

## 1. Define a Function
# def myfunction():
#     print("This is a Function")

# myfunction()


## 2. Function Arguments
# def myfunction(a, b, c):
#     print(a, b, c)

# myfunction(10, 20, 30)

#- *args
# def myfunction(*args):
#     print(args[2] - args[1])

# myfunction(10, 20, 30)

#- *kwargs
# def myfunction(**kwargs):
#     print(kwargs['c'] - kwargs.get('a'))

# myfunction(a=10, b=20, c=30)

#> Nested Function:-
# def outer_func():
#     print("I am outer function")
#     def inner_func():
#         print("I am inner function")
    
#     inner_func()
# outer_func()

#> returning value:-
# def sum(w):
#     a = 20
#     b = 30
#     c = a + b
#     return c * w

# print(sum(5)) 

#- bonus & salary func:
# def bonus():
#     bns = 2000
#     return bns

# def salary(bns):
#     basic = 5000
#     total = basic + bns
#     print("Total Salary", total)

# salary(bonus())

#- one & two func:
# def one(t):
#     print("I am One")
#     return t

# def two():
#     return "I am Two"

# print(one(two()))


## 3. Recursion in Python
# def recursion(n):
#     if n == 1:
#         return 1
#     else:
#         sum = n * recursion(n - 1)
#         return sum

# print(recursion(5))


## 4. Built-in {Function} Python
## 5. Anonymous Function or Lambda Expression