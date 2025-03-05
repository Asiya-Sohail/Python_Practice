#50 DAYS OF PYTHON
#A challenge a Day
#Benjamin Bennett Alexander

#Day 1
#Division and Square-root
'''import math
def divide_or_square(num):
    if num % 5 == 0:
        return math.sqrt(num)
    else:
        return num % 5
print(divide_or_square(7))'''
#Extra Challenge: Longest Value
'''def  longest_value(dict):
    if not dict:
        return None
    length = 0
    key_l = 0
    for key, value in dict.items():
        if len(value) > length:
            key_l = key
            length = len(value)

    return dict[key_l]
fruits = {'fruit': 'apple', 'color': 'green'}
print(longest_value(fruits))'''

#Day 2
#Strings to Integers
'''def convert_add(l):
    sum = 0
    j = 0
    for i in l:
        l[j] = int(i)
        j = j + 1
        sum += int(i)
    return sum
lis =  ['1', '3', '5']
print(convert_add(lis))
print(lis)'''

#Extra knowledge
'''string = ['1', '2', '3']
integer = [int(x) for x in string]
print(integer)'''

#Extra Challenge: Duplicate Names
'''def check_duplicates(l):
    seen = []
    duplicate = []
    for x in l:
        if x in seen:
            duplicate.append(x)
        else:
            seen.append(x)

    if duplicate:
        return duplicate
    else:
        return "No duplicate"
fruits = ['apple','orange', 'orange', 'banana', 'apple']
li = ['Yoda', 'Moses', 'Joshua', 'Mark']
print(check_duplicates(fruits))'''

#Day 3
#Register Check
'''def register_check(dict):
    count = 0
    for key, value in dict.items():
        if value == 'yes':
            count += 1
    return count


register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
print(register_check(register))'''

#Extra Challenge: Lowercase Names
'''def find_lower(lst):
    tup = []
    for x in lst:
        if x == x.lower():
            tup.append(x)
        else:
            continue
    tup = sorted(tup)
    tup = tup[::-1]
    return tuple(tup)

names = ["kerry", "carol", "dickson", "John", "Mary", "Rose", "adam"]
print(find_lower(names))'''

# Day 4
# Only Floats
'''def only_floats(a, b):
    if isinstance(a,float) and isinstance(b,float):
        return 2
    elif isinstance(a,float) or isinstance(b,float):
        return 1
    else:
        return 0

print(only_floats(12.1, 23.0))'''

#Extra Challenge: Index of the Longest Word
'''def word_index(str_lst):
    count = 0
    l = []
    max_length = max([len(i) for i in str_lst])
    for i in str_lst:
        if len(i) == max_length:
            l.append(i)
            c = count
        count += 1

    if len(l) == 1:
        return c
    else:
        return 0

words1 = ["Hate", "remorse", "vengeance"]
print(word_index(words1))'''

# Day 5
# My Discount
'''def my_discount():
    price = input("Enter the original price: ")
    discount = input("Enter the discount percent: ")
    return (int(price) - (int(price)*int(discount)/100))

print("The price with discount is", my_discount())'''

# Extra Challenge: Tuple of Student Sex
'''def student_sex(students):
    male = 0
    female = 0
    for i in students:
        if i.lower() == "male":
            male += 1
        elif i.lower() == "female":
            female += 1
    return ([("Male", male), ("Female", female)])

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

print(student_sex(students))'''

# Day 6
# User Name Generator
'''def user_name():
    email = input("Enter your email")
    ind = email.find("@")
    return email[:ind]

print("Your username is", user_name())'''

# Extra Challenge: Zero Both ends
'''def zeroed(lst):
    lst[0] = 0
    lst[-1] = 0
    return lst

lst =  [2, 5, 7, 8, 9]
print(zeroed(lst))'''

# Day 7
# A String Range
'''def string_range(l):
    string = ""
    for i in range(0,l):
        if i == l - 1:
            string += str(i)
        else:
            string += str(i) + '.'
    return string
print(string_range(6))'''

