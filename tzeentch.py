"""Tzeentch DNS Query"""

# Import libraries
import dns.resolver, time

class Tzeentch:
    def __init__(self, chaos):
        self.chaos = chaos

    def nslook(self, chaos):
        self.chaos = chaos
        x = 1
        while x == 1:
            
            if chaos > 10:
                print("\nTzeentch does not like your number...")
                x = 1
            elif chaos <= 10:
                print("\nTzeentch likes the smell of this number...")
                time.sleep(2)
                print("...")
                time.sleep(2)
                x = 2
        
        while True:

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
            
            # Printing record
            for val in dns_site:
                if chaos > 7:
                    print("\nAccessing The Warp...")
                    print("\nThe tendrils of lesser demons swirl around you.")
                    time.sleep(2)
                    print(f'Tzeencht says {val.to_text()}...')
                elif chaos == 7:
                    print("\n...")
                    time.sleep(2)
                    print("\n...7!")
                elif chaos < 7:
                    print("\nDelicious number...")
                    time.sleep(2)
                    print("\nThe angles, the corners, the spheres...")
                    time.sleep(1)
                    print(f"\n 'The true IP of this domain name is {val.to_text()},' says Tzeentch!")
                    quit()
