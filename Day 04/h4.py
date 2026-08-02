# Print all elements using a for loop.
my_items = ['apple', 'banana', 'cherry']
for item in my_items:
    print(item)  # Output: apple, banana, cherry


# Multiplication table using nested lists.
table = []

for i in range(1,11):
    row = []
    for j in range(1,11):
        row.append(i * j)
    print(row)    

# Even numbers using list comprehension.
even = [i for i in range(1,31) if i % 2 == 0]
print("Even Numbers : " ,even)

# Squares from 1 to 20 using list comprehension.
Squares = [i*i for i in range(1,21)]
print("Squares from 1 to 20 : " ,Squares)