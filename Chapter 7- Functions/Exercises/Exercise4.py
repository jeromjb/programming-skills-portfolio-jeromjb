'''Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

medium shirt with the default message, and a shirt of any size with a different message.
'''


def make_shirt(size="Large",msg="Nothing but Jesus"):
    print (f"Made a shirt of size {size} with the message:'{msg}'")
make_shirt()

make_shirt (size="Medium")
make_shirt (size="Small", msg="I love Jesus")
