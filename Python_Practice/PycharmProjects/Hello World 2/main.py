# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

tens = list(range(1,10))
print(tens)
print(sum(tens))
print(max(tens), min(tens))

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[:-1])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
my_foods = ['pizza', 'falafel', 'carrot cake']
x = my_foods[:]
print(x)
my_foods.append('cannoli')
x.append('ice cream')
print("My foods are:")
print(my_foods)
print("My friend's foods are:")
print(x)

y = my_foods
y.append("Rangoli")
print(my_foods)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for x in dimensions:
    print(x)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'audi'
print(car == 'bmw')
print(int(car == 'bmw'))

age1 = 21
age2 = 18
print(age1>=21 and age2>=21)
age2 = 25
print(age1>=21 and age2>=21)

age2 = 14
print(age1>=21 or age2>=21)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('ale' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

print('\n')
if age < 4:
    price = 5
elif age < 18:
    price = 10
else:
    price = 15
print("Your admission cost is $" + str(price) + ".")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for x in requested_toppings:
        print("Adding " + x + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

del alien_0['points']
print(alien_0)

user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for x, y in user_0.items():
    print("Key = " + x.upper())
    print("Value = " + y.lower())
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print('\n\n')
for language in set(favorite_languages.values()):
    print(language.title())

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
x = [alien_0, alien_1, alien_2]
for y in x:
    print(y)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell']}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

users = {
 'aeinstein': {'first': 'albert','last': 'einstein','location': 'princeton',},
 'mcurie': {'first': 'marie','last': 'curie','location': 'paris',},
 }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

#name = input("Please enter your name: ")
#print("Hello " + name)

#prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt += "\nWhat is your first name? "
#name = input(prompt)
#print(prompt + name)
#age = input("How old are you? ")
#print(age)
#age = int(age)
#print(age >= 18)

'''height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")'''
#This is known as multiple line comment

print(4%3)
print(str(6%3))

'''num = input("Enter a number and I will tell you if it is even or odd: ")
num = int(num)
if num % 2 == 0:
    print("Number " + str(num) + " is even!")
else:
    print("Number " + str(num) + " is odd!")'''

num = 1
while num <= 5:
    print(num)
    num += 1

prompt = "Tell me something I will print: "
prompt += "Enter 'quit' to end"
message = " "
'''while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)'''
'''active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)'''
'''while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)'''

num = 0
while num < 10:
    num += 1
    if num %2 == 0:
        continue
    print(num)

x = 1
while x  <= 5:
    print(x)
    x+=1

cu = ['Asiya', "Ayesha", "Daniyal", "Ahmed"]
ccu = []

while cu:
    x = cu.pop()
    print("Verifying user: ", x)
    ccu.append(x)
print("\nThe following users have been confirmed!")
for x in ccu:
    print(x.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)

'''responses = {}
polling_active = True
while polling_active:
    name = input("Enter name: ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Wannna repeat? ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")'''

def print_(username):
    print("Hello", username.title(), "!")

print_(username = "Asiya")

def fullname(first, last):
    full = first + ' ' + last
    return full.title()
print(fullname("asiya", "sohail"))

def fullname(first, last, age = ''):
    person = {'first' : first, 'last' : last}
    if age:
        person['age'] = age
    return person
print(fullname("asiya", "sohail", 19))

def fullname_(first, last):
    return first.title() + ' ' + last.title()

'''while True:
    print("Enter 'q' to quit anytime")
    first = input("Enter first name: ")
    if first == 'q':
        break
    last = input("Enter last name: ")
    if last == 'q':
        break

    full = fullname_(first, last)
    print("Assalamolikum" , full, "!")'''

def greet_users(list):
    for x in list:
        print("Hello", x.title(), "!")

users = ["Asiya", 'Kiran', "Mahnoor" ,"sarah"]
greet_users(users)

''''# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
# Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)'''

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models[:])
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)

def make_pizza(size, *toppings):
    print("Making a -" + str(size) + " size pizza with following toppings!")
    for x in toppings:
        print("-" + x)

make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese' )

def user(first, last, **many):
    person = { }
    person['first'] = first.title()
    person['last'] = last.title()
    for key, value in many.items():
        person[key] = value
    print(person)

user('asiya', 'sohail', location = "Pakistan", id = 13245, age = 19)

#Exceptions
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

filename = "test.txt"
try:
    with open(filename) as f:
        print(f.read())
except FileNotFoundError:
    print(f"Sorry the file {filename} doesn't exist")
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")











