#-# Class #4 - Loops in Python


## 1. For Loop Statement
# l = [10, 20, 30, 40, 50]
# for x in l:
#     print(x)

# l = [10, 20, 30, 40]
# sum = 0
# for x in l:
#     sum = sum + x
# print(sum)

# for x in range(5):
#     print(x)
# for x in range(5, 10):
#     print(x)
# for x in range(5, 20, 3):
#     print(x)

# for i in range(1, 10+1):
    # print(f"2 x {i} =", 2 * i)
    # print("2 x {} =".format(i), 2 * i)


## 2. While Loop Statement
# initial
# while condition:
#     statements
#     increament/decrement

# i = 1
# while i <= 15:
#     print(i)
#     i = i + 1

# a = "Hafizul Islam"
# i = 1
# n = len(a)
# while i < n:
#     print(a[i])
#     i = i + 1

# Assignment: Printing all Prime Numbers between 2-50


## 3. Infinite & Nested Loop Statement
# for x in range(1,6):
#     for y in range(x):
#         print('#', end='')
#     print('')

# for i in range(1, 10+1):
#     for j in range(1, 10+1):
#         print(i * j, end=" ")
#     print('')


## 4. break, continue & pass Statement
# for x in range(5):
#     if x == 3:
#         break
#     print(x)

# for x in range(5):
#     if x == 3:
#         continue
#     print(x)

# for x in range(5):
#     if x == 3:
#         pass          # do nothing and continue the program
#     print(x)