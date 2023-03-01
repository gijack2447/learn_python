filename = 'text_files/guest.txt'
text = input("Please enter your name: ")

with open(filename, 'w') as file_object:
    file_object.write(text)

z = True
while z == True:
    guests = input("Enter your name (or press q to quit): ")
    if guests == 'q':
        quit()
    else:
        print(f"Welcome {guests}! Your name has been added to the guest book!")
    
        with open('text_files/guest_book.txt', 'a') as file_object:
            file_object.write(f"{guests}\n")
    
 