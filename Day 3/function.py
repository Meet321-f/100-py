# syntex
#def fuction_name():
#code

#example
from numpy import square


def hello():
    print("Welcome to Pyhton")

hello()    

#P1
def helloguj():
    print("Good Morning Gujarat")

helloguj()

#p2
def collage():
    print("Uka Tarsadia University")
collage()

#p3
def square(num):
        print(num * num)
square(10)

#parameter

'''
Parameter → function ke andar variable.
Argument → function call ke time di gayi value.
'''

#print name useing parameter
def  great(name):
    print("Hello", name)
great("Meet")

#sum of 2 number
def sum(a , b):
    print(a + b)
sum(15 , 24)    

#student name and age 
def student(name , age):
    print(name)
    print(age)
student("Meet", 21)

# 1 to 10 multiplication table
def table(num):
    for i in range(1, 11):
        print(num , "x", i, "=", num * i)
table(5)        

#addition using return fuxtion
def add(a, b):
    return(a+b)
resullt = add(10,34)
print(resullt)

def square(num):
    return num * num
result = square(10)
print(result)

#3rd cube
def cube(num):
    return num ** 3
result = cube(4)
print(result)

#largest number
def largest(a , b):
    if a > b:
        return a
    else:
        return b
result = largest(110, 20)
print(result)

#even
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
result = is_even(10)
print(result)

#calculator
def calculator(a,b):
    return a + b , a - b , a * b , a / b , a % b
result = calculator(10, 5)
print("Addition:", result[0])
print("Subtraction:", result[1])    
print("Multiplication:", result[2])
print("Division:", result[3])
print("Modulus:", result[4])

#two type of veriable
#local varialble jo function ke andar define hota hai
def demo():
    a = 10
    print(a)
demo()    

#global veriable jo function ke bahar define hota hai
name = "Meet"
def demo():
    print(name)
demo()    

count = 0
def incress():
        global count
        count += 1

incress()
print(count)    

#welcome message using function
collage = "Uka Tarsadia University"

def welcome(name):
    print("Welcome" , name,  "to", collage)
welcome("Meet")
   