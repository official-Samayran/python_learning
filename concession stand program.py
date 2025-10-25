menu = {"Pizza": 2.30,
        "Samosa": 3.40,
        "Popcorn": 6.20,
        "Coke": 2.56,
        "Fries": 3.30,}

cart = []
total = 0

print("-----------MENU-----------")
for key, value in menu.items():
    print(f"{key:18} : ${value:.2f}")
print("--------------------------")

while True:
    food = input("Enter the item name (Q to Quit): ").capitalize()
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("-----------CART-----------")
for food in cart:
    total += menu.get(food)
    print(f"{food:18} : ${menu.get(food):.2f}")
    
print()    
print(f"TOTAL- ${total:.2f}")
print("--------------------------")

