

import time, random

class Text_to:
    def __init__main(self, name, power):
        self.name = name
        self.power = power
    
    def vibe_check(self, name, power):
        self.name = name
        self.power = power
        scrawnies = ['weak','fragile','hollow']
        bigs =['buff', 'strong', 'mighty']
        scrawny = random.choice(scrawnies)

        if power < 1000000:
            print(f"\n{name.title()}! A suckling!")
            time.sleep(1) 
            print(f"\n{name.title()} the {scrawny}!")
            time.sleep(1)
            print("\nAhahahahahahhahhahaaaaaa!")
            time.sleep(2)
            print("\nVery well then")
        elif power >= 1000000:
            print(f"{name.title()}!")
            time.sleep(2)
            print(f"{name.title()} the {random.choice(bigs).title()}! ")
            time.sleep(4)
            print(f"Did you hear it, oh {random.choice(bigs)} {name.title()}? The angels rejoice about how {random.choice(bigs)} you are!\n")




name = input("What is your name, creature? ")
power = int(input("And what is your power? "))

tzeentch = Text_to()
tzeentch.vibe_check(name, power)