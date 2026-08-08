# Abstrection  : hiding the implimentetion details of a class and only showing the functionality to the user

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clach = False

    def Start(self):
        self.clach = True
        self.acc = True
        print("Car Staryed")


c1 = Car()
c1.Start()

# Encapsulation = Encapsulation is the process of wrapping data and methods into a single unit (class) and controlling direct access to the data.

# example ;
class student:
    def __init__(self , name , marks):
        self.name = name       # public attribute
        self.__marks = marks   # private attribute

    def Display(self):
        print(self.name)
        print(self.__marks)     # only access in the class

    def get_marks(self):        # access using the class method
        return self.__marks      

s1 = student("Meet" , 21)
s1.Display()         
print(s1.name)          # public attribute can be accessed outside the class
print(s1.get_marks())   # access private attribute using the class method
# print(s1.__marks)     # private attribute can't be accessed outside the class


# Getter : getter is a value use to access or read a value from a private attribute of a class. It is a method that returns the value of a private attribute outside a class.
# Simple word ; "Getter : private data ko read/ access karna ka method."

# example 

class Student:
    def __init__(self , name , marks):
        self.name = name
        self._marks = marks   # protected attribute

    def get_marks(self):
        return self._marks

s1 = Student("Alice", 85)
print(s1.get_marks())        

'''
How get method is work inside code

Bank Account
┌────────────────────┐
│ balance = ₹50,000 🔒│
└────────────────────┘
          ↑
      get_balance()
          ↓
       ₹50,000

'''

# setter : setter is change or update data.
# simple word : Setter = private data ko change/update karne ka method.

class Student:
    def __init__(self , name , marks):
        self.name = name
        self._marks = marks

    def get_marks(self):
        return self._marks

    def set_marks(self , marks):
        self._marks = marks

s1 = Student("Alice", 85)
print(s1.get_marks())  # Output: 85

s1.set_marks(90)
print(s1.get_marks())







