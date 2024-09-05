from abc import ABC,abstractmethod


class Vehicle(ABC):
    def __init__(self,wheels,colour):
        print("Hi")
        self.wheels=wheels
        self.colour=colour


    @abstractmethod
    def get_fuel_efficiency(self):
        pass

    @classmethod
    def from_name(cls,name,wheel,colour):
        if name=="car":
            print("Hai")
            return Car(wheel,colour)
        elif name=="truck":
            return Truck(wheel,colour)

    def description(self):
        print(f"The description is{self.wheels,self.colour}")
        return type(self).__name__


class Car(Vehicle):
    def get_fuel_efficiency(self):
        return print("A fuel efficiency of 25 miles per gallon")

class Truck(Vehicle):
    def get_fuel_efficiency(self):
        return "A fuel efficiency of 15 miles per gallon"

def main():
    while True:
        print("Choices are (Car,Truck)")
        choice=input("Enter the choice ")
        wheel=input("Enter the no of wheel")
        colour=input("Enter the colour")
        if choice.lower()=="car":
            car=Vehicle.from_name(choice,wheel,colour)
            car.description()
            car.get_fuel_efficiency()
        elif choice.lower()=="truck":
            truck=Vehicle.from_name(choice,wheel, colour)
            truck.get_fuel_efficiency()
            truck.description()
        else:
            exit()

if __name__=="__main__":
    main()
