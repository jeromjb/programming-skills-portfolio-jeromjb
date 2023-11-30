#1 - Write a program where you can take 5 numbers as an input from user and print their
#sum, average
#2 - Write a program in which you can display list of your 5 favourite things and display the list
#3 - Create a Nested dictionary to store the item category, item name, item code, price,
#andstockAnd display the list of items using function


#1
no1 = int(input("Enter your number"))
no2 = int(input("Enter your number"))
no3 = int(input("Enter your number"))
no4 = int(input("Enter your number"))
no5 = int(input("Enter your number"))

sum = (no1+no2+no3+no4+no5)
print (sum)

avg = (no1+no2+no3+no4+no5/5)
print (avg)

print ("_________________________________________________")

#2
items = ["Milk Punch","Bushwacher","Milk & Honey","Brownie Drowns","Honey Vanilla"]
for item in items:
    print(item)

print ("_________________________________________________")




