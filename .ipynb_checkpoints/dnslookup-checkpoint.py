# Import libraries
import dns.resolver
  
# Finding A record
site = input("Input a domain name: ")
result = dns.resolver.resolve(site, 'A')
  
# Printing record
for val in result:
    print('\nA Record : ', val.to_text())

