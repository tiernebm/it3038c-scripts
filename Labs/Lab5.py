import random
guesses=0
print('Guess a number between 1 and 40, any number!')
number=random.randint(1,40)
while guesses<6:
    guess=input()
    guess=int(guess)
    guesses=guesses+1
    if guess<number:
        print('Your guess is too low')
    if guess>number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('Good job, You guessed the number!')
if guess != number:
    print('Sorry, out of chances. Try again!')