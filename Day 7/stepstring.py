# Step Slicing
# Syntex
# string[start:end:step]

'''
There are three parts
[ start : end : step]

part           Meaning
start          The starting index of the slice. It is inclusive, meaning the character at this index
end            The ending index of the slice. It is exclusive, meaning the character at this index
step           The step value determines the increment between each index for slicing. It can be positive or negative.

Imagine the string:
text = "PYTHON"

Indexs ;
P  Y  T  H  O  N
0  1  2  3  4  5


'''

# EXAMPLE 
text = "PYTHON"
print(text[0:6:1])

'''
step = 1
means "
P → Y → T → H → O → N
Nothing Special 
'''

# Example
print(text[0:6:2])  #output "PTO"

'''

0 → P
jump 2
2 → T
jump 2
4 → O


Python Understend :-

start = beginning
end = end
step = 2
'''

# Negative Step
# Negitive Step Means ,
# "Move Beckword"

# Example
text = 'PYTHON"'
print(text[::-1])  # output "NOHTYP"
print(text[::-2]) # output "NHY"

'''
Notes Importent :

Index 0 is not included because slicing always exclude  the ending index.

'''

# Reverse String
text = "PYTHON"
reverse = text[::-1]
print(reverse) # output "NOHTYP" 
# This is the shortest and fastst Python way.

# Method 2
text = "Python"
reverse = ""

for ch in text:
    reverse = ch + reverse
print(reverse)    

# this is teachs how to reverse a string using logic and loop.

'''

String is Immutable

Suppose  :
name = "meet"
name [0] = "B"  # it is get error 

correct method :

name = "Meet"

name = "B" + name[1]

print(name)  # output "Beet"

we didn't change the old string.
Python make a new string.

Easy trik to understend :

List , Dictionary , set is Mutable
String , Tuple is Immutable

'''

# Example 

name = "Meet"
name = "B" + name[1]
print(name)  # output "Beet"

text = "Programming"
print(text[::2])  # Output: "Pormig"
print(text[::-1])  # Output: "gnimmargorP"
print(text[3:9:2]) 
print(text[-5:])

text = "Ahmedabad"
reverse = text[::-1]
print(reverse)  

reverse = ""

for ch in text :
    reverse = ch + reverse
print(reverse)    