#-# Class #2 - String of Python

## 1. Introduction & Declaration of String
# mystring = 'This is python'       # we can use " " - double quote as well
# mystring = "This" " is" " python" # we can concatenate string like this
# print(mystring)
# print(type(mystring))

# multi_line_str = """This is Python
# It's a very nice language
# So efficient and user-friendly
# It's very efficient for data science"""
# print(multi_line_str)
# print(type(multi_line_str))


## 2. Accessing Values & Updating String
#> Accessing Values:-
#- Indexing:-
# p = 'python'
# i = p[0]
# print(i)

# p = 'python'
# l = len(p)    # length of p
# print(l)
# for i in range(l):
#     print(p[i], i)

#- Slicing:-
# s = "Hello Bangladesh"
# ans = s[:]        # all
# ans = s[6:]       # 'Bangladesh'
# ans = s[:5]       # 'Hello'
# ans = s[3:8]      # 'lo Ba'
# ans = s[2:13:2]   # 'loBnld'
# ans = s[-14:-2:2] # 'loBnld'
# ans = s[-10:-2]   # 'Banglade'
# ans = s[-10:]     # 'Bangladesh'
# print(ans)

#> Finding String:-
#> in, not in:- 
# mystring = "Python is the greatest programming language in the world"
# ans = "language" in mystring
# ans = "Java" not in mystring
# print(ans)


## 3. String Formatters & Escape Sequences
#> String Format:-
# piece = 3
# price = 300
# s = "I have {} apples and the cost of these are {}".format(piece, price)
# s = "I have {1} apples and the cost of these are {0}".format(piece, price)
# s = f"I have {piece} apples and the cost of these are {price}"
# print(s)


#> Escape Sequences:-
# s = 'Python is a \'awesome\' language'
# s = "Python is a 'awesome' language"
# s = 'Python is a "awesome" language'
# print(s)

# s = 'Python is a\nawesome language'
# s = 'Python is a\tawesome language'
# print(s)


## 4. String Functions and Operations
## 5. Most Important Built-in Methods of String

#> Updating String:-
# s = 'Hello, Python, how are you'
# ans = s.upper()
# ans = s.lower()
# ans = s.capitalize()
# ans = s.title()
# print(ans)

# s = 'Hello, Python'
# ans = s.replace('Python', 'Java')
# print(ans)

#> strip():-
# s = '    Hello, Python    '
# ans = s.strip()
# ans = s.lstrip()
# ans = s.rstrip()
# print(s)
# print(ans)

# s = 'Hello, Python'
# ans = s.split()
# ans = s.split(",")
# print(ans)



