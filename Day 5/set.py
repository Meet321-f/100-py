# sets
# a sets stored only unique value




num = { 1 , 2 , 3}
print(num)

# Duplicates are remove autometically.
t = { 1 , 2 , 3 , 2 , 1 , 4 , 2}
print(t)

# Adding value and Removing values and if value not exist then it will give error

s = {1,2,3}
s.add(4)
print("Adding Value : " , s)
s.remove(2)
print("Removing Value : " , s)
# safe way
s.discard(10) # it will not give error if value not exist
print ("Discard Value : " , s)

# set opretion

A={10,20,30,40}
B={30,40,50,60}

# Union
print("Union : " ,A | B)

#Intersection
print("Intersection : " , A & B)

# Difference
print("Difference : " , A - B)

# Symmetric Difference
print("Symmetric Difference : " , A ^ B)

student = {"name" : "Meet" }
student["city"] = "Surat"
print(student)