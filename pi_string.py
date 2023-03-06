filename = 'text_files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

while True:
    birthday = input("Enter your birthday (mmddyy): ")
    if birthday in pi_string:
        print("\nYour birthday appears in the first million digits of pi!")
    
    else:
        print("\nYour birthday doesnt appear in the first million digits of pi.")
    