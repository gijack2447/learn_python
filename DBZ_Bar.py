# import class from file
from dbz_database import Zfighter
import time

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