# Chat GPT code1
'''def string_range(num):
    return '.'.join([str(i) for i in range(num)])
print(string_range(6))'''

# CHat GPT code2
'''def string_range(num):
    return '.'.join(map(str, range(num)))
print(string_range(6))'''


# Extra Challenge: Dictionary of names
#CHat GPT
'''def S_names(names):
    return {name: names.count(name) for name in names if name.startswith('S')}'''

'''def s_names(names):
    dictionary = {}
    for i in names:
        if i.startswith('S') or i.startswith('s'):
            dictionary[i] = names.count(i)
    return dictionary
names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera", "Sana"]
print(s_names(names))'''

#Day 8
# Odd and Even
'''def odd_even(lst):
    max_even = max([i for i in lst if i % 2 == 0])
    min_odd = min([i for i in lst if i % 2 != 0])
    return max_even - min_odd
lst = [3,2,4,6, 8]
print(odd_even(lst))'''

#Extra Challenge: List of Prime Numbers
'''def prime_numbers(l):
    primes = []
    for i in range(2, l+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes
print(prime_numbers(10))'''

# Day 9
# Biggest Odd Number
'''def biggest_odd(number):
    odd = max([int(x) for x in list(number) if int(x) % 2 != 0])
    return odd

print(biggest_odd("23967"))'''

# Extra Challenge: Zeros to the End

'''def zeros_last(lst):
    zeros = lst.count(0)
    non_zeros = [x for x in lst if x != 0]
    return (non_zeros + zeros*[0]) 

lst = [1, 4, 6, 0, 7,0,9]
print(zeros_last(lst))'''

# Day 10
# Hide my Password
# my code
'''def hide_password():
    Password = input("Enter a password")
    lst = ["*" for x in Password]
    return ("".join(lst))

print(hide_password())'''

# Chat GPT
'''def hide_password():
    password = input("Enter your password: ")
    hidden_password = '*' * len(password)
    return hidden_password

print(hide_password())'''

# Extra Challenge: A Thousand Separator
# Chat GPT
'''def convert_numbers(numbers):
    return [format(num, ',') for num in numbers]

numbers = [1000000, 2356989, 2354672, 9878098]
print(convert_numbers(numbers))'''

#my code
'''def separator(lst):
    #str = [format(num, ",") for num in lst]
    str = [f"{num:,}" for num in lst]
    return str
lst = [1000000, 2356989, 2354672, 9878098]
print(separator(lst))'''

# Day 11
# Are They Equal?
'''def equal_strings(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

print(equal_strings("love", "evol"))'''

# Extra Challenge: Swap Values
# My code
'''def swap_values(lst):
    if len(lst) > 2:
        temp = lst[0]
        lst [0] = lst[-1]
        lst[-1] = temp
        return lst
    else:
        print("Can't swap!")

lst = [2, 4,67, 7] 
print(swap_values(lst))'''

# Chat GPT
'''def swap_values(nums):
    nums[0], nums[-1] = nums[-1], nums[0]
    return nums
print(swap_values([2, 4, 67, 7]))'''

# Day 12
# Count the Dots
'''def count_dots(str):
    return str.count(".")

str = "h.e.l.p."
print(count_dots(str))'''

# Extra Challenge: Your Age in Minutes
'''def  age_in_minutes():
    while True:
        birth_year = input("Enter your year of birth")
        current_year = input("Enter current year")
        if len(str(birth_year)) != 4 or len(str(birth_year)) != 4:
            print("Invalid Input, Please try Again!")
            continue
        elif birth_year > current_year or current_year < birth_year:
            print("Invalid Input, Please try Again!")
            continue
        else:
            return ((int(current_year) - int(birth_year)) * 365 * 24 * 60)

print(age_in_minutes())'''

