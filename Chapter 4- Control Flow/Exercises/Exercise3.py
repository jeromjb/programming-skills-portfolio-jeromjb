'''Turn your if-else chain from Exercise 5-4 into an if-elifelse
 chain.
•	 If the alien is green, print a message that the player 
earned 5 points.
•	 If the alien is yellow, print a message that the player 
earned 10 points.
•	 If the alien is red, print a message that the player e
arned 15 points.
•	 Write three versions of this program, making sure each 
message is printed for the appropriate color alien.'''
alien_colour = "yellow"
if alien_colour == "greean":
    print ("Congratulations! You just earned 5 points")

elif alien_colour == "yellow":
    print ("Congratulations! You just earned 10 points")

elif alien_colour == "red":
    print ("Congratulations! You just earned 15 points")

else :
    print ("Invalid colour")
