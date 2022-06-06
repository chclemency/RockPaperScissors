# -*- coding: utf-8 -*-
"""
Created on Tue May 31 12:36:35 2022

@author: cleme
"""
#imports
import random
import sys
import os
#variables and lists
#player_selection = [int(1), int(2), int(3)]- not used
comp_selection = [1, 2, 3]
#gameLength = [1, 3, 7] - not used
chosenLength = 0
loseRound = "Sorry, you lost this round"
winRound = "YOU WON THIS ROUND!"
loseGame = "Sorry, you lost the game...to a computer...\nthat has to be told what to think...don't quit your day job..."
winGame = "YOU WON THE GAME!!!  ...but nothing else..."
tieRound = "You both selected the same answer...no points awarded to either party"
playerAnswers = ["slings out the", "fires up the", "slaps down the", "launches the"]
playerScores = 0
computerScores = 0
replay = "N"

#try statement to cover any issues that may arise
try:
    print("Welcome to Rock, Paper, Scissors!!")
    print("    **    ","   "," ******","   "," *      *")
    print("  **  **  ","   "," *~~~~*","   ","  *    * ")
    print("**      **","   "," *~~~~*","   ","   *  *  ")
    print("**      **","   "," *~~~~*","   ","    **   ")
    print("  **  **  ","   "," *~~~~*","   ","   *  *  ")
    print("    **    ","   "," ******","   ","  @    @ ")


#Function for choosing game length - error handling included
    def chosen_length(game_length):
        print("Please choose a game length (1, 3 or 5)")
        game = game_length
        game = int(input())
        for i in range(11):
            if game == int(1) or game == int(3) or game == int(5):
                return game
            else:
                print("Sorry, that is not an option!")
                print("Please choose a game length (1, 3 or 5)")
                game = int(input())
                if i == 10:
                    print("Sorry, you have exceeded my expectations in getting this wrong...Shut down implemented!")
                    sys.exit()
                else:
                    continue
#variable for function to push - Modular
    chosenLength = chosen_length(chosenLength)         
    print("Please share your name (for the glory!!!)")
    playerName = input()

#while loop to itterate through each round and to handle a player's desire to play again
    i = 0
    while i < chosenLength:
        if replay == "y":
            chosenLength = chosen_length(chosenLength)
            replay = "n"
        print(playerName, "Please select 1 for 'Rock', 2 for 'Paper' or 3 for 'Scissors'")
        selection = int(input())
        selected = "none"
        compSel = "none"
        if selection == 1:
            selected = "rock."
        elif selection == 2:
            selected = "paper."
        elif selection == 3:
            selected = "scissors."
        comp = random.choice(comp_selection)
        if comp == 1:
            compSel = "rock."
        elif comp == 2:
            compSel = "paper."
        elif comp == 3:
            compSel = "scissors."
        print(playerName, random.choice(playerAnswers), selected)
        print("The machine", random.choice(playerAnswers), compSel)
        
#handles each rounds output as well as tallying score
        if selection == int(1) and comp == 2:
            print(loseRound)
            computerScores += 1
        elif selection == int(1) and comp == 3:
                print(winRound)
                playerScores += 1
        elif selection == int(1) and comp == 1:
                print(tieRound)
                continue
        elif selection == 2 and comp == 1:
                print(winRound)
                playerScores += 1
        elif selection == 2 and comp == 3:
                print(loseRound)
                computerScores += 1
        elif selection == 2 and comp == 2:
                print(tieRound)
                continue
        elif selection == 3 and comp == 1:
                print(loseRound)
                computerScores += 1
        elif selection == 3 and comp == 2:
                print(winRound)
                playerScores += 1
        elif selection == 3 and comp == 3:
                print(tieRound)
                continue
        else:
                print("I think you entered the wrong number...")
 #waits for playerscore to be greater then total rounds divided by 2               
        if playerScores > int(chosenLength)/2:
                print(winGame)
                computerScores = 0
                playerScores = 0
                result=input("\nDo you want to play again? [y/n] > ")
                if result=='y':
                    replay = "y"
                    continue
                else:
                    break;
 #waits for computerscore to be greater then total rounds divided by 2   
        if computerScores > int(chosenLength)/2:
                print(loseGame)
                computerScores = 0
                playerScores = 0
                result=input("\nDo you want to play again? [y/n] > ")
                if result=='y':
                    replay = "y"
                    continue
                else:
                    break;
#finally do this once done
finally:
        print("\nThe program will be closed...")
        sys.exit()
   
     