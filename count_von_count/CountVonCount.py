# version: CountvonCount 1.0
# author: Sabrina Schmütsch


# Instruction
# 1 Open an online interpreter for python (e.g. https://www.online-python.com/)
# 2 Copy this script.
# 3 Paste the script into the code editor on the website.
# 4 Press the green "Run"-button to start the script.
#   You will see the output in the console at the bottom of the page.
# 5 To interact with the script, type your answer in the console input field and press Enter to submit.


# planned Updates:
    # Extension to include language selection for German
    # Improvement of interactiv responses
    # Improvement of code structure

# import needed packages
import time
import textwrap
import sys
import random

#function for typewriter-effect-output
def typewriter(str):  # define function for typewriter effect
    str = textwrap.dedent(str).strip()  # remove indentation from text

    for char in str:
        sys.stdout.write(char)  # character-by-character output
        sys.stdout.flush()  # empty the buffer and display immediately
#        time.sleep(0.05)   # delay for typewriter effect
    print()     # new line after output


#Introduction
typewriter("""\
Greetings! It is I, the Count!
I guess you've heard from me before. I'm well known for my mathematical teaching skills.
I love to count.
What's your name?"""
           )

name = ""   # global variable

def getUserName():  # define function for input
    global name     # use global item

    while True:     # create infinite loop
        name = input().strip()  # get input, delete whitespace

        if not name:    # check if input is empty
            typewriter("Don't be shy! Please tell me your name. (Your input can't be empty.)")

        elif not name.isalpha():    # check if input contains non-letter characters
            typewriter("""\
               I love numbers and symbols... But now I like to get some letters.
               (Your input can only contain letters.)""")

        else:   # confirm that input is valid
            typewriter("Would you like to play a game with me, " + name.capitalize() + "? (yes/no)")
            break   # exit loop

getUserName()


while True:     # create infinite loop, game resumes after correct input
    userInput = input()

    if userInput.lower() == "yes":  # set input to lowercase letter, check if input is "yes"
        typewriter("""\
            Alright!
            It's a guessing game: I will choose a number between 1 and 100 [1,100].
            You need to guess which number it is. 
            Let's begin!"""
                   )
        break   # exit loop

    elif userInput.lower() == "no":     # set input in lowercase letter, check if input is "no"
        typewriter("""\
        I'm sorry that you missed out a chance to learn something about numbers.
        Remember: If you dont ask, you won't know. Goodbye, """ + name.capitalize() + """!"""
                   )
        exit()  # exit script

    else:   # restart loop to prevent game from crashing due to incorrect input
        typewriter("Sorry, I didn't understand you. (Enter 'yes' or 'no'.)")


while True:     # create infinite loop: allows to replay the game
    myNumber = random.randint(1,100)    # draw random number between 1 and 100
    guessesTaken = 0    # set number of guesses to 0
    guessesMax = 10     # set maximum number of guesses to 10

    outputGuess = [
        "Take a guess!",
        "Give me a number!",
        "What's your tip?",
        "Make a guess!",
        "Take a shot!",
        "Give it a try!",
        "Make a guess!",
        "Tell me a number!",
        "What number do you have in mind?",
        "Please share your number!"
    ]   # list of answer possibilities "to guess"

    typewriter(random.choice(outputGuess))  # choose random item from list outputGuess


    while guessesTaken < guessesMax:    # loop as long as limit of guesses isn't reached
        try:    # start to look for exceptions
            guess = int(input())    # convert input to int

            if 1 <= guess <= 100:   # check if input is in range 1-100
                guessesTaken += 1  # if True add +1 to round counter

                outputGuessAgain = [
                    " Try again!",
                    " Give it another shot!",
                    " Take another guess!",
                    " Have another go!",
                    " Give it another try!",
                    " Try once more!",
                    " Take a swing at it again!",
                    " Give it one more attempt!",
                    " Let’s see another guess!",
                    " You can do better, try again!"
                ]   # list of answer possibilities "to guess again"

                if guess < myNumber:    # check if input < random number
                    if guessesTaken < guessesMax:
                        outputLowNumber =[
                            "Your guess is too low.",
                            "That guess is below the target.",
                            "Too low!",
                            "You're under the correct number.",
                            "That’s not high enough.",
                            "You need to guess a larger number.",
                            "You're below the mark.",
                            "That number is too small.",
                            "You might want to go higher.",
                            "Try a number that's more than that."
                        ]   # list of answer possibilities if guess is lower than myNumber
                        typewriter(random.choice(outputLowNumber) + random.choice(outputGuessAgain))

                elif guess > myNumber:  # check if input > random number
                    if guessesTaken < guessesMax:
                        outputHighNumber = [
                            "Your guess is too high.",
                            "That guess is above the target.",
                            "You're too high.",
                            "Too high; aim a bit lower!",
                            "You're over the correct number.",
                            "That’s not low enough.",
                            "You need to guess a smaller number.",
                            "You're above the mark.",
                            "That number is too large.",
                            "You might want to go lower.",
                            "Try a number that's less than that."
                        ]   # list of answer possibilities if guess is higher than myNumber
                        typewriter(random.choice(outputHighNumber) + random.choice(outputGuessAgain))

                else:
                    break   # If guess is correct, end loop

            else:
                typewriter("Please enter a number between 1 and 100.")  # check if 0 < input < 100

        except ValueError:  # check for exceptions
            typewriter("Sorry, but your answer doesn't make sense "
                       "(Please enter a number between 1 and 100.)")


    if guess == myNumber:   # check if input == random number
        if guessesTaken > 1:    # check if number of guesses >1
            typewriter("Well done! You guessed my number in " + str(guessesTaken) + " guesses!")

        else:
            typewriter("Well done! You guessed my number in " + str(guessesTaken) + " guess!")

    else:
        typewriter("Sorry, you're out of guesses. My number is " + str(myNumber) + ".")


    typewriter("Would you like to play another round? (yes/no)")    # ask to restart the loop
    userInput= input().lower() # set input in lowercase letters

    while True:     # create infinite loop
        if userInput == "yes":
            break   # end this loop, start superodinate loop

        elif userInput == "no":
            typewriter("Thank your for playing! I hope I can count on you again soon, " + name.capitalize() + ". Goodbye! Ah-ah-ah!")
            quit()  # leave game

        else:
           typewriter("Sorry, I didn't get this. (Enter 'yes' or 'no'.)")
           userInput = input().lower()    # get input again
