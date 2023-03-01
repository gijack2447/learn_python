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