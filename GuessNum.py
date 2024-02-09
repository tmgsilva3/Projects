import random

print("Welcome to 'Guess The Number'! Let's play!")

answer = random.randint(1, 10)
guess = input("Enter your guess between 1 and 10: ")

print("The random number is: " + str(answer))

if (guess.isdigit()):
	if (guess == answer):
		print("You got it right!")
		quit()
	else:
		print("Try again next time!")
		quit()
else:
	print("Insert a number next time!")