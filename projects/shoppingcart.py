#shopping cart for food 
foods = []
prices = []
total = 0
while True:
    food = input("Enter the food item (or 'done' to finish): ")
    if food.lower() == 'done':
        break
    else:
        price = float(input(f"Enter the price for {food}: "))
    foods.append(food)
    prices.append(price)

print("------ Shopping Cart ---")

for food in (foods):
    print(food , end=", ")
print()
for price in (prices):
    print(f"₹{price:.2f}")
    total += price

print(f"Total: ₹{total:.2f}")
print("Thank you for shopping with us!")
          
