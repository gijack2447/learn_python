import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

def greet_user():
    """Greet user by name"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()