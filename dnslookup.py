# Import libraries
import dns.resolver, time

def nslook():
    while True:

        # Finding A record
        site = input("\nInput a domain name or press 'q' to quit: ")
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
            print("\nAccessing The Warp...")
            time.sleep(1)
            print(f'Tzeencht says {val.to_text()}...')

nslook()

