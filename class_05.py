#-# Class #5 - Built-in Data Structure in Python


## 1. List in Python
# l = [10, "Samrat", True, 12.5]
# print(l)
# print(type(l))


## 2. Indexing, Slicing & Negative Indexing in Python
# l = [10, "Samrat", True, 12.5]
# print(l[2])
# print(l[0:2])
# print(l[-2])
# print(l[-3:-1])

# if 'Samrat' in l:
#     print('Yes')

# a = ["rakib", "mijan", "rasel", "jabed"]
# a[1] = "rabbani"                  # changing value
# a[1:3] = "sobuj", "rabbani"
# a[1:3] = ["sobuj", "rabbani"]
# print(a)
# a.append("rony")
# a.insert(1, "alamgir")
# print(a)
# a.remove("mijan")
# print(a)
# a.pop(1)
# a.pop()       # removes last item
# a.clear()
# print(a)

# b = ["a", "b", "c", "d"]
# a.extend(b)
# print(a)

# for i in a:
#     print(i)
# for i in range(len(a)):
#     print(i, a[i])
# [print(i) for i in a]


## 3. Tuple & Sets in Python
# t = ("rakib", "mijan", "rasel", "jabed")
# print(type(t))
# print(t[2])
# print(t[0:2])
# print(t[-2])
# print(t[-3:-1])

# if 'mijan' in t:
#     print('Yes')

# for i in t:
#     print(i)
# for i in range(len(t)):
#     print(i, t[i])
# [print(i) for i in t]

#> appending/inserting to a tuple
#- convert tuple to list, then append, then convert list to tuple
# t_to_l = list(t)
# t_to_l.append("rabbani")
# l_to_t = tuple(t_to_l)
# print(l_to_t)


## 4. Dictionary in Python
# d = {'name': 'samrat', 'roll': 10, 'subject': 'python'}
# print(d['roll'])
# print(d.get('roll'))
# print(d.keys())
# print(d.values())

# d['dept'] = 'IT'    # adding
# print(d)

# d = {10: 'roll', 3.5: 'grade', True: 'passed'}
# print(d)
