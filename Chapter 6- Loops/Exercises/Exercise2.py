'''A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 

age, and then tell them the cost of their movie ticket'''


while True:
    age_input = input("Enter you age or 'quit' to exit : ")
    if age_input.lower() == 'quit':
        break
    try:
        age = int(age_input)
    except ValueError:
        print ("Please enter a valid age")
        continue
    if age < 3:
        ticket_cost = 0
    elif 3 <= age <= 12:
        ticket_cost = 10
    else:
        ticket_cost = 15

    print (f"The cost of your movie ticket is {ticket_cost} dhs")

    