a = int(input("Enter 1st number : "))
if a % 2 == 0:
    print("this is a Even Number.")

else:
    print("This is a odd number.")

a = int(input("Enter 2nd number : "))
b = int(input("Enter 3rd number : "))
c = int(input("Enter 4th number : "))

if a > b and a > c:
    print("1st number is the largest number.")
elif b > a and b > c:
    print("2nd number is the largest number.")
else:
    print("3rd number is the largest number.")


num = int(input("Enter a number : "))

for i  in range(1,11):
    print(num, "x", i, "=", num*i)

# fectorial
num = int(input("Enter a number : "))

factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else :
    for i in range(1,num +1):
        factorial = factorial*i
    print("The factorial of", num, "is", factorial)

# Fibonacci
num = int(input("Enter a number : "))
a = 0
b = 1
print(a, b, end=" ")
for i in range(2, num):
    c = a + b
    print(c, end=" ")
    a = b
    b = c


'''
First element
Last element
Reverse list
Sum
Maximum
'''
nums = [10,20,30,40,50]
print(nums[0])
print(nums[-1])
print(nums[::-1])
print(sum(nums))
print(max(nums))
