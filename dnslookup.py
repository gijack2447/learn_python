# Import libraries
import dns.resolver
  
# Finding A record
result = dns.resolver.query('bellevue.edu', 'A')
  
# Printing record
for val in result:
    print('\nA Record : ', val.to_text())

