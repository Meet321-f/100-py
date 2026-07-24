#keyword Arguments
#Ab tak hum arguments position ke hisaab se dete the.

#Keyword Arguments
#example
def student(name , age):
    print(name)
    print(age)
student("Meet" , 21)  #Yahan position ke hisaab se arguments diye gaye.    

# Hum parameter ka naam likhkar bhi value de sakte hain.
def student(name , age):
    print("Name :" ,  name)
    print("Age : " , age)
student(age = 21 , name = "Meet")  #Yahan keyword arguments diye gaye.    

#mix agrs
def student( name , city):
    print(name , city)

student("Fenil" , city = "Navsari") #Yahan position aur keyword arguments mix kiye gaye.

def employee(id, name, salary):
    print("ID :" , id)
    print("Name :" , name)
    print("Salary :" , salary)

employee( salary = 50000 ,id = 101 , name = "Vansg")

def book(title, author, price):
    print(title , author , price)

book(title = "Python Programming" , price = 500 , author = "John Doe")

#ko positional + keyword mix karke call karo.
def order(item, qty, price):
    print("Item :" , item)
    print("Quantity :" , qty)
    print("Price :" , price)

order("Laptop" , qty = 2 , price = 50000)

def movie(name, year, rating):
    print("Movie Name :" , name)
    print("Year :" , year)
    print("Rating :" , rating)

movie("python sed story" , 2013 ,  4.5)

movie(rating = 4.3 , name = "KGF 3" , year = 2026)