filename = input("Please input a name for your file: ")
name = input("Please input your name: ")
address = input("Please input your street address: ")
phone_number = input("Please input your phone number: ")

with open(filename, 'w') as f:
    f.write(f"{name.title()}, {address.title()}, {phone_number}")

with open(filename, 'r') as f:
    contents = f.read()
    print(contents)

