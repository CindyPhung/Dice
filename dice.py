import random
def dice1():
	number = random.randrange(1, 6)
	return number
	

print "Would you like to roll the dice?"
answer = raw_input("Y/N > ")


if answer == "Y" or answer == "y":
	print "%s, %s" %(dice1(), dice1())
else:
	print "Sorry to hear that. Goodbye."
