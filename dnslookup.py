# Import libraries
import dns.resolver, time

def nslook():
    while True:

        # Finding A record
        site = input("\nInput a domain name or press 'q' to quit: ")
        if site == 'q':
            quit()
        # Query private server
        if site == '40k':
            site = ""
        else:
            site = dns.resolver.resolve(site, 'A')
        
        # Printing record
        for val in site:
            print("\nAccessing The Warp...")
            time.sleep(1)
            print(f'Tzeencht says {val.to_text()}...')

nslook()

