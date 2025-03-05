import json
from name_function import get_formatted_name
from city_functions import get_city_country_name
from survey import AnonymousSurvey
from employee import Employee
import unittest
'''with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    
with open('pi_digits.txt') as file_object:
    #for line in file_object:
        #print(line.rstrip())
    lines = file_object.readlines()

for line in lines:
    print(line)
print(lines)'''

'''pi_string =""
for line in lines:
    pi_string += line.rstrip()
#if we use strip we would be able to get rid of widespaces
print(pi_string)
print(len(pi_string))'''


'''pi_string =""
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

birthday = input("Enter your birthday ")
if birthday in pi_string:
    print("Your birthday appears in the first thirty digits of pi!")
else:
    print("Your birthday does not appear in the first thirty digits of pi!")'''

#Practice
'''with open('learning_python.txt') as fp:
    contents = fp.read()
words = ""
for i in contents.split():
    if contents.split().count(i) >= 3:
        if i in words:
            continue
        else:
            words = words + i + " "
print(words) 
print(contents.replace('Python', 'C'))'''


'''filename = "programming.txt"
with open(filename, "w") as fp:
    fp.write("I love programming.\n")    
    fp.write("I love creating new games.\n")    
#If we don't add newline characters it will squinsh all lines together
#If the file you are opening in write mode already exists, it will replace that file with this

with open('programming.txt', "a") as fp:
    fp.write("I also love finding meaning in large datasets.\n")
    fp.write("I love creating apps that can run in a browser.\n")'''

#Practice
'''with open("guest.txt", "w") as fp:
    fp.write(input("Enter your name"))
with open("guest.txt") as fp:
    print(f"Assalamolikum! {fp.read().title()}")'''

'''while True:
    name = input("Enter your name: ")
    if name.lower() == 'quit':
        break

    print(f"Assalamolikum {name.title()}")
    with open("guest_book.txt", "a") as fp:
        fp.write(f"Assalamolikum {name.title()}"+'\n')'''

'''with open('reason.txt', "w"):
    while True:
        stat = input("Why do you like programming? ")
        with open('reason.txt', "a") as fp:
            fp.write(stat + "\n")'''

#Exceptions
'''try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")'''

'''print("Give me two numbers and I'll divide them")
print("Enter 'q' to quit")

while True:
    f_num = input("Enter first number: ")
    if f_num == "q":
        break
    s_num = input("Enter second number: ")
    if s_num == "q":
        break
    try:
        answer = int(f_num) / int(s_num)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(f"{f_num} / {s_num} = {round(answer, 2)}")'''

'''file = "programming.txt"
try:
    with open(file) as fp:
        contents = fp.read()
except FileNotFoundError:
    print("Sorry, the file " + file + " does not exist.")
else:
    num = len(contents.split())
    print("The file " + file + " has about " + str(num) + " words.")'''

'''def count_words(file):
    try:
        with open(file) as fp:
            contents = fp.read()
    except FileNotFoundError:
        pass
        #print("Sorry, the file " + file + " does not exist.")
    else:
        num = len(contents.split())
        print("The file " + file + " has about " + str(num) + " words.")
    
filenames = ['alice.txt', 'guest_book.txt', 'programming.txt', 'little_women.txt']
for file in filenames:
    count_words(file)'''

'''while True:
    f_n = int(input("Enter first number: "))
    s_n = int(input("Enter second number: "))
    try:
        addition = f_n + s_n
    except TypeError:
        print("Sorry You didn't enter numbers, Try Again!")
    else:
        print(f"{f_n} + {s_n} = {addition}")'''

'''def contents(file):
    try:
        with open(file) as fp:
            contents = fp.read()
    except FileNotFoundError:
        pass
        #print("File is in the wrong path")
    else:
        print(contents)

files = ["cats.txt", "dogs.txt"]
for file in files:
    contents(file)'''

'''line = "Row, row, row your boat"
print(line.count("row"))
print(line.lower().count('row'))'''

'''numbers = [2, 3, 5, 7, 11, 13]
with open("numbers.json", "w") as fp:
    json.dump(numbers, fp)
    
with open("numbers.json") as fp:
    num = json.load(fp)
print(num)'''

'''username = input("Enter your name: ")

filename = "username.json"
with open(filename, "w") as fp:
    json.dump(username, fp)
    print("We'll remember you when you come back, " + username + "!")

with open(filename) as fp:
    user = json.load(fp)
    print("Welcome back, " + user + "!")'''

'''def greet_user():
    filename = "username.json"
    try:
        with open(filename) as fp:
            username = json.load(fp)
    except FileNotFoundError:
        username = input("Enter your name: ")
        with open(filename, "w") as fp:
            json.dump(username, fp)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()'''

#practice
'''filename = "username.json"

def get_username():
    with open(filename) as fp:
        username = json.load(fp)
    return username

def get_new_username():
    username = input("Enter your name: ")
    with open(filename, "w") as fp:
        json.dump(username, fp)
        print("We'll remember you when you come back, " + username + "!")
    return username

def greet_user():
    username = get_username()
    if username:
        ask = input(f"Are you {username} (y/n) ?").lower()
        if ask != 'y':
            username = get_new_username()
        else:
            print(f"Welcome back! {username.title()}")
    else:
        username = get_new_username()

greet_user()'''

'''filename = "fav.json"
try:
    with open(filename) as fp:
        fav_num = json.load(fp)
        print(f"I know you favourite number is {fav_num}")
except FileNotFoundError:
    favourite = input("What's your favourite number? ")
    with open(filename, "w") as fp:
        json.dump(favourite, fp)'''

#Testing
'''print("Enter 'q' at any time to quit! ")

while True:
    first = input("Enter first name: ")
    if first == "q":
        break
    last = input("Enter last name: ")
    if last == "q":
        break

    fullname = get_formatted_name(first, last)
    print("\tNeatly Formatted Name :", fullname + ".")'''

#First code of testing

'''class NameTestCase(unittest.TestCase):
    #Test for name_function.py
    def test_fist_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")

unittest.main()'''

#Practice

'''class CheckName(unittest.TestCase):

    def test_city_country(self):
        full = get_city_country_name( 'santiago' , 'chile')
        self.assertEqual(full, "Santiago, Chile")

    def  test_city_country_population(self):
        full = get_city_country_name('santiago', 'chile', population= '5000000')
        self.assertEqual(full,  'Santiago, Chile - Population 5000000')

unittest.main()'''

#Testing Classes 
'''question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    my_survey.store_responses(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()'''


'''class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_responses("English")

        self.assertIn("English", my_survey.responses)

    def test_store_three_responses(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ["English", "Spanish","Chienese"]
        for response in responses:
            my_survey.store_responses(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main() '''

#modified using setup() method
'''class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        self.my_survey.store_responses(self.responses[0])
        self.assertIn("English", self.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_responses(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()'''

#Practise
'''class TestEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.employee = Employee("John", "Doe", 60000)

    def  test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.ann_salary, 65000)

    def test_give_custom_raise(self): 
        self.employee.give_raise(6000)
        self.assertEqual(self.employee.ann_salary, 66000)

unittest.main()'''







