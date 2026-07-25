# Create a list of five fruits.
fruits = ['apple' , 'banana' , 'mango' , 'orange', 'grapes']
print(fruits)

# Print the first and last element.
fruits = ['apple' , 'banana' , 'mango' , 'orange', 'grapes']
print(fruits[0])
print(fruits[-1])

# Replace the second element.
fruits = ['apple' , 'banana' , 'mango' , 'orange', 'grapes']
fruits[1] = 'kiwi'
print(fruits)

# Add a new fruit using append().
fruits = ['apple' , 'banana' , 'mango']
fruits.append('kiwi')
print(fruits)

# Insert a fruit at index 2.
fruits = ['apple' , 'banana' , 'mango']
fruits.insert(2, 'kiwi')
print(fruits)

# Remove a fruit using remove().
fruits = ['apple' , 'banana' , 'mango' ]
fruits.remove('banana')
print(fruits)

# Remove the last element using pop().
fruits = ['apple' , 'banana' , 'mango' ]
fruits.pop()
print(fruits)

# Sort a list of numbers.
num = [ 50 , 20, 60, 70]
num.sort()
print(num)

# Reverse a list.
num = [ 50 , 20, 60, 70]
num.reverse()
print(num)

# Count how many times 5 appears in a list.
num = [ 5 , 2 , 5 , 3 , 5 ]
print(num.count(5))

# Find the index of an element.
num = [ 1,2,3,4]
print(num.index(3))

# Copy one list into another.
a = [ 1,2,3]
b = a.copy()
print(b)

# Print all elements using a for loop.
fruits = ['apple' , 'banana' , 'mango' ]
for f in fruits:
    print(f)


# Find the largest element without using max().
num = [1, 10, 159, 64, 7, 3, 9]
max_value = num[0]
for n in num:
    if n > max_value:
        max_value = n
print(max_value)        

# Find the smallest element without using min().
num = [1, 10, 159, 64, 7, 3, 9]
min_value = num[0]
for n in num:
    if n < min_value:
        min_value = n
print(min_value)

# Calculate the sum of all elements.
num = [1, 10, 159, 64, 7, 3, 9]
sum = 0
for n in num:
    sum += n
print(sum)

# Remove duplicate elements.
num = [1, 10, 159, 64, 7, 3, 9, 10, 3]
sequence = []
for n in num:
    if n not in sequence:
        sequence.append(n)
print(sequence)   

#  Multiplication table using nested lists
table = []
for i in range(1,6):
    row = []
    for j in range(1,6):
        row.append(i * j)
    table.append(row)
print(table)

# Even numbers using list comprehension
even = [i for i in range(21) if i % 2 == 0]
print(even)

# Squares using list comprehension
squares = [i*i for i in range(10)]
print(squares)