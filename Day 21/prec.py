# Q1
class Cercle:
    def __init__(self , redius):
        self.redius = redius

    def area(self):
        return 3.14 * self.redius * self.redius

    def perimeter(self):
        return 2 * 3.14 * self.redius

c1 = Cercle(21)
print("Area of Circle is: ", c1.area())
print("perimeter of Circle is", c1.perimeter())

# Q2
class Employ:
    def __init__(self , role , dpt , selery):
        self.role = role
        self.dpt = dpt
        self.selery = selery

    def showDetails(self):
        print("Role : ", self.role)
        print("Department : ", self.dpt)
        print("Selery : ", self.selery)

e1 = Employ("Meneger" , "IT" , "10000")
e1.showDetails()

# Q3
class Order:
    def __init__(self , item , price):
        self.item = item
        self.price = price

    def __gt__(self , ord2):
        return self.price > ord2.price

ord1 = Order("Chips" , 20)
ord2 = Order("Poteto" , 30)
ord3 = Order("Chips" , 10)
print(ord1 > ord2)

print(ord1 > ord3)