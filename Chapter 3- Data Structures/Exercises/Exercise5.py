'''You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.'''

guests = ["Johan","Sathwik","Alan"]
for name in guests :
    print (f"Hello, {name}!, Inviting you for a dinner. Would you like to join?")

guest_cant_come = "Alan"
 print (f"\nUnfortunately, {guest_cant_come} cant come for dinner")

new_guest = "Sheehan"
 guests[guests.index(guest_cant_come)] = new_guest

print ("Invitation update")
for guest in guests:
  print (f"Dear {guest}, you are invited for dinner. Would you like to come?")
  