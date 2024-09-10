

class Student:
    def __init__(self,stuid,name):
        self.stuid=stuid
        self.name=name
        self.grade=Student.addgrade(self)


    def addgrade(self):
        grade=[]
        for i in range(3):
            mark=int(input(f"Enter the grade{i+1} between 1 and 100"))
            if 1 <= mark <= 100:
                grade.append(mark)
            else:
                return []
        return grade

    def average(self):
        if self.grade==[]:
            return None
        avg= sum(self.grade)/len(self.grade)
        if avg>=90:
            grade='A'
        elif avg>=80:
            grade='B'
        elif avg>=70:
            grade='C'
        elif avg>=60:
            grade='D'
        else:
            grade='F'
        return grade

    def display(self):
        print(f"The student id is {self.stuid}\nThe student name is {self.name}\nThe student grade is {self.grade}\n The student grade is {self.average()}")
