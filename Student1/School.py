
from Student1.Student import Student


class School:
    student_list={}

    def add(self,id:int,name:str):
        a = Student(id,name)
        if a.grade==[]:
            print("Invalid data")
            return
        self.student_list[a.stuid] = [a.name, a.grade,a.average()]
        print(f"Student is added to School list")


    def remove(self,id):
        count = 0
        if id in self.student_list:
            count = 1
            del self.student_list[id]
        if count == 1:
            print("Successfully removed")
        else:
            print("Not found")

    def search(self,id):
        if id in self.student_list:
            print(f"The id is{id} The student name is {self.student_list[id][0]} The student grade is{self.student_list[id][1]} The student grade is {self.student_list[id][2]}")
        else:
            print("Not found")

    def display1(self):
        if len(self.student_list)!=0:
            for student in self.student_list:
                print(f"The student id is {student} The student name is {self.student_list[student][0]} The student grade is {self.student_list[student][1]} The student grade is {self.student_list[student][2]} ")
        else:
            print(self.student_list)


class AdvancedSchool(School):

    def findaboveavg(self,grade:str):
        count=0
        value=self.findvalue(grade)
        for id in self.student_list:
            if self.findvalue(self.student_list[id][2])>= value:
                count=1
                print(f"The student id is {id}\nThe student name is {self.student_list[id][0]}\nThe student grade is {self.student_list[id][1]}\nThe student grade is {self.student_list[id][2]} ")
        if count==0:
            print("The list is empty")

    def findvalue(self,grade):
        if grade=='F':
            return 1
        elif grade=='D':
            return 2
        elif grade=='C':
            return 3
        elif grade=='B':
            return 4
        elif grade=='A':
            return 5
