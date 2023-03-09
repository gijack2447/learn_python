class Zfighter:
    def __init__(self,name, home, power):
        self.name = name
        self.home = home
        self.power = power

    def list(self):
        print(f"\n{self.name.title()}")
        print(f"Homeworld: {self.home.title()}")
        print(f"Power Level: {self.power}!")

    def describe(self):
        if self.power <= 1000:
            print(f"\nThe humble {self.name.title()}! He is from {self.home.title()}!")
            print(f"He is a hero in his own right...")
        elif self.power > 1000 and self.power < 500000:
            print(f"\n{self.name.title()} the strong! He hails from {self.home.title()}!")
            print(f"There are plenty of stories about his power level of {self.power}!")
        elif self.power >= 500000:
            print(f"\nA tyrant!!! {self.name.title()} of {self.home.title()}!")
            print(f"{self.power}! Let's hope he doesnt show up around here!")

