#-# Class #7 - File & Exception Handling

## 1. Open, Read & Write a File
#> Opening, creating and writing:-
# f = open('newfile.txt', 'x')    # Creating file with x mode
# f = open('newfile.txt', 'w')    # Creating file with w mode
# f = open('newfile.txt', 'a')    # appending text
# f.write('I am Bangladeshi'+'\n')
# f.close()

#> reading:
# f = open('newfile.txt', 'r')
# print(f.read())
# f.close()

# with open('newfile.txt', 'r') as f:
#     print(f.read())               # without close()

#-Seek()
# f = open('newfile.txt', 'r')
# f.seek(5)
# print(f.read())
# f.close()


## 2. Managing Directory & Rename a File
# import os

# old_path = r"E:\My Current Courses\Python Django Course by Universe IT\Online Batch-116 Class Codes\newfile.txt"
# new_path = r"E:\My Current Courses\Python Django Course by Universe IT\Online Batch-116 Class Codes\createfile.txt"
# os.rename(old_path, new_path)

#> remove file and dir
# os.remove("file.txt")
# os.rmdir("files")


## 3. Errors vs Exception
# import os
# f = open("createfile.txt")

# if os.path.isfile:
#     txt = f.read()
#     print(txt)
# else:
#     print("this file does not exist")

# if os.path.exists('createfile.txt'):
#     f = open("createfile.txt")
#     txt = f.read()
#     print(txt)
# else:
#     print("this file does not exist")

# path = r"E:\My Current Courses\Python Django Course by Universe IT\Online Batch-116 Class Codes\createfile.txt"
# if os.path.isfile(path):
#     f = open("createfile.txt",'r')
#     txt = f.read()
#     print(txt)
#     f = open("createfile.txt",'w')
#     f.write("258")
# else:
#     print("this file does not exist")

import os
path = os.chdir(r"E:\My Current Courses\images")
img_list = os.listdir(path)
i = 1
for img in img_list:
    new_name = f'new{i}.txt'
    os.rename(img, new_name)
    i += 1


## 4. try...except & try...except...else Statement
num1 = int(input('Enter 1st Number '))
num2 = int(input('Enter 2nd Number '))

try:
    div = num1 / num2
    print(div)
except Exception as e:
    print("Error: ", e)

    
## 5. try...except...finally Statement