import random

def guess(x):
    random_number = random.randint(1, x) #return a random number for us to guess
    #looping through till our guess number = random number
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        print(guess)
        if guess < random_number:
            print('Sorry, guess is again, Too Low')
        elif guess > random_number:
            print('Sorry, guess again.Too high')
    print(f'Yay congrats, You have guessed the {random_number} correctly')
    
guess(10)
