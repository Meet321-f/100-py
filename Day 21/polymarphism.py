# # polymorphisum : Opretor overloading

# class Complex:
#     def __init__(self , real , img):
#         self.real = real
#         self.img = img

#     def shownum(self):
#         print(self.real,"i +",self.img, "j")

# # dandar function :
#     def __add__(self , num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal , newImg)

#     def __sub__(self , num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal , newImg)
# num1 = Complex(3, 4)
# num2 = Complex(-2 , 3)
# num4 = Complex(5, -6)
# num1.shownum()
# num2.shownum()
# num4.shownum()

# # add two value
# num3 = num1 + num2
# num3.shownum()

# # sybtrect value
# num5 = num1 - num4
# num5.shownum()


