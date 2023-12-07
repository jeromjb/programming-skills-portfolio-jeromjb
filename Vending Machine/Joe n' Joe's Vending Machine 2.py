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

balance = 0.0

def insert_money (items):
    while True:
        try:
            amount = float(input("Insert money or press 0 to cancel"))
            if amount == 0:
                print ("Transaction cancelled. Returning to main menu.")
                break
            elif amount < 0:
                print ("Invalind amount. PLease insert a valid amount")
            else:
                balance += amount
                print (f"Current balance: {balance:.2f}")
                break
        except ValueError:
            print ("Invalid input. Please enter a valid amount")
            