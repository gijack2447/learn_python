

import time, random

scrawnies = ['weak','fragile','hollow', 'weak-minded','lifeless']
bigs =['buff', 'strong', 'mighty', 'hardy', 'steadfast', 'miraculous']

class Text_to:
    def __init__main(self, name, power):
        self.name = name
        self.power = power
    
    def vibe_check(self, name, power):
        self.name = name
        self.power = power
        
        

        if power < 1000000:
            print(f"\n{name.title()}! The {random.choice(scrawnies)}!")
            time.sleep(1) 
            print(f"\n{name.title()} the {random.choice(scrawnies)}!")
            time.sleep(1)
            print("\nAhahahahahahhahhahaaaaaa!")
            time.sleep(2)
            print("\nVery well then...")
        if power >= 1000000:
            print(f"{name.title()}!")
            time.sleep(2)
            print(f"{name.title()} the {random.choice(bigs).title()}! ")
            time.sleep(4)
            print(f"\nThe demons of Khorne {random.choice(bigs)} {name.title()}? The angels rejoice about how {random.choice(bigs)} you are!\n")
        
        khorne = open('text_files/list_of_Khorne', 'r+')
        if power >= 1000000:
            khorne.write(f"\n{name.title()} the {random.choice(bigs).title()}")
            khorne.write(f"The library of Khorne recognizes the {random.choice(bigs)} of {name.title()}!\n")

        if power < 1000000:
            khorne.write(f"\nThe library of Khorne cares not for the {random.choice(scrawnies)} {name.title()}!\n")

    






name = input("What is your name, creature? ")
power = int(input("And what is your power? "))

tzeentch = Text_to()
tzeentch.vibe_check(name, power)