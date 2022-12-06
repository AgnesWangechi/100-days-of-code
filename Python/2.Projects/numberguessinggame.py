import random # This is a python module for generating random numbers or characters in a list

# number = random.randrange(-1, 11) # It includes numbers from -1 to 10; it does nont include 11

# number2 = random.randint(-1, 11) # It includes numbers from -1 to 11 

top_of_range = input("Type the largest number to generate a random number from: ")

if top_of_range.isdigit(): #We want to make sure the user enters a digit and not strings
	top_of_range = int(top_of_range) # We are converting the input which is in string to an integer. 
	if top_of_range <=0:
		print('Please input a number greater than 0 next time')
		quit()
else:
	print('Please input a number')
	quit()
	
random_number = random.randint(0, top_of_range)
print(random_number)
guesses = 0

while True:
	guesses += 1
	user_guess = input("Make a guess (You get 3 tries): ")
	
	if user_guess.isdigit(): 
		user_guess = int(user_guess)
	
	else:
		print('Please input a number next time')
		continue
		
		
	if user_guess == random_number:
		print("You got it right!")
		break
	
	elif user_guess > random_number:
		print("You were above the number!")
		
	else:
		print("You were below the number!")
		
print("You got it in", guesses, "guesses")	
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
