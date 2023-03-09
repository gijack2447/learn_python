# Initiate a list 'bicycles'
bicycles = []

def bicycle_list():
        
    while True:

        bike = input("\nAdd a bicycle to the list, enter 'q' to quit: ")

        if bike.title() in bicycles:
            print("\nThat bike already exists!")
            True
        
        elif bike == 'q':
            quit()
        
        else:
            print(f"\nA new bike! A {bike.title()}!")

            bicycles.append(bike.title())

            print("\nCurrent inventory: ")
            for bicycle in bicycles:
                
                print(bicycle)

        f = open('bicycles.txt', 'a')
        f.write(bike.title() + '\n')
            

bicycle_list()


# Access the last elements in a list with [-1], or further (ex: [-2])
                        