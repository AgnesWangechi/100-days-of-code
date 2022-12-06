import random
# Greet the user
# Create a list of anime that generates random anime
# Create a fuction to hold the list
# Create a fuction to add to the list
# Create a fuction to delete from the list

def hello(name): # name is a parameter
	print('Hello', name)

def anime_list():
	anime = ['Attack on Titan', 'Chainsaw Man', 'Hunter x Hunter', 'Hero Academia', 'Komi can\'t communicate', 'Jujutsu Kaisen', 'Maid Sama', 'Spy x Family', 'Relife', 'Banana Fish', 'One Piece', 'Kaguya Sama (Love is war)', 'Grave of Fireflies', 'Prison School']
	

hello("Wangechi")
watch = random.choice(anime_list())
print (watch)




