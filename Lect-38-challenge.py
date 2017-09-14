# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 10

# Selects a random number as the answer
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))

# Initialization is compulsory in case of WHILE loops
guess = 0

while guess != answer:
    guess = int(input())
    # if guess == 0, then it will terminate the code and the game will be over
    if guess == 0:
        print("Game Over")
        break
    elif guess < answer:
        print("Guess higher")
    elif guess > answer:
        print("Guess lower")
    else:
        print("You've guessed it correctly !!")
