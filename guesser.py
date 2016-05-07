#This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name? ')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20...')

while guessesTaken < 20:
    print('Take a guess: ')
    guess = input()
    guess = int(guess)

    guessesTaken =guessesTaken + 1

    if guess < number:
        print('Too low, try again: ')
    elif guess > number:
        print('Too high, try again: ')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
