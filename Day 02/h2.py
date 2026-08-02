'''
Even/Odd Number
Largest of 3 Numbers
Multiplication Table
Factorial
Fibonacci Series
'''

#1st even or odd
a = int(input("enter your number: "))
if a % 2 == 0:
    print("even number")
else:
    print("odd number")

# 2nd largest of 3 numbers
a = int(input("enter your num 1:   "))
b = int(input("enter your num 2:   "))
c = int(input("enter your num 3:   "))
if a > b and a > c:
    print('a is larger')
elif b > a and b > c:
    print('b is larger')
else:
    print('c is larger')         

#3rd multiplication table  
num = int(input("enter your number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i) 

#4th factorial
num = int(input("enter your number: "))
if num < 0:
    print("factorial does not exist for negative numbers")
elif num == 0:
    print("factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("factorial of", num, "is", factorial)         

#5th fibonacci series
n = int(input("enter the number of terms: "))
n1 ,n2 = 0,1
print("Fibonacci sequence up to", n, "terms:")   
for i in range(n):
        print(n1, end=' ')
        n1, n2 = n2, n1 + n2

