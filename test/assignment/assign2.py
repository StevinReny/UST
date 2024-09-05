from abc import ABC, abstractmethod


class Electronic_device(ABC):

    @abstractmethod
    def power_usage(self):
        pass

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model


    def describe(self):
        print(f"The brand is {self.brand}")
        print(f"The model is {self.model}")
        return

    @classmethod
    def from_type(cls,name,brand,model,battery_life,screensize=0):
        if name=="laptop":
            return Laptop(brand,model,battery_life)
        elif name=="smartphone":
            return SmartPhone(brand,model,battery_life,screensize)

class Laptop(Electronic_device):

    def __init__(self,brand,model,battery_life):
        super().__init__(brand,model)
        self.battery_life=battery_life


    def power_usage(self):
        print(f"The power consumption is {self.battery_life*50}")
        return

class SmartPhone(Electronic_device):

    def __init__(self,brand,model,battery_life,screen_size):
        super().__init__(brand,model)
        self.screensize=screen_size
        self.battery_life=battery_life

    def power_usage(self):
        print(f"The screen size is {self.screensize}")
        return print(f"The power consumption is{self.battery_life*10}")


def main():
    try:
        choice=input("Choices are laptop and smartphone")
        if choice=="laptop" or choice=="smartphone":
            brand=input("Enter the brand")
            model=input("Enter the model")
            battery_life=float(input("Enter the battery_life"))
            if choice=="laptop":
                laptop=Electronic_device.from_type(choice,brand,model,battery_life)
                laptop.power_usage()
                laptop.describe()
                #print(laptop.brand)
            elif choice=="smartphone":
                screensize=float(input("Enter the size of screen size in inch"))
                smartphone=Electronic_device.from_type(choice,brand,model,battery_life,screensize)
                smartphone.describe()
                smartphone.power_usage()
        else:
            print("Invalid choice")
    except ValueError:
        print("An error occurred")
        exit()

if __name__=="__main__":
    main()

