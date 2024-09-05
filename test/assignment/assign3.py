from abc import ABC, abstractmethod
from random import choice


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    def __init__(self,name):
        self.name=name

    def describe(self):
        print(self.name)
       # print(type(self).__name__)
        print(self.__class__.__name__)
        return

class FullTimeEmployee(Employee):

    def __init__(self,name):
        super().__init__(name)

    def calculate_salary(self):
        return print(f"The salary of {self.name} as {type(self).__name__} is 3000$")


class PartTimeEmployee(Employee):
    def __init__(self,name,hrs,rate):
        super().__init__(name)
        self.rate=rate
        self.hrs=hrs
    def calculate_salary(self):
        return print(f"The salary of {self.name}as {self.__class__.__name__}is {self.rate*self.hrs}")

def main():
    print("1:FullTime\n 2:PartTime")
    try:
        choice = int(input("Enter the choice "))
        if choice ==1:
            name=input("Enter the name of employee")
            femployee=FullTimeEmployee(name)
            femployee.calculate_salary()
            femployee.describe()
        elif choice==2:
            name=input("Enter the name of emploeyee")
            hrs=float(input("Enter the hrs worked"))
            rate=float(input("Enter the rate per hr"))
            pemployee=PartTimeEmployee(name,hrs,rate)
            pemployee.describe()
            pemployee.calculate_salary()
        else:
            print("Invalid")
            exit()
    except ValueError:
        print("An error occurred")


if __name__=="__main__":
    main()








