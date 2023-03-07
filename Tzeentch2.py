from tzeentch import Tzeentch

chaos = int(input("Offer a number to Tzeentch:         "))
new_number = Tzeentch(chaos)
new_number.request(chaos)
new_number.sleep(chaos)

