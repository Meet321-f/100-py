# Remaining String Methods

# index() - same as a find() , but if the substring is not found, it raises a ValueError instead of returning -1.
text = "Python Progeamming"
print(text.index("Progeamming")) # Output: 7
# if substring is not present its give error 
# print(text.index("Java"))
# Output: ValueError: substring not found

# Diffarence between find() and index() method
text = "Python"
print(text.find("java")) # Output: -1
'''
in the index() 
print(text.index("java")) 
output: ValueError: substring not found
'''

# rfind() - search from right side
text = "apple apple apple"
print(text.rfind("apple")) # Output: 12

# rindex() - same as rfind() , but if the substring is not found, it raises a ValueError instead of returning -1.
text = "apple apple apple"
print(text.rindex("apple")) # Output: 12
# if substring is not present its give error
# print(text.rindex("banana"))

# center() - text align in the center
text = "Meet"
print(text.center(20)) # Output: '        Meet         '
print(text.center(20, "-"))

# ljust() - text align in the left
text = "Meet"
print(text.ljust(20)) # Output: 'Meet                '
print(text.ljust(20, "-")) # Output: 'Meet----------------'

# rjust() - text align in the right
print(text.rjust(20)) # Output: '                Meet'
print(text.rjust(20, "-")) # Output: '----------------Meet'

text = "python python java"
print(text.index("java"))
print(text.rfind("python"))

name = input("enter your name; ")
print(name.center(20, "*"))
print(name.ljust(20 , "-"))
print(name.rjust(20, "-"))

text = "programming"
print(text.index("m"))
print(text.rfind("m"))

# zfill() - fill the string with zeros
# syntex : string.zfill(width)

num = "25"
print(num.zfill(10)) # Output: 0000000025
print(num.zfill(50)) 

# partition() - string ko 3 part me divide karta hai
print("apple-mengo-banana".partition("-")) # Output: ('apple', '-', 'mengo-banana')
# it is return tuple after sepreting the string into 3 parts

# rpartition() - string ko 3 part me divide karta hai from right side
print("apple-mengo-banana".rpartition("-")) # Output: ('apple-mengo', '-', 'banana')

# splitlines() - it is convert multi line string into a list of lines
text = "hello\nMeet\nPython"
print(text.splitlines()) # output : ['hello', 'Meet', 'Python']

# casefold() - lower() se bhi powerful lowercase conversion.
text = "PYTHON"
print("i am from lower: ", text.lower()) # Output: python
print("i am from casefold: ", text.casefold()) # Output: python

# encode() - convert string into bytes
print("Meet".encode()) # Output: b'Meet'
print(type("Meet".encode())) # Output: <class 'bytes'>

# maketrans()  + translate() - for replace the character in string

table  = str.maketrans("abc", "123")
text = "abc cab"
print(text.translate(table  )) # output ; 123 312



num = "87"
print(num.zfill(5))

text = "Python-Java-C++"

print(text.partition("-"))
print(text.rpartition("-"))

text = "A\nB\nC\nD"

print(text.splitlines())

text = "HELLO"

print(text.casefold())
print(text.encode())

table = str.maketrans("xyz", "789")

text = "x y z xyz"

print(text.translate(table))


text = "Python\nJava\nC++"
lines  = text.splitlines()
print("Lines : ", lines)
print("Total Lines : ", len(lines ))










