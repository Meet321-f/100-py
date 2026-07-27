'''
What is a String?
A string is a sequence of characters.

characters inside : -

letters
symbols
numbers
space

python stores text inside a quotes.

name = "Meet"
city = 'Mumbai'

Both single (' ') and double (" ") quotes work.


'''

# Example
name = "Meet"
print(name)

# Examole 
message = 'Hello World'
print(message)

# Example
# Numbers inside quotes become strings.
age = "21"
print(age)
print(type(age))  # Output: <class 'str'>
# without quotes, it will be an integer.

# Creating String
a = "python"
b = 'programming'
c = ""

print(c) # Output: (empty string)

# Multiple Line String
# use triple quotes.
text =  """ Hello 
i am Meet.
i am learning python. """
print(text)

'''
Strings are Immutable
Once a string is created, you cannot change individual characters.

Example
name = "Meet"
name[0] = "m"  # This will raise an error because strings are immutable.
'''

'''
Escape characters:

\n → New line
\t → Tab
\" → Double quote
\' → Single quote
\\ → Backslash
'''

name = "Meet"
print(name)
city = "Mumbai"
print(city)
college = "CGPIT"
print(college)
course = "Computer Science"
language = "Python"
print(course)
print(language)


# String Indexing
# Positive Indexing

'''
String Indexing

Every character in a string has an index (position).

Python starts counting from 0.

Example:

M  e  e  t
0  1  2  3

This is called Positive Indexing.
'''

# Example 1
name = "Meet"
print(name[0])  # Output: M
print(name[1])  # Output: e
print(name[2])  # Output: e
print(name[3])  # Output: t

'''
Negative Indexing

Python also supports negative indexing.

It starts counting from the end.

M  e  e  t
-4 -3 -2 -1
'''

print(name[-1])  # Output: t
print(name[-2])  # Output: e

'''
Accessing a Single Character

Use square brackets [] with the index.
'''

word = "programming"
print(word[0])
print(word[1])

'''
Length of a String

Use the len() function to find the total number of characters.
'''
print(len(word))  # Output: 11

'''
IndexError

If you try to access an index that doesn't exist,
Python raises an IndexError.
'''

'''
example
name = "Meet"
print(name[10]) 
# This will raise an IndexError because the index 10 is out of range.
'''
# You can also use variables  as a indexing.
name = "python"
i = 2
print(name[i])  # Output: t

a = "Computer"
print(a[0])
print(a[-1])

name = "meet"
j = 0
i = -1
print(name[j])  # Output: m
print(name[i])  # Output: t

b = "Artificial Intelligence"
print(len(b))

language = "Programming"
print(language[0])  # Output: P
print(language[2])
print(language[-1])  # Output: g
print(language[-2])  # Output: n
print(len(language))  # Output: 11


# String Slicing
'''
String Slicing

slicing is a used to get a part of a string.

syntex: 
string[start:end]

The Starting Index INCLUDED.
The end Index is EXCLUDED.

Example :

P  y  t  h  o  n
0  1  2  3  4  5

string[1:4]

output :
yth

'''

word = "programming"
print(word[0:4])  # Output: prog

# If the start index is omitted,
# Python starts from index 0.

print(name[:4])

# If the end index is omitted,
# Python goes until the last character.

name = "Python"
print(name[2:])

