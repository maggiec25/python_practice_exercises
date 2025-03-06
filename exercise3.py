groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]
print(groceries)

def remove_groceries():
    while True:
        item = input("Which item would you like to remove?")
        if item == "cheez its":
            groceries.remove("cheez its")
            print(groceries)
        if item == "nerds gummy clusters":
            groceries.remove("nerds gummy clusters")
            print(groceries)
        if item == "doritos":
            groceries.remove("doritos")
            print(groceries)
        if item == "cocoa puffs":
            groceries.remove("doritos")
            print(groceries)
        if item == "pepsi": 
            groceries.remove("pepsi")
            print(groceries)
        if item == "dr. pepper":
            groceries.remove("dr. pepper")
            print(groceries)
        if item == "mountain dew":
            groceries.remove("mountain dew")
            print(groceries)
        if item == "stop":
            break 
        
remove_groceries()