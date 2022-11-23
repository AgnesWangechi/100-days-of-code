import random # A python library that is used to make things chosen in random

def get_choices(): # Defines a function
	player_choice = input("Enter a choice(rock, paper, scissors): ") #Getting the user input using the input function
	options = ["rock","paper", "scissors"] # Example of a list
	computer_choice = random.choice(options) # Calling the random library to choose among the options list
	choices = {"player": player_choice, "computer": computer_choice} #Example of a dictionary
	
	return choices
	
def check_win(player, computer):
	print("You chose " + player) # Concatenating Strings
	print(f"Computer chose {computer}")# F-strings
	
	if player == computer:
		return ("It's a tie!")
		
	elif player == "rock":
		if computer =="scissors":
			return ("Rock smashes scissors! You win")
		else:
			return ("Paper covers rock! You lose")
			
	elif player == "paper":
		if computer =="scissors":
			return ("Scissors cuts paper, you lose")
		else:
			return ("Paper covers rock! You win")
			
	elif player == "scissors":
		if computer =="rock":
			return ("Rock smashes scissors! You lose")
		else:
			return ("Scissors cuts paper! You win")
	
choices = get_choices()			
result = check_win(choices["player"], choices["computer"]) # Assesing dictionaries
print(result)		
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
	
	
	

