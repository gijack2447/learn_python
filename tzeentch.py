"""Tzeentch DNS Query"""

# Import libraries
import dns.resolver, time

class Tzeentch:
    def __init__(self, chaos):
        self.chaos = chaos

    def request(self, chaos):
        self.chaos = chaos
        x = 1
        while x == 1:
            
            if chaos > 10:
                print("\nTzeentch does not like your number...")
                if chaos != 40000:
                    print("Ah!")
                    x = 2
                else:
                    x = 2
            elif chaos <= 10:
                print("\nTzeentch likes the smell of this number...")
                time.sleep(2)
                print("...")
                time.sleep(2)
                x = 2
        
        while x == 2:

            # Finding A record
            site = input("\nQuestion Tzeentch about a domain name: ")
            with open('tzeentch.txt', 'a') as f:
                if site == 'q':
                    quit()
                # Query private server
                if site == '40k':
                    site = ""
                else:
                    dns_site = dns.resolver.resolve(site, 'A')
                    for val in dns_site:
                        f.write(f"\n{site}: {val.to_text()}")
                x = 3
                        
            
            # Printing record with chaos
            for val in dns_site:
                if chaos > 7:
                    print("\nAccessing The Warp...")
                    time.sleep(2)
                    print("\nThe precense of Tzeentch confounds you.")
                    time.sleep(2)
                    print(f'Tzeencht says {val.to_text()}...')
                    

                elif chaos == 7:
                    print("\n...")
                    time.sleep(2)
                    print("\n...7!")
                    x = 3
                elif chaos < 7:
                    print("\nThe number!")
                    time.sleep(2)
                    print("\nInfinite.")
                    time.sleep(1)
                    print(f"\n 'The true IP of this domain name is {val.to_text()},' says Tzeentch!")
                    x = 3
       
    
    def sleep(self, chaos):
      self.chaos = chaos
      
      while True:
        if chaos <= 3:

            x = int(input("How much sleep is enough sleep?"))
            if x <=10:
                print("You are a FOOL!")
                time.sleep(60)
                quit()
            if x > 10:
                print("That's a start!")
                time.sleep(1)
                quit()
            if x > 1000:
                print("\nThe Warp howls!")
                time.sleep(2)
                print("\nThe appearance of Tzeentch blinds you with darkness!")
                time.sleep(3)
                print("\nTzeentch shines in your minds eye...")
                time.sleep(2)
                print("\nTzeentch is pleased!")
                input()
                 
        elif chaos == 7:
            x = int(input("What year? "))
            if x > 40000:
                print("\n'Death to the corpse emperor!', howls Tzeentch.")
                print("\nThe Warp shreds your body into slivers as Tzeentch devours your soul!")
                time.sleep(5)
                quit()
            if x < 40000:
                print("\nYou are snatched into the boosum of Tzeentch!")
                time.sleep(3)
                print("\nYour tomorrows and yesterdays merge into a tapestry of massive, unfolding shapes.")
                time.sleep(2)
                quit()

