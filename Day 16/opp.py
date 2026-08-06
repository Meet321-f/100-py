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

# # class created 
# class Car:
#     color = "Blue"
#     brand = "Toyota"

# # who a object created
# c1 = Car()
# print(c1.color)  # output: Blue
# print(c1.brand)  # output: Toyota    

# constructor = constructor is a special method which is used to initialize the object of class.
#  _init_() = constructor method in python.

