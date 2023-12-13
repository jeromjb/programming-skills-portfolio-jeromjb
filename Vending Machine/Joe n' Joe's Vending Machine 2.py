print ('''__      __   _                    _            _                 _      _          _    
\ \    / /__| |__ ___ _ __  ___  | |_ ___   _ | |___  ___   _ _ ( )  _ | |___  ___( )___
 \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ _ \ | || / _ \/ -_) | ' \|/  | || / _ \/ -_)/(_-<
  \_/\_/\___|_\__\___/_|_|_\___|  \__\___/  \__/\___/\___| |_||_|    \__/\___/\___| /__/''')

items = {
    'item1': {
        'category': 'Milk & Bevs',
        'name': 'Brownie Drowns',
        'code': 101,
        'price': 15.00,
        'stock': 12
    },
    'item2': {
        'category': 'Snacks',
        'name': 'Larabar',
        'code': 102,
        'price': 10,
        'stock': 20
    },
    'item3': {
        'category': 'Drinks',
        'name': 'Mango Punch',
        'code': 103,
        'price': 13,
        'stock': 15
    },
    
    
}

print("Category:", items['item1']['category'])
print("Name:", items['item1']['name'])
print("Code:", items['item1']['code'])
print("Price:", items['item1']['price'])
print("Stock:", items['item1']['stock'])

print("Category:", items['item2']['category'])
print("Name:", items['item2']['name'])
print("Code:", items['item2']['code'])
print("Price:", items['item2']['price'])
print("Stock:", items['item2']['stock']) 

print("Category:", items['item3']['category'])
print("Name:", items['item3']['name'])
print("Code:", items['item3']['code'])
print("Price:", items['item3']['price'])
print("Stock:", items['item3']['stock']) 



print("Please select an item:")
for key, item in items.items():
    print(f"{key}. {item['name']} - Dhs {item['price']}")

choice = input("Enter the item no. you wish for...")

if choice in items:
    choice_item = items [choice]
    print ("Your item is {choice_item['name']}.")
    amount = choice_item['price']

    while amount > 0:
        try:
            payment = float(input(f"Please insert Dhs {amount:.2f}: "))
            if payment >= amount:
                balance = payment - amount
                print(f"Thank you for purchasing! Your balance is ${balance:.2f}.")
                break
            else:
                print("Insufficient payment. Please insert more money.")
                amount -= payment
        except ValueError:
            print("Invalid payment amount. Please enter a valid number.")
else:
    print("Invalid selection. Please try again.")


