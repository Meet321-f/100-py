name = "Meet"
print(name)
print(type(name))

age = 20
print(age)
print(type(age))

hight = 5.3
print(hight)
print(type(hight))

isstudent = True
print(isstudent)
print(type(isstudent))

a = int(input("enter first number: "))
b = int(input("enter second number: "))
sum = a + b
print(sum)

a = int(input("enter your num 1:   "))
b = int(input("enter your num 2:   "))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

age = int(input("enter your age: "))
if age >= 18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")

mark = int(input("enter your mark: "))
if mark >= 90:
    print("A grade")
elif (mark >= 75):
    print("B grade")
elif (mark >= 60):
    print("C grade")
elif (mark >= 40):
    print("P grade")
else:
    print("F grade")            

for i in range(1, 6):
    print(i)

#print 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1