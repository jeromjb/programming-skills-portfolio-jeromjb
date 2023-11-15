'''Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 

occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.'''



sandwich_orders = ["Chicken","Pastrami","Mutton","Pastrami","Beef","Veg","Pastrami",
                   "Combo","Club"]
finished_sandwiches = []
print ("The deli has run out of Pastrami")
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print (f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print ("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print ("Pastrami")