# Day 13
# Pay Your Tax
'''def your_vat():
    while True:
        try:
            price , vat = [int(x) for x in input("Enter price and Vat in percentage").split()]
            #price, vat = input("Enter price and Vat in percentage").split()
            return price + (price*vat/100)
        except ValueError:
            print("Try Again!")

print(your_vat())'''

# Extra Challenge: Pyramid of Snakes
'''def Python_snakes(num):
    for i in range(1,num):
            print(" "*(num-1-i), "* "*i)
Python_snakes(7)'''

#Chat GPT
'''def python_snakes(num):
    for i in range(1, num + 1):
        spaces = ' ' * (num - i)  
        snakes = ' '.join(["*" for _ in range(i)]) 
        print(spaces + snakes)
python_snakes(7)'''

#Day 14
#Flatten the List
#my code
'''def flat_list(lst):
    new = lst[0]
    return new
lst = [[2,4,5,6]]
print(flat_list(lst))'''

#Chat GPT
#'item for sublist in nested_list' is the outer loop and 'for item in sublist' is the inner loop
'''def flat_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

print(flat_list([[2, 4, 5, 6]]))  '''

#Extra Challenge: Teacher’s Salary
# My Code
'''def your_salary():
    gross_salary = 0
    name = input("What's your name")
    periods = int(input("Enter the number of periods you took in a month"))
    rate = int(input("Enter the monthly rate per period"))
    total_periods = periods
    if periods > 100:
        gross_salary += 25*(periods - 100)
        gross_salary += rate * 100
    else:
        gross_salary += (rate * periods)
    gross_salary = "{:,.0f}".format(gross_salary)
    return name, total_periods, gross_salary

name, periods, salary = your_salary()
print("Teacher : " + name)
print("Periods :", periods)
print("Gross salary :", salary)'''

# Chat GPT
'''def your_salary(name, periods):
    monthly_rate = 20
    overtime_rate = 25
    max_normal_periods = 100

    if periods <= max_normal_periods:
        gross_salary = periods * monthly_rate
    else:
        normal_salary = max_normal_periods * monthly_rate
        overtime_salary = (periods - max_normal_periods) * overtime_rate
        gross_salary = normal_salary + overtime_salary

    formatted_gross_salary = "{:,.0f}".format(gross_salary)  # Format salary with commas
    return f"Teacher: {name},\nPeriods: {periods}\nGross salary: {formatted_gross_salary}"

print(your_salary("John Kelly", 105))'''

# Day 15
# Same in Reverse
# my code
'''def same_in_reverse(str):
    return str == str[::-1]
print(same_in_reverse("civic"))'''

# Chat GPT
'''def same_in_reverse(string):
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True
print(same_in_reverse("dad"))'''

# Extra Challenge: What’s My Age?
'''def your_age():
    name = input("What's your name")
    names_age = {"jane" : 23, "kerry": 45, "tim": 34, "peter": 27}
    for key, value in names_age.items():
        if key.lower in names_age.keys():
            return ( f"Hi, {key.title()}, you are {value} years old")
    print("Your name is not in the dictionary")
    age = int(input("What's your age"))
    names_age[name.lower()] = age
    return ( f"Hi, {name.title()}, you are {age} years old")

print(your_age())'''

# Day 16
# Sum the List
'''def sum_list(lst):
    Sum = sum([x for i in lst for x in i])
    return Sum
lst =  [[2, 4, 5, 6], [2, 3, 5, 6]]
print(sum_list(lst))'''

# Extra Challenge: Unpack A Nest
'''def output(Nested_list):
    return list({x for i in Nested_list for x in i if x == 34 or x == 67 or x == 78})

Nested_list = [[12, 34, 56, 67], [34, 68, 67, 34, 78]]
print(output(Nested_list))'''

# Day 17
# User Name Generator
'''import random
def  user_name():
    name = input("Enter your name").lower()
    username = name[::-1] + str(random.randint(0,9))
    return username
print("Your user name: " + user_name())'''


