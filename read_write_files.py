"""Manipulating files"""

import json


def finch():
    filename = 'text_files/programming.txt'

    # 'w', write mode, writes new text to file
    with open(filename, 'w') as file_object:
        file_object.write("I love programming!\n")
        file_object.write("I love creating new games!\n")

    with open(filename) as file_object:
        contents = file_object.read()
        print(contents)

    # 'a', append mode, allows adding text without overwriting
    with open(filename, 'a') as file_object:
        file_object.write("I also love finding meaning!\n")
        file_object.write("And suffering, of course!\n")

    with open(filename) as file_object:
        contents = file_object.read()
        print(contents)


def show():
    filename = "text_files/learning_python.txt"
    with open(filename) as file_object:
        for i in range(4):
            contents = file_object.read()
            print(contents.strip())

    with open(filename) as file_object:
        for line in file_object:
            print(line.strip())
    print()

    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            print(line.strip())

    print()
    with open(filename) as file_object:
        lines = file_object.read()
        print(lines.replace('Python', 'C'))


def pi():
    with open('text_files/pi_digits.txt') as file_object:
        contents = file_object.read()
    print(contents)

    # Put file path in a variable for cleaner code
    filename = 'text_files/pi_digits.txt'
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())
    # rstrip() strips whitespace to the right of lines

    """Making a List of Lines from a File"""
    with open(filename) as file_object:
        lines = file_object.readlines()
        # readlines() takes each line from file and stores in a list (lines)
    for line in lines:
        print(line.rstrip())


def ghoul():
    username = input("What is your name?")

    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We see you, {username}!")

def fresh():
    filename = input("Please input a name for your file: ")
    name = input("Please input your name: ")
    address = input("Please input your street address: ")
    phone_number = input("Please input your phone number: ")

    with open(filename, 'w') as f:
        f.write(f"{name.title()}, {address.title()}, {phone_number}")

    with open(filename, 'r') as f:
        contents = f.read()
        print(contents)

def pi_game():
    
    """Birthday in the first million digits of pi"""

    filename = 'text_files/pi_million_digits.txt'

    with open(filename) as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    while True:

        birthday = input("\nEnter your birthday (mmddyy): ")
        if birthday in pi_string:
            print("\nYour birthday appears in the first million digits of pi!")
        
        else:
            print("\nYour birthday doesnt appear in the first million digits of pi.")
    
