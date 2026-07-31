'''
What is an Array?
An Array is a collection of elements stored in sequence.

Example :
arr = [10 , 20 , 30 , 40 , 50]

visualizetion :
index : 0   1     2     3   4
array : 10 , 20 , 30 , 40 , 50

why array ?
instead of creating many variables:

a = 10
b = 20
c = 30
d = 40

we use :
arr = [10,20,30,40]

Creating Array :
nums = [ 10 , 20 , 30 , 40]

fruits = ["apple" , "banana" , "mango" , "grapes"]

mixed = [10 , "apple" , 20.5 , True]
Python allows mixed data type.

'''

# Accessing Element in Array
arr = [10 , 20 , 30 , 40 , 50]
print(arr[0])
print(arr[2])
print(arr[-1])

# Updating element in array
arr[3] = 120
print(arr)

# Traversing an Array
# Method 1
arr = [5 , 10 , 15 , 20 , 25]
for item in arr:
    print(item)

# method 2

for i in range(len(arr)):
    print(f"index: {i} -> arr : {arr[i]}")  

# Finding Length
print(len(arr))

numbers = [12, 25, 36, 48, 50]
for num in numbers:
    print(num)
      
arr = [5, 10, 15, 20]
arr[2] = 100
print(arr)

marks = [80, 75, 90, 65, 88]

print("First : ", marks[0])
print("last : ", marks[-1])
print("Total subject ; ", len(marks))

arr = [ 10,20,30,40,50]
print("First element : ", arr[0])
print("Last element : ", arr[-1])
print("Total Element: ", len(arr))