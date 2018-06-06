import random
running= True
number=random.randint(0,100)

count = 0

while running:
	guess = raw_input("Guess the Number:")
	guess_int = int(guess)
	if number > guess_int:
		count+=1
		print "Too low!"
		print "Sum:"
		print count
	if number < guess_int:
		count+=1
		print "Too high!"
		print "Sum:"
		print count
	if number == guess_int:
		count+=1
		print "You got it!" 
		print "Sum:"
		print count
	        running = False