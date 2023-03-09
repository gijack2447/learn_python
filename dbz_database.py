import time

class Zfighter:
    def __init__(self,name, home, power):
        self.name = name
        self.home = home
        self.power = power

    def describe(self):
        if self.power <= 1000:
            print(f"\nThe humble {self.name.title()}! He is from {self.home.title()}!")
            print(f"\nHe is a hero in his own right...")
        elif self.power > 1000 and self.power < 500000:
            print(f"\n{self.name.title()} the strong! He hails from {self.home.title()}!")
            print(f"There are plenty of stories about his power level of {self.power}!")
        elif self.power >= 500000:
            print(f"\nA tyrant!!! {self.name.title()} of {self.home.title()}!")
            print(f"{self.power}! Let's hope he doesnt show up around here!")

x = 1
while x == 1:


    name = input("\nWhat's this guy's name? ")
    home = input("\nWhere's he from? ")
    power = int(input("\nWhat's his power level? "))
    print("Gotcha! Let me ask around...")
    time.sleep(3)

    fighter = Zfighter(name, home, power)
    fighter.describe()

    x = int(input("\nPress 1 to ask again, press 2 to exit: "))