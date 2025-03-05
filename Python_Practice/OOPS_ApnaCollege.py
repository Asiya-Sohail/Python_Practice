# Normal or Intro
'''class student:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod     #doesn't need self as a parameter
    def hello():
        print("Hello")

    def get_avg (self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hi", self.name, "Your Average score:", sum/3)

s1 = student("tony", [78, 65, 99])
s1.name = "Iron man"
s1.marks = [92, 53, 76] 
s1.get_avg()
s1.hello()'''

# Abstraction (Hidden one)
'''class Car:
    def _init_(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.brk = True
        print("Car Started...")

c1 = Car()
c1.start()'''

# Practice Question
'''class Account:
    def _init_(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited.")
        print("Total balance:", self.get_balance())
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited.")
        print("Total balance:", self.get_balance())
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 123456)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)'''

#Delete Attribute or method
'''class Student:
    def _init_(self, name):
        self.name = name
s1 = Student("Shradha")
print(s1.name)
del s1
#print(s1.name) Error becuase it's deleted'''

#Private attributes
'''class Account:
    def _init_(self, acc_no, acc_bal):
        self.acc_balance = acc_bal
        #self.__acc_no = acc_no
p1 = Account(12345, "abhki")
#print(p1.__acc_no)  #Private giving error
print(p1.acc_balance)'''

#Private attributes inside a function
'''class Person:
    __name = "Anonymous"
    def __hello(self):
        print("Hello Person")
    def welcome(self):
        self.__hello() #Private method used inside the class

p1 = Person()
print(p1.welcome())'''

# Inheritance (simple)
'''class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car):
    def _init_(self, name):
        self.name = name
c1 = ToyotaCar("fortuner")
c2 = ToyotaCar("Pirus")
print(c1.name)
print(c1.start())
print(c1.stop())
print(c1.color)'''

# multi-level inheritance
'''class Car:
    @staticmethod
    def start():
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car):
    def _init_(self, name):
        self.name = name

class Fortuner(ToyotaCar):
    def _init_(self, type):
        self.type = type
car1 = Fortuner("diesel")
car1.start()'''

# multiple inheritance
# child can have multpile parennts, alternatively multiple parents can inherit a single class
'''class A:
    varA = "Welcome to Class A"
class B:
    varB = "Welcome to Class B"

class C(A, B):       #Child class
    varC = "Welcome to Class C"
c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)'''

# Super() Method, used to access methods of parent Class (super means parent)
'''class Car:
    def _init_(self, type):
        self.type = type
    @staticmethod    #decorator #It is common for whole class (all objets)
    def start():
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car Stopped...")

class ToyotaCar(Car):
    def _init_(self, name, type): # (self, name, type)
        self.name = name     
        #self.type = type (This means in ToyotaCar obj a type attribute is created)
        #But we want to change parent class tyoe attribute
        super()._init_(type)
        super().start()
car1 = ToyotaCar("Prius", "electric")   #"electric" is a type 
print(car1.name)
print(car1.type) #At initial level error '''

# class method
# static method used for utility (can;t access or modify class state) no attribute or instance used
'''class Person:
    name = "Anonymous"
    def ChangeName(self, name):   #Instance methods  , instead of self, obj (Normal Method, self as an argument)
        #self.name = name  #New name created
        #Person.name = name  #This will change class name 1st method
        self.__class__.name = name #This will also change, self means object and object's class = class
p1 = Person()
print(p1.name)
p1.ChangeName("Rahul Kumar")
print(p1.name)
print(Person.name)   #we couldn't change class attribute for my object or instance'''

# If we want to access class directly through function
'''class Person:
    name = "Anonymous"
    @classmethod
    def ChangeName(cls, name):
        cls.name = name #This change will directly happen to class attribute

p1 = Person()
print(p1.name)
p1.ChangeName("Rahul Kumar")
print(p1.name)'''

# Property decorator (Method as a property) (It can change attributes in calculation)
'''class Student:
    def _init_(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
    @property
    def Percentage(self):
        return str((self.phy + self.chem + self.maths) / 3) + " %"

s1 = Student(77, 89, 72)
print(s1.Percentage)
s1.phy = 90
print(s1.Percentage)'''

# Polymorphism  Many forms/ faces
# One thing is used in many ways
# In python Best example of polymorphism is operator Overloading
# When same operator is allowed to have different meaning according to the context

# All of the following is implicit overloading
print(1 + 2)  # addition
print("apna" + "college")  # concatenate
print([1, 2, 3] + [4, 5, 6])  # merge

# Polymorphism example  (Dunder Function)
'''class Complex:
    def _init_(self, real, img):
        self.real = real
        self.img = img
    def ShowNum(self):
        print(self.real , "i +", self.img, "j" )

    def add(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)

n1 = Complex(2,3)
n1.ShowNum()
n2 = Complex(6, 8)
n2.ShowNum()
num3 = n1.add(n2)
num3.ShowNum()'''
# But I don't wanna make function I want that if I write num1 + num2 it autoatically adds
'''class Complex:
    def _init_(self, real, img):
        self.real = real
        self.img = img
    def ShowNum(self):
        print(self.real , "i +", self.img, "j" )

    def _add_(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)
    def _sub_(self, num2):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return Complex(newreal, newimg)

n1 = Complex(2,3)
n1.ShowNum()
n2 = Complex(6, 8)
n2.ShowNum()
num3 = n1 + n2    #because of dunder func _add_ This means + means changes
num3.ShowNum()
num4 = n1 - n2
num4.ShowNum()  '''
# This is operator overloading and this is application of Polymorphism

# Practice Questions
# Ques 1
'''class Circle:
    def _init_(self, radius):
        self.radius = radius
    def area(self):
        return (22/7) * self.radius ** 2
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())'''

# Ques 2
'''class Employee:
    def _init_(self, role, dep, salary):
        self.role = role
        self.dep = dep
        self. salary = salary
    def ShowDetails(self):
        print("Role :", self.role)
        print("Department :", self.dep)
        print("Salary :", self.salary)
e1 = Employee("Accountant", "Finance", "60,000")
e1.ShowDetails()

class Engineer(Employee):
    def _init_(self, name, age):
        self.name = name
        self.age = age
        super()._init_("Engineer", "IT", "75,000")
e1 = Engineer("Elon Musk", 40)
e1.ShowDetails()'''

# Ques 3 (_gt_ means greater than)
'''class Order:
    def _init_(self, item, price):
        self.item = item
        self.price = price
    def _gt_(self, ord2):
        return self.price > ord2.price

ord1 = Order("Chips", 20)
ord2 = Order("Tea", 15)
print(ord1 > ord2)'''