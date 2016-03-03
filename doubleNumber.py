userNumber = raw_input("Tell me a number. " )
finalNumber = "none"

while finalNumber == "none":
	try:
		finalNumber = float(userNumber)
		#Only put lines that you expect to cause exceptions here
	except ValueError:
		print("Uhhhh, that's not a number")
		userNumber = raw_input("Try again: ")	
		

print("Double that is {} . ".format(finalNumber * 2))