# Extra Challenge: Sort by Length
'''def  sort_length(lst):
    for i in range(0, len(lst)-1):
        if len(lst[i]) > len(lst[i+1]):
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

names = [ "Peter", "Jon", "Andrew"]
print(sort_length(names))'''

# Day 18
# Any Number of Arguments
# my code
'''def any_number(*numbers):
    sum = 0
    count = 0
    for x in numbers:
        if isinstance(x, (int, float)):
            sum += x
            count += 1
    return sum/count if count > 0 else 0

print(any_number(2.5, 3.5, 4.5))'''

# Chat GPT
'''def any_number(*numbers):
    num = [x for x in numbers if isinstance(x, (int, float))]
    return  sum(num) / len(num) if numbers else 0 #If the numbers list is not empty

print(any_number(2.5, 3.5, 4.5))'''


# Extra Challenge: Add and Reverse
'''def add_reverse(l1, l2):
    if len(l1) != len(l2):
        return "The lists are not of equal lengths"
    new_list = []
    #for i in range(0, len(l1)):
    for i in range(len(l1)-1, -1, -1):
        new_list.append(l1[i] + l2[i])
    return new_list
    #return new_list[::-1]

lst1 = [10, 12, 34]
lst2 = [12, 56, 78]
print(add_reverse(lst1, lst2))'''

# Day 19
# Words and Elements
'''def  count_words(str):
    return len(str.split())

def count_elements(str):
    return len(str) - len(str.split()) + 1
    #return len(str) - str.count(" ")
    #return len([char for char in str if char != " "])
    #return len(str.replace(" ", ""))

print(count_words('I love learning Python'))
print(count_elements('I love learning Python'))'''

# Day 20
# Capitalize First Letter
'''def capitalize(str):
    return str.title()
print(capitalize('i like learning'))'''

# Extra Challenge: Reversed List
'''def convert(str):
    string = [word[::-1] for word in str.split() if any(x.isupper() for x in word)]
    return string

str1 = 'leArning is hard, bUt if You appLy youRself ' \
 'you can achieVe success'
print(convert(str1))'''

# Day 21
# List of Tuples
# my code
'''def make_tuples(lst1, lst2):
    if len(lst1) != len(lst2):
        return "Lists are not of equal lengths"
    tuple_list = [(lst1[i], lst2[i]) for i in range(0, len(lst1))]   
    return tuple_list

lst1, lst2 = [1,2,3,4] , [5,6,7,8]
print(make_tuples(lst1, lst2))'''

# Chat GPT
'''def make_tuples(lst1, lst2):
    return list(zip(lst1, lst2))

    #return [(x,y) for x, y in zip(lst1, lst2)]

lst1, lst2 = [1,2,3,4] , [5,6,7,8]
print(make_tuples(lst1, lst2))'''

# Extra Challenge: Even Number or Average
# my code
'''def even_or_average():
    while True:
        numbers = input("Enter five numbers")
        numbers = numbers.split()
        if len(numbers) != 5:
            print("Enter 5 number")
            continue
        if any(int(x) % 2 == 0 for x in numbers):
            even = max([int(x) for x in numbers if int(x) % 2 == 0])
            return f"Largest Even Number is {even}"
        else:
            average = sum([int(x) for x in numbers])/len(numbers)
            return f"There is no even number, so average is {average}"
print(even_or_average())'''

# Chat GPT
'''def even_or_average():
    numbers = [float(input("Enter number {}".format(i+1))) for i in range(5)]
    even_numbers = [num for num in numbers if num % 2 == 0]
    if even_numbers:
        return max(even_numbers)
    else:
        return sum(numbers) / 5
print(even_or_average())'''

# Day 22
# Add Under_Score

'''def add_hash(str):
    #return str.replace(" ", "#")
    return "#".join(str.split())
def add_underscore(str):
    return str.replace("#", "_")
def remove_underscore(str):
    return str.replace("_", " ")

print(remove_underscore(add_underscore(add_hash('Python'))))'''

