# dictionary

# A dictionary is a storing value in a key-value pair.
#  it is like a id card

'''
 key           Value
 name          Meet
 age          20
 city          Surat
 '''

# In Python
student = {
 "name" : "Meet",
 "age" : 20 ,
 "city" : "navsari"
}
print(student)
# Accesing Value
print("Student Name : " , student["name"])
print("Student Age : " , student["age"])

# using get()
print("Student City : ", student.get("city"))

# Adding New Data
student["class"] = "2nd year B.tech"
print(student)

# Updating Data
student["city"] = "Mumbai"
print(student)

# Removing Data using pop()
student.pop("class")
print(student)

# Dictionary Methods [ key and value]
print(student.keys())
print(student.values())

# items()
print(student.items())

# Loop Through Dictionary
# Print only keys
for key in student:
    print(key)

# Print only values
for value in student.values(): 
    print(value)

# Print both
for key , value in student.items():
    print(key , " : " , value)    

# Membership
# check if a key exist
print( "name" in student)
print( "selery" in student)

# Nested Dictionary
student = {
    "s1" : {
        "name" : "Meet",
        "age" : 20
    },
    "s2" : {
        "name" : "Meet",
        "age" : 20
    }
}
print(student["s1"]["name"])

# practice
car = {
    "brand": "Toyota",
    "model": "Fortuner",
    "year": 2023
}

print("Car Brand : " , car["brand"])
print("Car Model: " , car["model"]  )

#addition
car["color"] = "Black"
print(car)

# update
car["year"] = 2025
print(car)

# remove
car.pop("model")
print(car)

for key in car:
    print(key)

for value in car.values():
    print(value)    

for key, value in car.items():
    print(key, ":", value)
