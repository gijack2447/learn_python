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
