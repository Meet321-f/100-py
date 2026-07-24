# Jab hume pata na ho ki kitne arguments aayenge.
from unittest import result


def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 3))
print(multiply(2, 3, 4))
print(multiply(1, 2, 3, 4, 5))

## **kwargs
# *args ka matlab hai ki function ek ya ek se zyada values ek tuple ke form me receive kare.
def profile(**data):
    print(data)
    print("Name : " , data['name'])
    print("Age : " , data['age'])
    
profile(name = "Meet" , age = 21 , city = "Surat")       