#juliana resendiz



#init

import random


#function

def guessing_game():
    print("Welcome to the Guessing Game! Today you will be attempting to guess a random number!")
    print("You will be given 3 differet opportunities to guess the mystery number!")
    ans = input("Would you like to play on easy(e), medium(m), or hard(h) difficulty?")
    if ans == "e":
        guess = int(input(" Please enter your 1st guess between 1 and 10"))
        secret = random.randint(1, 10)
        print(secret)
        if guess == secret:
            print("Congratulations you have succesfully guessed the mystery number! The mystery number was "+ str(secret))
            quit()
        elif guess == secret + 1 or guess == secret - 1:
            guess = input("Unfortunately that is not correct but you are close, try again with another guess")
        else:
            guess = input("Unfortunately that is incorrect and you are far from the mystery number, try again with another guess")
        if guess == secret:
            print("Congratulations you have succesfully guessed the mystery number! The mystery number was "+ str(secret))
            quit()
        elif guess == secret + 1 or guess == secret - 1:
            guess = input("Unfortunately that is not correct but you are close, try again with another guess")
        else:
            guess = input("Unfortunately that is incorrect and you are far from the mystery number, try again with another guess")
        if guess == secret:
            print("Congratulations you have succesfully guessed the mystery number! The mystery number was "+ str(secret))
        else:
            print("Aww unfortunately that was incorrect and your final guess, the mystery number was actually "+str(secret)+" better luck next time")
    if ans == "m":
        guess = int(input(" Please enter your 1st guess between 1 and 20"))
        secret = random.randint(1, 20)
        print(secret)
        if guess == secret:
            print("Congratulations you have succesfully guessed the mystery number! The mystery number was "+ str(secret))
            quit()
        elif guess == secret + 1 or guess == secret - 1:
            guess = input("Unfortunately that is not correct but you are close, try again with another guess")
        else:
            guess = input("Unfortunately that is incorrect and you are far from the mystery number, try again with another guess")
        if guess == secret:
            print("Congratulations you have succesfully guessed the mystery number! The mystery number was "+ str(secret))
            quit()
        elif guess == secret + 1 or guess == secret - 1:
            guess = input("Unfortunately that is not correct but you are close, try again with another guess")
        else:
            guess = input("Unfortunately that is incorrect and you are far from the mystery number, try again with another guess")
        if guess == secret:
            print("Congratulations you have succesfully guessed the mystery number! The mystery number was "+ str(secret))
        else:
            print("Aww unfortunately that was incorrect and your final guess, the mystery number was actually "+str(secret)+" better luck next time")
    if ans == "h":
        guess = int(input(" Please enter your 1st guess between 1 and 100"))
        secret = random.randint(1, 100)
        print(secret)
        if guess == secret:
            print("Congratulations you have succesfully guessed the mystery number! The mystery number was "+ str(secret))
            quit()
        elif guess == secret + 1 or guess == secret - 1:
            guess = input("Unfortunately that is not correct but you are close, try again with another guess")
        else:
            guess = input("Unfortunately that is incorrect and you are far from the mystery number, try again with another guess")
        if guess == secret:
            print("Congratulations you have succesfully guessed the mystery number! The mystery number was "+ str(secret))
            quit()
        elif guess == secret + 1 or guess == secret - 1:
            guess = input("Unfortunately that is not correct but you are close, try again with another guess")
        else:
            guess = input("Unfortunately that is incorrect and you are far from the mystery number, try again with another guess")
        if guess == secret:
            print("Congratulations you have succesfully guessed the mystery number! The mystery number was "+ str(secret))
        else:
            print("Aww unfortunately that was incorrect and your final guess, the mystery number was actually "+str(secret)+" better luck next time")


#main
guessing_game()
