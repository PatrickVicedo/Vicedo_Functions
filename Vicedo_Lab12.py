# Define the main menu with food items and their respective prices
main_menu = {
    'Coke': 30.00,
    'Kare-Kare': 150.00,
    'Sisig': 90.00,
    'Adobo': 80.00,
    'Sinigang': 85.00,
    'Lechon Kawali': 130.00,
    'Pancit': 100.00,
    'Bicol Express': 120.00,
    'Laing': 90.00,
    'Lumpiang Shanghai': 60.00,
    'Puto': 40.00,
    'Banana Cue': 25.00
}

# Define the dessert menu with dessert items and their respective prices
dessert_menu = {
    'Halo-Halo': 50.00,
    'Leche Flan': 45.00,
    'Bibingka': 35.00,
    'Turon': 40.00,
    'Kakanin': 55.00,
    'Suman': 30.00,
    'Manggang Hilaw': 60.00,
    'Ice Cream': 70.00,
    'Taho': 25.00,
    'Coconut Macaroons': 40.00
}

# Display the main menu items with their prices
print("Main Menu:")
for item, price in main_menu.items():
    print(f"{item}: ₱{price:.2f}")

# Display the dessert menu items with their prices
print("\nDessert Menu:")
for item, price in dessert_menu.items():
    print(f"{item}: ₱{price:.2f}")

# Initialize the total cost variable to track the total price of the order
total_cost = 0

# Start a loop to allow users to order items
while True:
    # Ask the user to input their choice of food or type 'stop' to finish
    choice = input("Please enter the food item you'd like to order (or type 'stop' to finish): ").strip()

    # Check if the user wants to stop ordering
    if choice.lower() == 'stop':
        break
    # Check if the chosen item is in the main menu
    elif choice in main_menu:
        item_price = main_menu[choice]  # Get the price of the item
        total_cost += item_price  # Add the item price to the total cost
        print(f"You added {choice} to your order. Current total: ₱{total_cost:.2f}")
    # Check if the chosen item is in the dessert menu
    elif choice in dessert_menu:
        item_price = dessert_menu[choice]  # Get the price of the item
        total_cost += item_price  # Add the item price to the total cost
        print(f"You added {choice} to your order. Current total: ₱{total_cost:.2f}")
    # If the item is not in either menu, inform the user
    else:
        print("Invalid item. Please select a valid item from the menu.")

# Print the total cost of the order once the user is done
print(f"Your total order cost is ₱{total_cost:.2f}.")

# Start a loop to handle payment from the user
while True:
    # Prompt the user to enter their payment amount
    payment = input(f"Please enter your payment: ₱")
    
    # Check if the input is a valid number
    if payment.replace('.', '', 1).isdigit():
        payment = float(payment)  # Convert the input to a float
        # Check if the payment is less than the total cost
        if payment < total_cost:
            print("Insufficient payment. Please provide more money.")
        else:
            # Calculate the change and inform the user
            change = payment - total_cost
            print(f"Payment accepted. Your change is ₱{change:.2f}.")
            break
    else:
        # Inform the user if they entered an invalid amount
        print("Invalid input. Please enter a valid amount of money.")

