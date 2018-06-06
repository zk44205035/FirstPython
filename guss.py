import random
running= True
number=random.randint(0,100)
while running:
	guess = raw_input("Guess the Number:")
	guess_int = int(guess)
	if number > guess_int:
		print "Too low!"
	if number < guess_int:
		print "Too high!"
	if number == guess_int:
		print "You got it!"
	        running = False