# Day 23
# Simple Calculator
'''def calculator(num1, num2):
    try:
        print("Here we are to calculate to numbers")
        operation = input("Press\n+ for addition.\n- for subtraction.\n* for multiplication.\n/ for division.\n")
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            try:
                return num1 / num2
            except ZeroDivisionError:
                print("Can't divide by zero")
        else:
            print("Operation isn't defined")
    except ValueError:
        print("One or both parameters are not valid numbers")
try:
    num1 = int(input("Enter 1st number"))
    num2 = int(input("Enter 2nd number"))
    print(calculator(num1, num2))
except ValueError:
    print("Invalid input. Please enter valid numbers.")'''

# Extra Challenge: Multiply Words
'''import math
def multiply_words(string):
    string = string.split()
    length = math.prod([len(i) for i in string if all(x.islower() for x in i)])
    return length

print(multiply_words("love live and laugh"))'''

# Day 24
# Average Calories
'''def average_calories():
    list = []
    flag = True
    while flag:
        num = input("Enter number of calories ('done' for quitting)")
        if num == 'done':
            flag = 0
        else:
            try:
                num = int(num)
            except ValueError:
                print("You can only enter numbers, Try Again!")
            else:
                list.append(num)

    return f"The average calories for {len(list)} days are {sum(list)/ len(list)}"

print(average_calories())'''

# Extra Challenge: Create a Nested List
'''def nested_lists(*lists):
    return [x for x in lists]
    #return list(lists)
print(nested_lists( [1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]))'''

# Day 25
# All the Same
'''def all_the_same(obj):
    if isinstance(obj, str):
        obj = obj.split()
    if len(set(obj)) == 1:
        return True
    else:
        return False

print(all_the_same(['Marry', "Marry", "Marry"]))'''

# Extra Challenge: Reverse a String
'''def read_backwards(string):
    return " ".join(string.split()[::-1])
    #return ' '.join(reversed(string.split()))
    #return ' '.join([word for word in string.split()][::-1])

print(read_backwards("the love is real"))'''

# Day 26
# Sort Words
'''def sort_words(string):
    #return [",".join(sorted(set([x for x in string if x != " "])))]
    return [','.join(sorted(set(string.replace(' ', ''))))]

print(sort_words("love life"))'''

# Extra Challenge: Length of Words
# my code
'''def string_length(string):
    dictionary = {}
    for i in string.split():
        dictionary[i] = len(i)
    return dictionary
print(string_length("Hi my name is Richard"))'''

# Chat GPT
'''def string_length(s):
    return {word: len(word) for word in s.split()}
print(string_length('Hi my name is Richard'))'''

# Day 27
# Unique Numbers
'''def unique_numbers(lst):
    new_list = list(set(lst))
    difference = sum(lst) - sum(new_list)
    if difference % 2 == 0:
        return lst
    else:
        return new_list

lst =  [1, 2, 4, 5, 6, 7, 8, 8]
print(unique_numbers(lst))'''

# Extra Challenge: Difference of two Lists
# my code
'''def difference(lst1, lst2):
    return [x for x in lst1 if x not in lst2] + [x for x in lst2 if x not in lst1]
    #return list(set(lst1) ^ set(lst2)) #symmetric difference method
list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
print(difference(list1, list2))'''

# Day 28
# Return Indexes
# my code
'''def index_position(string):
    return [string.index(i) for i in string if i.islower()]
print(index_position('LovE'))'''

# Chat GPT
'''def index_position(string):
    return [i for i, char in enumerate(string) if char.islower()]
print(index_position('LovE'))'''

# Extra Challenge: Largest Number
'''def largest_number(lst):
    return int("".join(sorted("".join(str(x) for x in lst), reverse = True)))

lst = [3, 67, 87, 9, 2]
print(largest_number(lst))'''

