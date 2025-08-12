# dict = {"name" : "John", 5 : 0, True :False}
# print(dict)

# mylist = [1, 7, 9, 2, 6, 3]
# # print(mylist.sort)
# print(sorted(mylist))
# print(dict['name'])
# print(dict[5])
# print(dict[True])
# dict[True] = "I am true"
# print(dict[True])
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# del dict[5]
# print(dict)
# for key,value in dict.items():
#   print(key, " : ", value)

# # Only returns keys
# for i in dict:
#   print(i)

# # List Comprehension
# squares = [x**2 for x in range(10)]
# cubes = [x**3 for x in range(10)]
# print(squares)
# print(cubes)

# even = [x for x in range(10) if x % 2 == 0]
# print(abs(-99.8778))

# def greet(name, greet="Hello"):
#   print(f"{greet} : {name}")

# greet("John")

# coordinates = (10, 20)
# print(id(coordinates)) 
# # TypeError: can only concatenate tuple (not "int") to tuple
# # coordinates = coordinates + (30)
# coordinates = coordinates + (30,)
# print(id(coordinates)) 
# print(coordinates)
# # coordinates[0] = 15

# mylist.append(10)
# print(mylist)
# #TypeError: 'int' object is not iterable
# # mylist.extend(12)
# mylist.extend([0, 11])
# print(mylist)
# print(id(mylist))

# print(hash("string"))
# # TypeError: unhashable type: 'list'
# # print(hash(mylist))

# # Q: "Why can't lists be dictionary keys?"
# # A: Dictionary keys must be hashable, and mutable objects can't be hashed because their hash value could change if the object is modified.

# # TypeError: unhashable type: 'list'
# # dict = {[1,2,3], [4, 5, 6]}
# # print(dict)



# # Q: "What's the difference between lst = lst + [4] and lst.append(4)?"
# # A:
# # lst = lst + [4] creates a NEW list object
# # lst.append(4) modifies the EXISTING list object

# # Q: "How do you safely copy mutable objects?"
# # A: Use .copy() for shallow copy or copy.deepcopy() for deep copy:

# import copy

# # Shallow copy
# original = [1, 2, [3, 4]]
# print(original, id(original))
# shallow = original.copy()
# print(shallow, id(shallow))

# # Deep copy  
# deep = copy.deepcopy(original)
# print(deep, id(deep))

# '''SINFB are immutable'''
# # Strings
# # Integers (and all numbers)
# # None
# # Frozensets
# # Bytes
# # Tuples*
# mylist.sort() #: Modifies original list, returns None
# print(mylist)

# # Q4: "How do you loop through two lists simultaneously?"
# # Use zip(list1, list2) - it's the most Pythonic way.

# # Dictionary: for key, value in dict.items()
# # List with index: for index, item in enumerate(list)
# # Multiple lists: for a, b in zip(list1, list2)


# # Lambda Functions (Anonymous Functions)
# # What is a Lambda Function?
# # A lambda function is a small anonymous function that can have any number of arguments but can only have one expression.

# # Find maximum of two numbers
# max_num = lambda a, b: a if a > b else b
# print(max_num(10, 5))  # 10

# # Check if number is even
# is_even = lambda x: x % 2 == 0
# print(is_even(4))      # True
# print(is_even(5))      # False

# # Absolute value
# abs_value = lambda x: x if x >= 0 else -x
# print(abs_value(-5))   # 5

# # Extract specific field from dictionary
# get_name = lambda person: person.get("name", "Unknown")
# person = {"name": "Alice", "age": 30}
# print(get_name(person))  # "Alice"

from datetime import datetime, timedelta

today = datetime.today()
today_date = datetime.today().date()
today_time = datetime.today().time()
print("Today:", today)
print("Today's date:", today_date)
print("Today's time", today_time)

yesterday_date = today_date - timedelta(days=1)
print("Yesterday's date:", yesterday_date)
tomorrow_date = today_date + timedelta(days=1)
print("Tomorrow's date:", tomorrow_date)

now = datetime.now().date()
print("Now:", now)

yesterday_date = now - timedelta(days=1)
print("Yesterday's date:", yesterday_date)
tomorrow_date = now + timedelta(days=1)
print("Tomorrow's date:", tomorrow_date)