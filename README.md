# Define menu of restaurant
menu = {
   'pizza': 99,
   'pasta': 120,
   'burger': 99,
   'salad': 70,
   'coffee': 80
}

# Greeting
print('Welcome to Kiran Restaurant')
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

# Taking input order from user
order_total = 0

while True:
    item = input("\nEnter the name of the item you want to order: ").lower()
    if item in menu:
        order_total += menu[item]
        print(f"Your item '{item}' has been added to your order.")
    else:
        print(f"Sorry, ordered item '{item}' is not available yet!")

    another_order = input("Do you want to order another item? (yes/no): ").lower()
    if another_order == "no":
        break

print(f"\nThe total amount of items to pay is Rs{order_total}")
print("Thank you for visiting Kiran Restaurant!")