# Day 29
# Middle Figure
'''def middle_figure(str1, str2):
    integrated = str1.replace(" ", "") + str2.replace(" ", "")
    if len(integrated) % 2 != 0:
        return integrated[len(integrated)//2 : (len(integrated)//2) + 1]
    else:
        return "No Middle Figure"
str1 = "make love"
str2 = "not wars"
print(middle_figure(str1, str2))'''

# Day 30
# Most Repeated Name
'''def repeated_name(name):
    l_count = 0
    for i in name:
        if name.count(i) > l_count:
            l_count = name.count(i)
    for i in name:
        if name.count(i) == l_count:
            return i
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
print(repeated_name(name))'''

# Extra Challenge: Sort by Last Name
'''def sorted_names(lst):
    return sorted([f"{last} {first}" for first, last in [name.split() for name in lst]])
    #return sorted(" ".join(x.split()[::-1]) for x in lst)
names = ['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']
print(sorted_names(names))'''

# Day 31
# Longest Word
'''def  longest_word(lst):
    #longest = max(lst, key = len)
    #return [len(longest), longest]
    longest = ""
    for x in lst:
        if len(x) > len(longest):
            longest = x
    return [len(longest), longest]

lst = ['Java' , 'JavaScript', 'Python']
print(longest_word(lst))'''

#Extra Challenge: Create User
'''def create_user():
    dictionary = {}
    dictionary["name"] = input("Enter your name")
    dictionary["age"] = int(input("Enter your age"))
    dictionary["password"] = input("Enter your password")
    print("User saved. Please login")
    while True:
        name = input("Enter your name to check")
        password = input("Enter password")
        if name == dictionary["name"] and password == dictionary["password"]:
            print("Logged in successfully")
            return 
        else:
            print("Wrong password or user name. Please try again")

create_user()'''

# Day 32
# Password Validator
'''def password_validator():
    while True:
        password = input("Enter a password")
        if len(password) < 8:
            print("Length should not be less than 8 characters. Try Again")
        elif not any(x.isupper() for x in password):
            print("Password should have upper letters")
        elif not any(x.islower() for x in password):
            print("Password should have lower letters")
        elif not any(x.isdigit() for x in password):
            print("Password should have a number")
            print("Please Enter another Password")
        else:
            return password
print("Valid password: " + password_validator())'''

# Extra Challenge: Valid Email
'''def email_validator(lst):
    valid = [x for x in lst if x.endswith(".com") and x[0] != "@" and x.count("@") == 1]
    if valid:
        return valid
    else:
        return "All emails are Invalid"

emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com' ]
print(email_validator(emails))'''

# Day 33
# List Intersection
'''def intersection_list(lst1, lst2):
    return tuple([x for x in lst1 if x in lst2])
    #return tuple(set(lst1) & set(lst2)) #intersection
    #return tuple(set(lst1).intersection(set(lst2)))
list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]
print(intersection_list(list1, list2))'''

#Extra Challenge: Set or list
'''a = range(9999999)
print(list(a)) # faster than set in iteration
print(set(a))'''

#Day 34
#Just Digits
import csv










#Day 35
#Pangram
# my code
'''import string
def check_pangram(str):
    missing = ""
    for x in string.ascii_lowercase:
        if x not in str:
            missing += x
    if missing:
        return False
    else:
        return True

str = "the quick brown fox jumps over a lazy dog" 
print(check_pangram(str))'''

# Chat GPT
'''import string
def check_pangram(sentence):
    return all(letter in sentence.lower() for letter in string.ascii_lowercase)
print(check_pangram('the quick brown fox jumps over a lazy dog'))'''

# Extra Challenge: Find my Position
# my code
'''def find_index(lst, integer):
    index_list = []
    for i, n in enumerate(lst):
        if integer == n:
            index_list.append(i)
    if index_list:
        return index_list
    else:
        return [integer for x in lst]
print(find_index([1, 2, 4, 6, 7, 7], 8))'''

