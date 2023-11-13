'''Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.'''

usb_price = 9
budget = 100
num_usbstick = budget // usb_price
remain = budget % usb_price
print (f"She can buy {num_usbstick} usb sticks with {budget} Dhs, and she will have a reamaining of {remain} Dhs left ")