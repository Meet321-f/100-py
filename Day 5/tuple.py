# 1 . Tuples
# A tuple is a si,ilar to a list, but it cannot be change after creation. (immutable)
# Creating a tuple

t = ( 10 , 20 , 30)
print(t)

# Accessing elements
t = ( 5 , 10 , 15 , 20 )
print(t[0])
print(t[3])
# Negitive indexing also work
print(t[-2])

'''
Why use tuples?
use tuple when data should never change after creating.

Example

days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

'''
'''
 Tuple methods
 Only two methods exist.

1 . tuple packing
student = ("Meet", 21, "Python")
python pack value autometically

2 . tuple unpacking
name, age, course = student

print(name)
print(age)
print(course)

output :
21
python
 '''

# create a tuple and print first , last and lenth of tuple
t = (100,200,300,400,500)
print(t[0])
print(t[-1])
print(len(t))