# Chat GPT
'''def index_list(lst, num):
    if num in lst:
        return [i for i,x in enumerate(lst) if x == num]
    else:
        return [num] * len(lst)

print(index_list([1, 2, 4, 6, 7, 7], 8))'''

# Day 36
# Count String
'''def count(str):
    return {word: str.count(word) for word in str}
print(count("hello"))'''

# Day 37
# Count the Vowels
'''def count_the_vowels(str):
    vowels = "aeiou"
    return len({char.lower() for char in str if char in vowels})
print(count_the_vowels('saas'))'''

# Day 38
# Guess a Number
'''import random
def guess_a_number():
    w = 0
    r = random.randint(1, 10)
    while w < 3:
        w += 1
        num = int(input("Enter a number"))
        if num > r:
            print("Guess is too high, Try Again")
        elif num < r:
            print("Guess is too low, Try Again")
        else:
            print(f"Your Guess is right\nNumber of attempts took is {w}")
            return "Winner"
    return "Looser"
print(guess_a_number())'''

# Extra Challenge: Find Missing Numbers
'''def missing_numbers(lst):
    absent = []
    for i in range(lst[0],lst[-1] + 1):
        if i not in lst:
            absent.append(i)
    return absent
list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
print(missing_numbers(list))'''

# Day 39: Password Generator
'''import string
import secrets
def generate_password():
    total = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    level = int(input("How strong you want your password to be (weak 1, strong 2 or very strong 3)"))
    password = ""
    while True:
        if level == 1:
            for i in range(0,5):
                password += ''.join(secrets.choice(total))
        elif level == 2:
            for i in range(0,8):
                password += ''.join(secrets.choice(total))
        elif level == 3:
            for i in range(0,12):
                password += ''.join(secrets.choice(total))
        else:
            return "Wrong level chosen! Try Again" 
        print("Password is : ", password)

        if not any(char.islower() for char in password):
            password = " "
            continue
        elif not any(char.isupper() for char in password):
            password = " "
            continue
        elif not any(char.isdigit() for char in password):
            password = " "
            continue
        elif not any(char in string.punctuation for char in password):
            password = " "
            continue
        else:
            return f"{password} is right password"
print(generate_password())'''

#Day 40
#Pig Latin
'''def translate(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    translated = []
    for x in string.split():
        if x[0].lower() in vowels:
            translated.append(x + 'yay')
        else:
            x = list(x)
            x.append(x[0])
            del x[0]
            x = "".join(x)
            translated.append(x + 'ay')
    return " ".join(translated)

a = 'i love python'
print(translate(a))'''

#Day 41
#Only Words with Vowels
#my code
'''def words_with_vowels(str):
    lst = []
    vowels = "aeiouAEIOU"
    for word in str.split():
        for x in word:
            if x in vowels:
                lst.append(word)
                break
    return lst
print(words_with_vowels('You have no rhythm'))'''

#Chat GPT
'''def words_with_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [word for word in sentence.split() if any(char.lower() in vowels for char in word)]
sentence = 'You have no rhythm'
print(words_with_vowels(sentence))'''

#Extra Challenge: Class of Cars
'''class Car:
    def __init__(self, model, Color, Year, Transmission, Electric):
        self.model = model
        self.Color = Color
        self.Year = Year
        self.Transmission = Transmission
        self.Electric = Electric
    @classmethod
    def print_cars(cls, car_objects):
        for car in car_objects:
            print("car_model =", car.model)
            print("Color =", car.Color)
            print("Year =", car.Year)
            print("Transmission = ", car.Transmission)
            print("Electric =", car.Electric)
            print("\n")
class Ford(Car):
    pass
class BMW(Car):
    pass
class Tesla(Car):
    pass

bmw1 = BMW("x6", "silver", 2018, "Auto", False)
tesla1 = Tesla("S", "beige", 2017, "Auto", True)
ford1 = Ford("focus", "white", 2020, "Auto", False)
Car.print_cars([bmw1, tesla1, ford1])'''




























