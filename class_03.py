#-# Class #3 - Operators & Condition


## 1. Operators & Operands
# a + b     # Here, + is Operator, and, a and b are Operands

## 2. Arithmetic, Comparison & Logical Operators
#> Arithmetic Operators:-
# a = 50
# b = 30
# print(a + b)    # Addition
# print(a - b)    # Subtraction
# print(a * b)    # Multiplication
# print(a / b)    # Division

# a = 7
# b = 3
# print(a % b)    # Modulus
# print(a ** b)   # Exponentiation
# print(a // b)   # Floor division

#> Comparison Operators:-
# x = 10
# y = 12
# print(x == y)   # False
# Other Same Operators:  !=, >, <, >=, <=

#> Logical Operators:-
# a = 15
# b = 10
# c = 12
# print(a>b and b>c and c<a)
# print(a>b or b>c or c<a)
# print(not(a>b or b>c))


## 3. Assignment, Boolean & Membership Operators
#> Assignment Operators:-
# x = 5   # Assignment
# x += 3  # Same as x = x + 3
# print(x)
# Other Same Operators:  -=, *=, /=, %=, //=, **=

#- Bitwise Assignment Operators:-
# x = 5       # binary of 5 is 00000101
# x &= 3      # binary of 3 is 00000011
# print(x)    # Ans: 1         00000001
# Other Same Operators:  |=
# x ^= 3      # Ans: 1         00000110
# x >>= 3     # Ans: 0         00000000
# x <<= 3     # Ans: 0         00101000
# print(x)

#> Identity Operators:-
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)   # returns True because z is the same object as x
# print(x is y)   # returns False because x is not the same object as y, even if they have the same content

# print(x is not z)
# print(x is not y)

# print(id(x))
# print(id(y))
# print(id(z))

#> Membership Operators:-
# x = ["apple", "banana"]
# print("banana" in x)
# print("pineapple" not in x)


#> Bitwise Operators:
# Bitwise operators are used to compare (binary) numbers:
# print(6 & 3)    # 2
# 6 = 0000000000000110
# 3 = 0000000000000011
# --------------------
# 2 = 0000000000000010

# print(6 | 3)
# 6 = 0000000000000110
# 3 = 0000000000000011
# --------------------
# 7 = 0000000000000111

# print(6 ^ 3)
# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
# 6 = 0000000000000110
# 3 = 0000000000000011
# --------------------
# 5 = 0000000000000101

# print(~3)
# The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).
#  3 = 0000000000000011
# -4 = 1111111111111100

# print(3 << 2)
# The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:
# If you push 00 in from the left:
#  3 = 0000000000000011   becomes
# 12 = 0000000000001100

# print(8 >> 2)
# The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.
# If you move each bit 2 times to the right, 8 becomes 2:
#  8 = 0000000000001000   becomes
#  2 = 0000000000000010

#> Operator Precedence:-
# (), **, +x  -x  ~x, *  /  //  %, +  -, <<  >>, &, ^, |
# ==  !=  >  >=  <  <=  is  is not  in  not in, not, and, or   
# If two operators have the same precedence, the expression is evaluated from left to right.


## Python Conditions ##
## 4. if, if..else, & if..elif..else Statement
# if condition:
#     statement...

# x = 25
# y = 15
# if x > y:
#     print("X is higher than y")

# x = 25
# y = 35
# if x > y:
#     print("X is higher than Y")
# else:
#     print("Y is higher than X")

# x = 25
# y = 35
# z = 50
# if x > y and x > z:
#     print("X is the Largest Number")
# elif y > x and y > z:
#     print("Y is the Largest Number")
# else:
#     print("Z is the Largest Number")


## 5. Nested if & Nested if..else Statement
x = 55
y = 35

if x > y:
    if 60 > 33:             # nested if..else
        print("Pass")
    else:
        print("Fail")
else:
    print("Error")
