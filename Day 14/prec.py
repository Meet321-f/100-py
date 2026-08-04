# First we make a file practice.txt and write some data in it. Then we read the data from the file and replace the word "Java" with "Python" and write the new data back to the file.

with open("practice.txt", "w") as f:
    f.write("Hi everyone, \n We are learning File I/O.")
    f.write("\nuseing Java.\nI like programming in Java.")

# only read data in the file 
with open("practice.txt", "r") as f:
    data = f.read()

# replace the word "Java" with "Python"
new_data = data.replace("Java", "Python")
print(new_data)

# overwrite the file with new data
with open("practice.txt", "w") as f:
    f.write(new_data)

word = "learning"      # This word is present in the file, thet the output will be "Found"
with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")    
        
word = "Java"       # This word is not  present in the file, thet the output will be "Not Found"
with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not Found") 

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(f"Found in line {line_no}")
                return
            line_no += 1    

        return -1    
print(check_for_line())
# if word id exist in the file then it will return the line no of the word
# if word is not exist in the file then it will return -1
    
with open('practice.txt', 'r') as f:
    data = f.read()
    print(data)
    print(type(data))

    num = ""

    for i in range(len(data)):
        if data[i] == ',':
            print(int(num)) 
            num = ""
            
        else :
            num += data[i]    

count = 0
with open('practice.txt', 'r') as f:
    data = f.read()
    print(data)
    num= data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
           count += 1
print(count)
