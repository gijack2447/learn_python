"""Add to a list of bicycles kept as a list in bicycles.txt"""

def bicycle_list():
    
    #with open('bicycles.txt', 'a') as f:
        #data = f.read()
        #data_into_list = data.split("\n")
      
    while True:
        bike_list = open("bicycles.txt", "a")
        data = bike_list.read()
        data_into_list = data.split("\n")

        bike = input("\nAdd a bicycle to the list, enter 'q' to quit: ")

        if bike.title() in data_into_list:
            print("\nThat bike already exists!")
            True
        
        elif bike == 'q':
            quit()
        
        else:
            print(f"\nA new bike! A {bike.title()}!")

            data_into_list.append(bike.title())

            print("\nCurrent inventory: ")
            for bicycle in data_into_list:
                
                print(bicycle)

            f.write(bike.title() + '\n')
            

bicycle_list()


# Access the last elements in a list with [-1], or further (ex: [-2])
                        