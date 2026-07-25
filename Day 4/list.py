#list
# what is list ?
# A List is a collection of multiple values stored in one variable.

# example

fruits = ['Apple' , 'banana' , 'mengo']
print(fruits)

# 2nd Creating Lists
#integer List

number = [ 1,2,3,4,5]
print(number)

# String List
# save a string Values in a list
name = ['Meet' , 'Fenil' , 'Krish']
print(name)

# Mixed list
# save a multiple data type values in a list
data = [ 1 , 'Meet' , 'True' , 5.4]
print(data)      # Python allows different data types inside one list.

'''
3rd Indexing in List
Indexing is used to access individual items in a list. Each item in a list has an index, starting from 0 for the first item.
every item has an index

0        1        2        3
A        B        C        D

'''

# Example
letters = ['A' , 'B' , 'C' , 'D']
print(letters[0])  # Output: A
print(letters[1])  # Output: B
print(letters[2])  # Output: C
print(letters[3])  # Output: D

'''
4. Negative Indexing
Python can count from the end
-4       -3       -2       -1
A        B        C        D
'''

# Example
letters = ['A' , 'B' , 'C' , 'D']
print(letters[-1])  # Output: D
print(letters[-2])  # Output: C
print(letters[-3])  # Output: B
print(letters[-4])  # Output: A

# 5. Slicing
# Syntax
# string[start:end]

# Example
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [2, 3, 4]

# 6. Updating List
# Lists are mutable, meaning you can change their content without changing their identity.

friuts = ['Apple', 'Banana', 'Mango']
# Update the second item
friuts[1] = 'Orange'
print(friuts)  # Output: ['Apple', 'Orange', 'Mango']

# 7. Important List Methods
# append()
# Adds one item at the end.

number = [ 1 ,2 , 3 ]
number.append(4)
print(number)

# insert ()
# insert at any position
number = [ 1 , 2 , 3 ]
number.insert(1,100)  # Insert 100 at index 1
print(number)  # Output: [1, 100, 2, 3]

# extend()
# adding another list
a = [ 1,2]
b = [3,4]
a.extend(b)
print(a)  # Output: [1, 2, 3, 4]

# remove()
# remove an item from the list
fruits = ['Apple', 'Banana', 'Mango']
fruits.remove('Banana')
print(fruits)  # Output: ['Apple', 'Mango']

# pop()
# remove using index
fruits = ['Apple', 'Banana', 'Mango']
fruits.pop(1)  # Removes the item at index 1
print(fruits)  # Output: ['Apple', 'Mango']

# sort()
# sort the list in ascending order
numbers = [ 50 , 100 , 800 , 40]
numbers.sort()
print(numbers)  # Output: [40, 50, 100, 800]

# reverse()
# reverse the list
numbers = [ 50 , 100 , 800 , 40]
numbers.reverse()
print(numbers)  # Output: [40, 800, 100, 50]

# count()
# count the number of occurrences of an item in the list

numbers = [ 1 , 2 , 2 , 2 , 4 , 2 ]
print(numbers.count(2))  # Output: 4

# index()
# returns the index of the first occurrence of an item in the list

numbers = [ 1 , 2 , 3 , 2 , 4 , 2 ]
print(numbers.index(2))  # Output: 1

#copy()
# copy the list
a = [1,2,3]
b = a.copy()
print(b)  # Output: [1, 2, 3]

# clear()
# clear the list

numbers = [ 1 , 2 , 3 , 4 ]
numbers.clear()
print(numbers)  # Output: []

# 8. Nested List
# A nested list is a list that contains other lists as its elements.
metrix = [
    [1,2],
    [3,4]
]
print(metrix)
print(metrix[1])
print(metrix[1][0])  # Output: 3

# 9. List Comprehension (Introduction)
square  = []
for i in range(5):
    square .append(i*i)

print(square )  # Output: [0, 1, 4, 9, 16]




