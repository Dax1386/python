# concession stand program
menu = {
    "Samosa (2 pcs)": 30.00,
    "Masala Chai": 20.00,
    "Pav Bhaji": 80.00,
    "Vada Pav": 30.00,
    "Paneer Tikka Roll": 100.00,
    "Chicken Frankie": 110.00,
    "Cold Coffee": 60.00,
    "Sweet Lassi": 50.00,
    "Gulab Jamun (2 pcs)": 40.00,
    "Water Bottle": 20.00
}
cart = []
total = 0.0
print("----------------MENU--------------------")
for key, value in menu.items():
    print(f"{key}: ₹{value:.2f}")
print("----------------------------------------")

while True:
    food_item = input("Enter the food item you want to order (or 'done' to finish): ")
    if food_item.lower() == 'done':
        break
    elif food_item in menu is False:
        print("Invalid food item. Please choose from the menu.")
    else:
        cart.append(food_item)

for food_item  in cart:
    total += menu.get(food_item)
    print(food_item , end=", ")
print()
print(f"total is:₹{total:.2f}")