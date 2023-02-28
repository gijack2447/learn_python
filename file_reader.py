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