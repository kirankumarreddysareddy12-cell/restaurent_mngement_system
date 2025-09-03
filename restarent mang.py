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

order_total = 0

# First order
item_1 = input("\nEnter the name of the item you want to order: ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Sorry, ordered item '{item_1}' is not available yet!")

# Asking if user wants another order
another_order = input("Do you want to order another item? (yes/no): ").lower()

if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added to your order.")
    else:
        print(f"Sorry, ordered item '{item_2}' is not available yet!")

print(f"\nThe total amount of items to pay is Rs{order_total}")
print("Thank you for visiting Kiran Restaurant!")
