"""Guesserr.py, written by Liam Heisler
This program allows person to guess a number between 1 and 100"""

import random

guesses = 0 

name = raw_input("What is your name?") 

number = random.randint(1, 50)

print (name + ", I am thinking of a number between 1 and 50..")

while guesses < 6:
	guess = int(raw_input("Take a guess.."))
	guesses = guesses + 1
	
	if guess < number:
		print("Your guess is too low.")
	elif guess > number:
		print("Your guess is too high.")
	elif guess == number:
		break 
if guess == number:
	print ("Good job, " + name + ", you guessed my number correctly, it was " + number)
	