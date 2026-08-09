# del Keyword : delete the reference to the object
# del s1.name
#del s1

# class Student:
#     def __init__(self , name):
#         self.name = name

# s1 = Student("Meet")
# print(s1.name)
# del s1
# print(s1.name)

# # inheritance : 

# # Example of simple inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stop.")

# class Toyotacar(Car):
#      def __init__(self , name):
#          self.name = name

# car1 = Toyotacar("Fortuner")
# car2 = Toyotacar("Innova")

# print(car1.name)
# '''
# if i try to do like this "print(car1.start())" 
# here is not getting error because the first class or object
#  is used for the secound class of object.
# '''
# print(car1.start())

# # Multi level inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stop.")

# class Toyotacar(Car):
#      def __init__(self , brand):
#          self.brand = brand

# class Fortuner(Toyotacar):
#     def __init__(self , type):
#         self.type = type

# car1 = Fortuner("electric")      
# car1.start()  

# multiple inheritance :
class A:                          # class 1
    varA = "Welcome class A"

class B:                      # class 2
    varB = "Welcome class B"

class C(A , B):               # child class = this class is inherited from class A and class B
    varC = "Welcome class C"


c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)










