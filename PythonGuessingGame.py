# Amy Nguyen
# 11/18/2018
# CS 3377.0W3
# Number Guessing Game - Python

import random

print("-----------------------------------------------------")
print("                                                     ")
print("                       Welcome                       ")
print("           Please enter your player name.            ")
print("                                                     ")
print("-----------------------------------------------------\n")

player = input()

print("\n-----------------------------------------------------")
print("                                                     ")
print("                 Number Guessing Game                ")
print(" A random number will be generated from -100 to 100. ")
print("  Guess the number within 10 tries in order to win.  ")
print("     A lower number of attempts is a high score.     ")
print("     A higher number of attempts is a low score.     ")
print("                      Good luck!                     ")
print("                                                     ")
print("-----------------------------------------------------\n")

# Generate Random Number Between -100 and 100
randomNumber = random.randint(-100,100)
print("Debugging number = ", randomNumber)

# Initialize number of tries
tries = 0

print("\n-----------------------------------------------------")
print("                                                     ")
print("         The random number has been generated.       ")
print("           Please enter your guess below.            ")
print("                                                     ")
print("-----------------------------------------------------\n")

guess = int(input())


# Loop for guesses
while (guess != randomNumber and tries < 10):

    # If the guess is not between -100 and 100, error message
    if (guess < -100 or guess > 100):
        print("\n-----------------------------------------------------")
        print("                                                     ")
        print("                        ERROR!                       ")
        print("       Your guess was not between -100 and 100.      ")
        print("            Please enter a valid number.             ")
        print("                                                     ")
        print("-----------------------------------------------------\n")
    
        guess =int(input())

    # If guess is greater than random number
    elif (guess > randomNumber):
        tries += 1
        
        print("\n-----------------------------------------------------")
        print("                                                     ")
        print("               Your guess was too high!              ")
        print("                     Try again.                      ")
        print("                Number of tries = ", tries, "        ")
        print("                                                     ")
        print("-----------------------------------------------------\n")
        
        guess = int(input())

    # If guess is less than random number
    elif (guess < randomNumber):
        tries += 1
        print("\n-----------------------------------------------------")
        print("                                                     ")
        print("               Your guess was too low!               ")
        print("                     Try again.                      ")
        print("                Number of tries = ", tries, "        ")
        print("                                                     ")
        print("-----------------------------------------------------\n")

        guess = int(input())

if (guess == randomNumber and tries < 10):
    tries += 1
    print("\n****************************************************")
    print("                                                     ")
    print("                    !!!YOU WIN!!!                    ")
    print("               The random number was ", randomNumber  )
    print("               You guessed correctly!                ")
    print("                Number of tries = ", tries, "        ")
    print("                                                     ")
    print("******************************************************\n")

if (tries > 10 and guess != randomNumber):
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("                                                     ")
    print("        You have used up all of your tries.          ")
    print("                 !!!YOU LOSE!!!                      ")
    print("                   GAME OVER                         ")
    print("                                                     ")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

# Write out score data to file
file = open("scores.txt", "a")
file.write (player + " " + '%d' %tries + "\n")

file.close
print("\n Results have been printed to scores.txt. \n")