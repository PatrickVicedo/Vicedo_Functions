
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

print("Main Menu:")
for item, price in main_menu.items():
    print(f"{item}: ₱{price:.2f}")

print("\nDessert Menu:")
for item, price in dessert_menu.items():
    print(f"{item}: ₱{price:.2f}")

total_cost = 0

while True:
    choice = input("Please enter the food item you'd like to order (or type 'stop' to finish): ").strip()

    if choice.lower() == 'stop':
        break
    elif choice in main_menu:
        item_price = main_menu[choice]
        total_cost += item_price
        print(f"You added {choice} to your order. Current total: ₱{total_cost:.2f}")
    elif choice in dessert_menu:
        item_price = dessert_menu[choice]
        total_cost += item_price
        print(f"You added {choice} to your order. Current total: ₱{total_cost:.2f}")
    else:
        print("Invalid item. Please select a valid item from the menu.")

print(f"Your total order cost is ₱{total_cost:.2f}.")

while True:
    payment = input(f"Please enter your payment: ₱")
    
    if payment.replace('.', '', 1).isdigit():
        payment = float(payment)
        if payment < total_cost:
            print("Insufficient payment. Please provide more money.")
        else:
            change = payment - total_cost
            print(f"Payment accepted. Your change is ₱{change:.2f}.")
            break
    else:
        print("Invalid input. Please enter a valid amount of money.")
