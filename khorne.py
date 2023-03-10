"""Khorne"""

capitals = {
            "USA":"Washington DC",
            "India":"New Delhi",
            
            }

print(capitals.get("USA"))

capitals.update({"India":"Kandahar"})

keys = capitals.keys()
for key in capitals.keys():
    print(key)




