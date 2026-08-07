# opp in python

# 1. Class = class is a blue-print to creating object.
# creating class 
'''
class student: 
    name = "Meet"

class name alweys start from cepital lettter.

      
'''

# Example 

class Student:

    def __init__(self , name , marks ):     # using th self perameter we store diffarent values to diffarent object.
        self.name = name
        self.marks = marks
        print("Adding New Student in Database.")



s1 = Student("Meet", 85)
print(s1.name)  # output: meet
print(s1.marks)  # output: 85
# the data stored inside a class or varible we can say tha data to a atributes.

# example 

# class created 
class Car:
    color = "Blue"
    brand = "Toyota"

# who a object created
c1 = Car()
print(c1.color)  # output: Blue
print(c1.brand)  # output: Toyota    

constructor = constructor is a special method which is used to initialize the object of class.
 _init_() = constructor method in python.

class & instance attributes
 
class Student:
    collage_name = "Amtics"  # class attribute
    def __init__(self , name , marks ):     # using th self perameter we store diffarent values to diffarent object.
        self.name = name
        self.marks = marks
        print("Adding New Student in Database.")

s1 = Student("Meet", 85)
print(s1.name)  # output: meet
print(s1.marks)  # output: 85
print(s1.collage_name)  # output: Amtics


class Student:
    def __init__(self , name , marks ):     # using th self perameter we store diffarent values to diffarent object.
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome Student.", self.name)    

    def get_marks(self):
        return self.marks

s1 = Student("Meet", 85)
print(s1.name)  # output: meet
print(s1.marks)  # output: 85
s1.welcome()  # output: Welcome Student.
print(s1.get_marks())  # output: 85

