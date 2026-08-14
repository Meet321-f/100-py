'''
Besic syntsx of import:
import modul_name

if we wont a specific function from a modul we can use the following syntax:
from modul_name import function_name

Multiple functions can be imported from a modul using the following syntax:
from modul_name import function1 , function2 , function3

import...as fuction_name can be used to give a function an alias name

datetime modul
data/time ke liye python me ek built in modul hai jiska name datetime hai. is modul ka use date aur time ke sath kaam karne ke liye kiya jata hai. is modul me kai sare classes aur functions hote hai jo date aur time ke sath kaam karne me help karte hai.

we can also make a coustome modul and here is the modul is "import cal"
'''

import cal  , random , datetime , os
import math as m      # modul ko short name de sakte he 
from math import sqrt , factorial

print(cal.add(10, 20))
print(cal.sub(10, 20))

# print(math.sqrt(16))      # math is a python built in modul , used for mathematical operations
# print(math.pi)
print(m.sqrt(16))      # m is a short name of math modul , used for mathematical operations

print(sqrt(16))           # sqrt is a function from math modul , used to find the square root of a number
print(factorial(5))      # factorial is a function from math modul , used to find the factorial of a number

print(random.randint(1, 10))      # random is a python built in modul , used to generate random numbers

today = datetime.date.today()
print(today)      # datetime is a python built in modul , used to work with date and time
today = datetime.datetime.now()
print(today)      # datetime is a python built in modul , used to work with date and

print(cal.add(10,12))
print(cal.sub(10 , 5))
print(cal.mul(10 , 5))
print(cal.div(10 , 5))

print(random.randint(1, 100))      # random is a python built in modul , used to generate random numbers


today = datetime.date.today()
print("Date: ", today) 
today = datetime.datetime.now().strftime("%H:%M:%S")
print("Time: ", today)
print("Day: ", datetime.datetime.now().strftime("%A"))


print(os.getcwd())
print(os.listdir())
print(os.path.exists("Day 24"))
print(os.path.exists("Day 25"))