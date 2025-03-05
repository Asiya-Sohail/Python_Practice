# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

a = 35701579205
b = 78.804
c = 'Javeria'
d = True
e = None
print("Hello", "World")
print(a)
print(b)
print(c)
print(d)
print(e)

a, b, c = 1, 2, 3
print(a, b, c)

a = b = c = 1 # all three names a, b and c refer to same int object with value 1
print(a, b, c)

x = y = [7, 8, 9]
x[0] = 13
print(y)

x = [1, 2, [3,4, 5], 7, 8, 6]
print(x[2], x[-1])

def myfunction():
    a = 2
    return a
print(myfunction())

a = 2
b = 7
if a>b: print(a)
else: print(b)

if x > y:
    pass
y = x
print(y)

c = 123456789.e9
print(c)

b = 100 + 10j
print(b)

i = "79"
if isinstance(i, int):
    i += 1
    print(i)
elif isinstance(i, str):
    i = int(i) + 1
    print(i)

x = None
if x is None:
    print("Not a surprise. I just defined x")

a = '123.956'
b = float(a)
#c = int(a) # ValueError: invalid literal for int() with base 10: '123.456'
d = int(b)
print(b, d)

a = 'hello'
print(list(a))
print(tuple(a))
print(set(a))

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first = "\tAli"
last = "Sohail"
name = first + " " +  last
print(name)
print("Hello", name.title(), "!")
print("Hello\n", name.title(), "\t!")
print(first.rstrip())
favorite_language = 'python '
print(favorite_language.rstrip())

name = "Albert Einstein"
quote = '"A person who never made a mistake never tried anything new."'
print(name, "once said,", quote)

print(2+3)
print(0.1+0.1)
print(0.2-0.04)
print(2  * 0.1)

age = 19
message = "Happy " + str(age) + " Birthday!"
print(message)
print(3/2)
# Zen Of Python
import this

bicycle  = ['redline', 'trek', 'specialized']
print(bicycle[0].title())
print(bicycle[-1].title())

message = "My first bicycle was " + bicycle[0].title() + "."
print(message)

colour = ['red', 'blue', 'green']
print(colour)
colour[0] = 'yellow'
print(colour)
colour.append('red')
print(colour)
del colour[-1]
print(colour)
colour.insert(0, 'red')
print(colour)

print("My favourite colour is", colour.pop(0) )
print(colour)

colour.remove('yellow')
print(colour)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
print(len(cars))

magicians = ['alice', 'david', 'carolina']
for x in magicians:
    print(x)
    print(x.title() +  ", that was a great trick!")
print("Thank You Everyone!")

message = "Hello Python world!"
print(message)

for value in range(1,6):
    print(value)

even_numbers = list(range(2,11,2))
print(even_numbers)

for value in range(1,6):
    print(value**2)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,6)]
print(squares)

cubes = [value**3 for value in range(1,11)]
print(cubes)


import randomword as r
print(r.get_random_word())

