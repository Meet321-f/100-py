#Default Parameters
#Kabhi-kabhi hum chahte hain ki agar user value na de, to function khud ek default value use kare.

#example
def greet(name='Guest'):
    print("hello", name)
greet()
greet("Meet")     # Yahan "Guest" default parameter hai.

#multiple default parameter
def student(name, city = "surat"):
    print("my Name" ,name)
    print("from" ,city)

student("Meet")
student("Fenil" , "Bilimora")

#cal
def cal(a , b = 20):
    print(a + b)
cal(10)  # Yahan b ka default value 20 hai.
cal(10 , 30)  # Yahan b ka value 30 hai, default value override ho gaya.    

#power and cube
def power(num , p = 2):
    print(num ** p)
power(5)  # Yahan p ka default value 2 hai.
power(5 , 3)  # Yahan p ka value 3 hai, default value override ho gaya.

#bill(price, gst=18) → final price return karo.
def bill(price, gst=18):
    final_price = price + (price * gst/100)
    return final_price
result = bill(1000)
print(result)  # Yahan gst ka default value 18 hai.
result = bill(1000, 5)
print(result)  # Yahan gst ka value 5 hai, default value override ho gaya.
