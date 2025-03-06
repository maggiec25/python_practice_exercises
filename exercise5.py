menu = { "Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

def menu_add(item, price):
    menu[item] = price

menu_add(item = "Hot Dog", price = 2)

print(menu)