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
