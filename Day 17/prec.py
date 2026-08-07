class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def get_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", s1.name , "Your Avg  Score is: ", sum/3)    

s1 = Student("Meet" , [85, 90, 95])
s1.get_marks()

