# File Hending
# what is File Handilng ?
#  A file use to data store paermanently.


import os


'''
Examples:

notes.txt
students.csv
data.json
image.png

'''

# Opening file Syntex ;
# file = open(filename.txt , "mode")

# for fike writing "w"
file = open("demo.txt", "w")
file.write("Hello\nWelcome to Python")
file.close()


# for file reading use "r"
f = open("demo.txt", "r")
print(f.read())
f.close()

# file Reading line by line  use "readline"
file = open("demo.txt", "r")
line1 = file.readline()
print(line1)
line2 = file.readline()
print(line2)
file.close()

file = open("demo.txt", "w")
file.write("Hello\nWelcome to Python\nThis is file handling")
file.close()


f = open("demo.txt", "r+")      # in the "r+" mode the file is overwrite the content of the file.
f.write("Additional content")
print(f.read())
f.close()

# with syntex : with open(filename.txt" , "r") as file:
with open("demo.txt","w") as f:
    data = f.write("new data")
    print(data) 

with open("demo.txt", "r") as f:    # "with" can autometically close the file.
    data = f.read()     
    print(data)


# Deleting file useing the modul "os".
os.remove("demo.txt")   # this will delete the file from the directory.
