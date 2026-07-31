# What is String Formatting?
# String formeting means inserting variables or valus into a string.

# Example 
name = "Meet"
age = 21

print("My name is Meet and i am 21 year old.")
# Instead of writing values manually, we use formatting.
#f-string() 
'''
syntex :
name = "Meet"
age = 21
print(f"My name is {name} and i am {age} year old.")
output :- My name is Meet and i am 21 year old.
enything inside {} is evaluted.


'''

# Example :
a= 10
b = 20
print(f"sum: {a+b}")

# Expressions inside f-Strings

x = 15
y = 5

print(f"{x} + {y} = {x+y}")  # Output: 15 + 5 = 20
print(f"{x}- {y} = {x-y}")  # Output: 15 - 5 = 10
print(f"{x} * {y} = {x*y}")  # Output: 15 * 5 = 75
print(f"{x} / {y} = {x/y}")  # Output: 15 / 5 = 3.0

# Formatting Decimal Numbers

pi = 3.141592653589793
print(f"Value of pi: {pi:.2f}")  # Output: Value of pi: 3.14
print(f"Value of pi: {pi:.4f}")  # Output: Value of pi: 3.1416

# Width Formatting
num = 5
print(f"{num:5}")  # Output:     5 (right-aligned with width 5)
print(f"{num:0<5}")  # Output: 00005 (left-aligned with width 5 and zero-padding)

# .format() Method - befor f-string() python use .formet()
name = "Meet"
print("Hello {} ".format(name))  # Output: Hello Meet

# Multi value
name = "Meet"
age = 21
print("Name : {} Age: {} ".format(name,age))  # Output: Name : Meet Age: 21

print("name : {m} Age ; {a} ".format(m = "Meet" , a= 21))  # Output: name : Meet Age ; 21

# Old % Formatting
name = "Meet"
marks = 90

print("Name ; %s " %name)
print("Marks : %d " %marks)

name = input("Enter name: ")
city = input("Enter city: ")

print(f"Hello {name}, welcome to {city}!")

price = 149.5678
print(f"Price = ₹{price:.3f}")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
percentage = float(input("Enter your percentage: "))

print("Student Details".center(25, "-"))
print(f"Name     :    {name}")
print(f"Age      :    {age}")
print(f"Percentage:   {percentage:.2f}%")
