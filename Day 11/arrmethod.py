# append() - append() method array ke last (end) me ek naya element add karta hai.
# syntex : array.append(value)

# Example :
arr = [10,30,40,50]
arr.append(60)
print(arr)

'''
Visualization :

before 
index : 0   1   2  3   
array : 10  30  40 50

append(60)

after :
index : 0   1   2  3   4
array : 10  30  40 50  60

'''

# Example :
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)


# insert() - insert() method array ke kisi bhi index me ek naya element add karta hai.
# syntex : array.insert(index, value)

# Example
arr = [10,30,40,50]
arr.insert(2,20)
print(arr)

city = ["Surat" , "Rajkot"]
city.insert(1, "Navsari")
print(city)

# extend() - extend() method array ke last (end) me ek dusre array ke elements add karta hai.
# syntex : array1.extend(array2)

# Example:
arr1 = [ 10 , 20]
arr2 = [30 , 40]

arr1.extend(arr2)
print(arr1)

a= [ "A" , "B"]
b = [ "C" , "D"]
a.extend(b)
print(a)

# remove() - remove() method array ke kisi bhi element ko remove karta hai.
# syntex : array.remove(value)
# Note: Agar same value multiple baar ho to sirf first occurrence remove hoti hai.

# Example :
arr = [ 10,20,30,40]
arr.remove(20)
print(arr)

fruits = ["Apple", "Banana", "Apple"]
fruits.remove("Apple")
print(fruits)

# pop() - pop() method array ke last (end) me se ek element remove karta hai.
# syntex : array.pop()
# "Agar index nahi diya jaye to last element remove hota hai."

# Example :
arr = [ 10,20,30,40]
arr.pop()
print(arr)
# if we give index then it will remove that index element
arr.pop(1)
print(arr)

# storing remove element 
x = arr.pop()
print(x)
print(arr)

# sort() - sort() method array ke elements ko ascending order (small to large) me arrange karta hai.
#syntex : array.sort()

arr = [20,30,50,10,40]
arr.sort()
print(arr)

# string sorting example
fruits  = ["Mengo" , "Apple" , "Orange" , "Banana"]
fruits.sort()
print(fruits)

# Descending Order
arr = [20,30,50,10,40]
arr.sort(reverse=True)
print(arr)

# reverse() - reverse() method array ke current order ko ulta kar deta hai.
# syntex : array.reverse()

# Notes : reverse order ko sort nahi karta , only ulta karta he.
arr = [10,20,30,40]
arr.reverse()
print(arr)

# count() - count() method array me kisi bhi element ke occurrence ko count karta hai.
# syntex : arr.count(value)

arr = [10,20,30,10,10,40,10]
x = arr.count(10)
print(x)

fruits = ["Apple","Banana","Apple","Mango"]
print(fruits.count("Apple"))

# index() - index() method kisi value ka first index return karta hai.
# syntex : arr.index(value)

arr = [10,20,30,40]
print( "Index of the element:", arr.index(30))

# copy() - copy() method array ke ek copy create karta hai.
# syntex : arr.copy()
arr = [10,20,30]
new_arr = arr.copy()
print(new_arr)
new_arr.append(40)
print(arr)
print(new_arr)

# clear() - method array ke element ko remove kar deta he .
# syntex : arr.clear()
arr = [10,20,30]
arr.clear()
print(arr)


