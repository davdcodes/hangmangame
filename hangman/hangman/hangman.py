import random

# defines most important variables and lists

gameEnd = False
replay = "n"

easywordbank = ["BANANA", "LISTEN", "FRIEND", "PICTURE", "JOURNEY", "BICYCLE", "PIRATE", "COUNTRY", "PROBLEM", "CAPTAIN", "DIAMOND", "KITCHEN", "MORNING", "STATION", "CONCERT", "LIBRARY", "PERFECT", "FREEDOM", "HEALTHY", "WEATHER"]
medwordbank = ["ELOQUENT", "GRATITUDE", "NOTABLE", "IMMINENT", "PONDEROUS", "JUBILANT", "FLUCTUATE", "DELICATE", "SERENITY", "IMPARTIAL", "RESILIANT", "INTREPID", "DILIGENT", "SERENADE", "NOTORIOUS", "MAVERICK", "INSCRIBE", "AMBIGUOUS", "PROCLAIM", "PERVASIVE"]
hardwordbank = ["SERENDIPITY", "UBIQUITOUS", "PERSPICACIOUS", "DISCOMBOBULATE", "MELANCHOLY", "QUIXOTIC", "EPHEMERAL", "VICARIOUS", "SYCOPHANT", "SCHADENFREUDE", "JUXTAPOSITION", "PARADOXICAL", "OBFUSCATE", "CACOPHONY", "IDIOSYNCRASY", "ENIGMATIC", "RESPLENDENT", "MELLIFLUOUS", "INEFFABLE", "INSCRUTABLE"]

# ascii for the hangman. yeah, it takes up a lot of lines. not sure how id cut down on this yet

def printgame(strikes, blankword, wrongLetters):
    print()
    if strikes == 0:
        print("        _____________       ")
        print("        |           |       ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("________|________           ")
        print()
    elif strikes == 1:
        print("        _____________       ")
        print("        |         _|_       ")
        print("        |        /   \      ")
        print("        |       |     |     ")
        print("        |        \___/      ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("________|________           ")
    elif strikes == 2:
        print("        _____________       ")
        print("        |         _|_       ")
        print("        |        /   \      ")
        print("        |       |     |     ")
        print("        |        \___/      ")
        print("        |          |        ")
        print("        |          |        ")
        print("        |          |        ")
        print("        |          |        ")
        print("        |          |        ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("________|________           ")
    elif strikes == 3:
        print("        _____________       ")
        print("        |         _|_       ")
        print("        |        /   \      ")
        print("        |       |     |     ")
        print("        |        \___/      ")
        print("        |         /|        ")
        print("        |        / |        ")
        print("        |       /  |        ")
        print("        |      /   |        ")
        print("        |          |        ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("________|________           ")
    elif strikes == 4:
        print("        _____________       ")
        print("        |         _|_       ")
        print("        |        /   \      ")
        print("        |       |     |     ")
        print("        |        \___/      ")
        print("        |         /|\       ")
        print("        |        / | \      ")
        print("        |       /  |  \     ")
        print("        |      /   |   \    ")
        print("        |          |        ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("        |                   ")
        print("________|________           ")
    elif strikes == 5:
        print("        _____________       ")
        print("        |         _|_       ")
        print("        |        /   \      ")
        print("        |       |     |     ")
        print("        |        \___/      ")
        print("        |         /|\       ")
        print("        |        / | \      ")
        print("        |       /  |  \     ")
        print("        |      /   |   \    ")
        print("        |          |        ")
        print("        |         /         ")
        print("        |        /          ")
        print("        |       /           ")
        print("        |      /            ")
        print("        |     /             ")
        print("________|________           ")
    elif strikes == 6:
        print("        _____________       ")
        print("        |         _|_       ")
        print("        |        /   \      ")
        print("        |       |     |     ")
        print("        |        \___/      ")
        print("        |         /|\       ")
        print("        |        / | \      ")
        print("        |       /  |  \     ")
        print("        |      /   |   \    ")
        print("        |          |        ")
        print("        |         / \       ")
        print("        |        /   \      ")
        print("        |       /     \     ")
        print("        |      /       \    ")
        print("        |     /         \   ")
        print("________|________           ")
    
    if strikes != 6:
        print("Current Progress: ")
        print(blankword)
        print("Missed Letters: ")
        print(wrongLetters)
    
while replay != "q":

    # resets all major variables

    if replay == "2":
        wordbank = medwordbank
    elif replay == "3":
        wordbank = hardwordbank
    else:
        wordbank = easywordbank

    currword = wordbank[random.randint(0,19)]
    availLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    wrongLetters = []
    strikes = 0
    
    blankword = []

    for i in range(len(currword)):
        blankword.append("_")

    # guessing feature
    
    printgame(strikes,blankword,wrongLetters)
    userletter = input("Enter your letter guess for the word! ")

    while gameEnd == False: 

        userletter = userletter.upper()

        # game determines if letter is a singular letter, then if it has already been tried, then if it is in the word or not
        # game also checks if player has won or lost the round

        if len(userletter) == 1:
            if userletter in availLetters:

                if currword.find(str(userletter)) != -1:
                    print("Nice! That letter was in the word!")
                    for i in range(len(currword)):
                        if currword[i] == userletter:
                            blankword[i] = userletter
                    printgame(strikes,blankword,wrongLetters)

                else:
                    print("Too bad! That letter wasn't in the word!")
                    wrongLetters.append(userletter)
                    strikes += 1
                    printgame(strikes,blankword,wrongLetters)

                availLetters.remove(userletter)

                if not ("_" in blankword):
                    print("Congrats! You win! The word was " + currword)
                    break
                if strikes >= 6:
                    print("Uh oh! You lose! The word was " + currword)
                    break

                userletter = input("What letter will you try next? ")

            else:
                userletter = input("You already tried that letter! Try a different one. ")

        else:
            userletter = input("Please enter a single available letter! ")

        print("-------------------------------------------------------------------------------------------")

    print()
    print("Would you like to play again? Enter any key except 'q' to play again!")
    replay = input("Or, try entering any number 1, 2, or 3, to try a more easy, medium, or hard word (respectively). ")
    
print()
print("That was fun, thanks for playing! :)")