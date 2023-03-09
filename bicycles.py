def bicycle_list():
    # Initiate a list 'bicycles'
    bicycles = []
    
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

            for bicycle in bicycles:
                print("\nCurrent inventory: ")
                print(bicycle)

        with open('bicycles.txt', 'a') as f:
            f.write(bike.title().rstrip())
            True
            

bicycle_list()


# Access the last elements in a list with [-1], or further (ex: [-2])
                        