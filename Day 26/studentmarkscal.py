name = input("Enter Your Name : ")

subjects = int(input("Enter Number of Subjects : "))

print(f"Student Name:{name}")
print(f"Number of Subjects:{subjects}")

marks_list = []

for i in range(subjects):
    subject_name = input(f"Enter Your Subject { i +1} Name : ")
    marks = float(input(f"Enter {subject_name} Marks : "))

    marks_list.append((marks))
    print(f"{subject_name} : {marks}")

total = sum(marks_list)
pr = total / (subjects * 100) *100

print(f"Total Marks : {total}")
print(f"Percentage : {pr}%")

if pr >= 90:
    grade = "A+"
elif pr >= 80:
    grade = "A"
elif pr >= 70:
    grade = "B"
elif pr >= 60:
    grade = "C"
elif pr >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Grade : {grade}")