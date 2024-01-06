"""Add to a list of bicycles kept as a list in bicycles.txt"""

def bicycle_list():
    
    #with open('bicycles.txt', 'a') as f:
        #data = f.read()
        #data_into_list = data.split("\n")
      
    while True:
        
        bike_list = open("bicycles.txt", "r+")
        data = bike_list.read()
        data_into_list = data.split("\n")
        print("\nCurrent inventory: ")
        print(data)

        bike = input("\nAdd a bicycle to the list, 'p' to print list, or 'q' to quit: ")
    # Omit content that already exists in list
        if bike.title() in data_into_list:
            print("\nThat bike already exists!")
            True
        elif bike == 'p':
            print(data_into_list)
        elif bike == 'q':
            quit()
        
        else:
            print(f"\nA new bike! A {bike.title()}!")
            data_into_list.append(bike.title())
            bike_list.write(bike.title() + '\n')
            
def remembrancer():

    sons_list = open('text_files/20_primarchs.txt', 'r+')
    data = sons_list.read()
    data_list = data.split('\n')
    while True:
        primc = input("Name a Primarch: ")
        if primc.title() in data_list:
            print("Got it...")
        if primc == 'q':
            quit()
        else:
            f = f"primc + '\n'"
            data_list.append(f)
            sons_list.write(f)
        


    # print(data_list)
    # open text file 

            
            

remembrancer()

# Access the last elements in a list with [-1], or further (ex: [-2])
                        