# Python String Methods

# upper() - Converts a string into uppercase

text = "hello python"
print(text.upper()) # Output: HELLO PYTHON

# lower() - Converts a string into lowercase
text = "HELLO , WELCOME TO PYTHON"
print(text.lower()) # Output: hello , welcome to python

# title() - Converts the first character of each word to uppercase
text = "hello , welcome to python"
print(text.title()) # Output: Hello , Welcome To Python

# capitalize() - Converts the first character of the string to uppercase
print(text.capitalize()) # Output: Hello , welcome to python

# swepcase() - Converts uppercase characters to lowercase and lowercase characters to uppercase
print("PyThOn".swapcase()) # Output: pYtHoN)

# Practice
print("Practice of String Methods")
name = "meet"
print(name.upper()) 

text = "PYTHON IS AWESOME"
print(text.lower()) 

city = "new york"
print(city.title()) 

sentence = "python programming"
print(sentence.capitalize()) 

text = "PyThOn123"
print(text.swapcase())

name = input("Enter your name: ")

print("Upper :", name.upper())
print("Lower :", name.lower())
print("Title :", name.title())
print("Capitalize :", name.capitalize())
print("Swapcase :", name.swapcase())


# strip() - Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
text = ("    Hello World      ")
print(text.strip()) # Output: Hello World
# It is remove spaces from the beginning and end of the string , it is not remove space between the characters of the string

text = ("Hello         World")
print(text.strip()) # Output: Hello         World

# lstrip() - Removes any leading characters (space is the default leading character to remove)
text = ("    Hello World      ")
print(text.lstrip()) # Output: Hello World

# rstrip() - remove space only from the right side of string
text = ("    Hello World      ")
print(text.rstrip()) # Output:     Hello World

# replace() - replace one part of string with the another part of string
text = "i like java"
print(text.replace("java", "python")) # Output: i like python

# find() - Finds the index of the first occurrence of a substring.
text = "Python Programming"
print(text.find("Programming")) # Output: 7
print(text.find("java")) # Output: -1 (not found)

# count() - cont how many time somting appears in the string
text = "Python is a programming language. Python is easy to learn."
print(text.count("Python")) # Output: 2

print("practice of strip, lstrip, rstrip, replace, find and count methods")
text = "   Meet Tailor   "
print(text.strip())

text = "   Python"
print(text.lstrip())

text = "Python   "
print(text.rstrip())

text = "I love Java"
print(text.replace("Java", "Python"))

text = "Python Programming"
print(text.find("Programming"))


text = "banana banana apple banana"
print(text.count("banana")) # Output: 3

name = input("Enter your name: ")
print("Strip :", name.strip())
print(name.title())
print(name.count("a"))
print(name.replace("a", "@"))


# startswith() - Returns True if the string starts with the specified value, otherwise False.
text = "Python is a programming language."
print(text.startswith("Python")) # Output: True
print(text.startswith("Java")) # Output: False

# endswith() - Returns True if the string ends with the specified value, otherwise False.
print(text.endswith("language.")) # Output: True
print(text.endswith("Python")) # Output: False

filename = "resum.pdf"
if filename.endswith(".pdf"):
    print("PDF file")

# split() - split string into a list.
text = "Apple banana Mengo"
print(text.split()) # Output: ['Apple', 'banana', 'Mengo']

# join() - combines a list into a string.
# "separator".join(list_name)

fruits = ["Apple", "Banana", "Mango"]
print("".join(fruits)) # Output: AppleBananaMango
print(" ".join(fruits)) # Output: Apple Banana Mango
print(",".join(fruits)) # Output: Apple,Banana,Mango
print("-".join(fruits)) # Output: Apple-Banana-Mango

# isalpha() - Returns True if all characters in the string are alphabetic and there is at least one character, otherwise False.
print("Hello".isalpha()) # Output: True
print("hello123".isalpha()) # Output: False

# isdigit() - check only digits 
print("12345".isdigit()) # Output: True

# isalnum() - it is check both alphabet and digit
print("Hello123".isalnum()) # Output: True
print("Hello 123".isalnum()) # Output: False (space is not alphanumeric)

# isspace() - check only space
print("   ".isspace()) # Output: True

text = input("Enter text: ")
print(text.startswith("hello"))
print(text.endswith("python"))
words = text.split()
print("Words:", words)
print("-".join(text))
print("Is alpha:", text.isalpha())
print("Is digit:", text.isdigit())
print(text.isalnum())
print(text.isspace())

