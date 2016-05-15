import random

def handle_guesses():

    guessesTaken = 0

    print('Hello! What is your name?')
    myName = input()

    number = random.randint(1, 10) 
    print('Well, ' + myName + ', I am thinking of a number between 1 and 20...')

    while guessesTaken < 30:
        print('Take a guess: ')
        guess = input()
        guess = int(guess)

        guessesTaken = guessesTaken + 1
        

        if guess < number:
            print('Too low, try again: ')
        elif guess > number:
            print('Too high, try again: ')
        elif guess == number:
            break
        
    if guess == number:
        guessesTaken = str(guessesTaken)
        number = str(number) 
        print('Good job, ' + myName + '! You guessed my number, ' + number + ', in ' + guessesTaken + ' guesses!')
    if guessesTaken == 30:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number)


handle_guesses()
