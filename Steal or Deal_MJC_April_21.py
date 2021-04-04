
import random                                                                                                           # import random module for generating computer score

                                                                                                                        # creating variables to be used within the game.
computerChoice = random.randint(1,2)                                                                                    # assign random variable for computers choice
computerScore = 0                                                                                                       # variable to count the computers score
humanScore = 0                                                                                                          # variable to count the humans/players score
gameCount = 0                                                                                                           # variable to count the amount of games played
gamesWon = 0                                                                                                            # variable to count the amount of games won by the human/player
gamesLost = 0                                                                                                           # variable to count the amount of games lost by the human/player
gamesDrawn = 0                                                                                                          # variable to count the amount of games drawn by the human/player
stealCount = 0                                                                                                          # variable to count the amount of games where the human selects steal


print("Welcome to Steal or Deal!")                                                                                      # initialise game welcoming the user and asking them to select a strategy for the computer.
print("-------------------------")
print("")
print("1. Always steal")
print("2. Always deal")
print("3. Random")
print("")


compStrategy = int(input("Which Strategy for the computer [1,2,3]? "))                                                  # prompt for user to select the strategy of the computer. Strategy can be always steal, always deal or random

if compStrategy > 3:                                                                                                    # control to limit users entry to the 3 choices
    print("Please enter either 1, 2, or 3.")
    print("")
    compStrategy = int(input("Which Strategy for the computer [1,2,3]?"))
elif compStrategy == 1:                                                                                                 # passing value to computer choice variable to be used during the games.
    computerChoice = 1
elif compStrategy == 2:
    computerChoice = 2

print("")                                                                                                               # print jackpot to be won and prompt the user to make their game choice
print("Jackpot: 100")
gameAnswer = (input("Steal, Deal or Quit [s|d|q]? "))
print("")


if gameAnswer == "q":                                                                                                   # if user selects quit they receive acknowledgement
    print("")
    print("No worries... another time perhaps : )")


elif gameAnswer == 's':                                                                                                 # displaying humans selection
    print("You chose: Steal")
    stealCount += 1
elif gameAnswer == 'd':
    print("You chose: Deal")


elif computerChoice == 1:                                                                                               # displaying computers selection
    print("Comp chose: Steal")
elif computerChoice == 2:
    print("Comp chose: Deal")


if computerChoice == 2 and gameAnswer == "d":                                                                           # comparing answers in case of a draw and defining the result to assign scores
    print("Draw! Split pot - 50 each")
    gamesDrawn += 1                                                                                                     # assigning count to the draw sum
    humanScore += 50                                                                                                    # assigning score to the human score sum
    computerScore += 50                                                                                                 # assigning score to the computer score sum

    print("")                                                                                                           # displaying score summary to screen
    print(">> Your Score: ", humanScore, "-- Comp score: ", computerScore, "<<")
    print("")

if computerChoice == 1 and gameAnswer == 'd':                                                                           # comparing answers in case of a loss and defining the result to assign scores
    print("You lose! Comp gains 100")
    gamesLost += 1                                                                                                      # assigning count to the loss sum
    computerScore += 100                                                                                                # assigning score to the computer score sum

    print("")                                                                                                           # displaying score summary to screen
    print(">> Your Score: ", humanScore, "-- Comp score: ", computerScore, "<<")
    print("")

if computerChoice == 2 and gameAnswer == 's':                                                                           # comparing answers in case of a win and defining the result to assign scores
    print("You win! you gain 100")
    gamesWon += 1                                                                                                       # assigning count to the win sum
    humanScore =+ 100                                                                                                   # assigning score to human score sum

    print("")                                                                                                           # displaying score summary to screen
    print(">> Your Score: ", humanScore, "-- Comp score: ", computerScore, "<<")
    print("")

if computerChoice == 1 and gameAnswer == 's':                                                                           # comparing answers in case of a double loss and defining the result to assign scores
    print("Too greedy! You get nothing")
    gamesLost += 1                                                                                                      # assigning score to the human loss sum

    print("")
    print(">> Your Score: ", humanScore, "-- Comp score: ", computerScore, "<<")
    print("")

while gameCount < 9 and gameAnswer != "q":                                                                              # create loop to cycle through multiple games but also control the quit option
    gameCount = gameCount + 1

    print("Jackpot: 100")                                                                                               # prompt to play
    gameAnswer = (input("Steal, Deal or Quit [s|d|q]? "))
    print("")

    if gameAnswer == 's':                                                                                               # display users selection
        print("You chose: Steal")
    if gameAnswer == 'd':
        print("You chose: Deal")

    if computerChoice == 1:                                                                                             # display computers selection
        print("Comp chose: Steal")
    if computerChoice == 2:
        print("Comp chose: Deal")

    if computerChoice == 2 and gameAnswer == "d":                                                                       # evaluate answers for draw and assign scores
        print("Draw! Split pot - 50 each")
        gamesDrawn += 1
        humanScore += 50
        computerScore += 50
    if computerChoice == 1 and gameAnswer == 'd':                                                                       # evaluate answers for human loss and assign scores
        print("You lose! Comp gains 100")
        gamesLost += 1
        computerScore += 100
    if computerChoice == 2 and gameAnswer == 's':                                                                       # evaluate answers for human win and assign scores
        print("You win! you gain 100")
        gamesWon += 1
        humanScore = + 100
    if computerChoice == 1 and gameAnswer == 's':                                                                       # evaluate answers for double loss and assign scores
        print("Too greedy! You get nothing")
        gamesLost += 1

        if stealCount == 3:                                                                                             # limiting the human users steal count and removing all points if the steal 3 times.
            print("")
            print("I told you... you lose all of your winnings")
            print("")
            humanScore = 0                                                                                              # assigning users score as 0 in response to stealing 3 times.
            print("")
            print(">> Your Score: ", humanScore, "-- Comp score: ", computerScore, "<<")
            print("")

    print("")
    print(">> Your Score: ", humanScore, "-- Comp score: ", computerScore, "<<")                                        # displaying score summary after each loop
    print("")

    if gameAnswer == "q":                                                                                               # display games summary if quit is selected
        print("Game Summary")
        print("------------")
        print("")
        print("You played ", gameCount, "games:")
        print("|--> Won:   ", gamesWon)
        print("|--> Lost:  ", gamesLost)
        print("|--> Drawn: ", gamesDrawn)
        print("")
        print("Your final score: ", humanScore)
        print("Comp final score: ", computerScore)

        if humanScore > computerScore:                                                                                  # evaluate results and proclaim the human winner
            print("")
            print("You win!")
        elif computerScore > humanScore:                                                                                # evaluate results and proclaim the computer winner
            print("")
            print("Computer Wins!")

        print("")
        print("Thanks for playing : )")

    if gameCount == 10:                                                                                                 # game count control limiting games to 10.
        print("")
        print("Game Limit reached")
        print("")



    else:                                                                                                               # once the limit of games played has been reached the game summary is printed with the results.
        print("Game Summary")
        print("------------")
        print("")
        print("You played ", gameCount, "games:")
        print("|--> Won:   ", gamesWon)
        print("|--> Lost:  ", gamesLost)
        print("|--> Drawn: ", gamesDrawn)
        print("")
        print("Your final score: ", humanScore)
        print("Comp final score: ", computerScore)

        if humanScore > computerScore:
            print("")
            print("You win!")
        elif computerScore > humanScore:
            print("")
            print("Computer Wins!")
        elif computerScore == humanScore:
            print("")
            print("Draw - No Winner")

        print("")
        print("Thanks for playing : )")



