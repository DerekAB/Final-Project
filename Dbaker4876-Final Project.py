#Name:                  Dbaker4876-Final Project.py
#Author:                Derek Baker
#Date Created:          05-04-2023
#Date Last Modified:    05-04-2023
#
#Purpose:
#This program is a game of rock, paper, scissors between a player and the computer. 
#The game will be best two out of three, and the results will be added to a text file

#importing the Random and OS for use
import random

import os

#defining the scores as zero
playerWins = 0
compWins = 0


#defining the path for the text file
path = 'Results.txt'

#creating a class for each of the three objects so that they can have a type
class Game:
    
    def __init__(self, type):
        self.type = type

#giving the objects a type
r = Game('rock')
s = Game('scissors')
p = Game('paper')

#creating the random number generator that will determine what the computer picks
def bot():
    global option
    option = random.randint(1, 3)
    if option == 1:
        option = r
    if option == 2:
        option = s
    if option == 3:
        option = p

#creating a function that will tell the player that there was a tie, as well as adding the round results
#to the text file
def tie():
    global output
    print('\nRound {} is a Tie!'.format(x))
    output += '\nRound {}: Tie'.format(x)
    
#a function that will tell the player that they won the round and adds 
#that rounds results to the text file
def playerWin():
    global output, playerWins
    print('\n{} wins round {}'.format(player, x))
    output += '\nRound {}: {} wins'.format(x, player)
    playerWins += 1

#a function that will tell the player that they computer won the round
#and will add the round results to the text file
def botWin():
    global output, compWins
    print('\nComputer wins round {}'.format(x))
    output += '\nRound {}: Computer wins'.format(x)
    compWins += 1

#the start of the program
print("Welcome to Rock, Paper, Scissors!\n")

#getting the players name so that the game can be more personalized
player = input("Please enter your name: ").strip().capitalize()


print("Hi {}, you will be playing against the computer. Good luck!\n".format(player))

#defining the variable that will be output into the text file
output = 'Game between the computer and {}'.format(player)


#the variable 'x' is the round counter
#this while loop will continue until the win requirements have been met
x = 1
while playerWins < 2 or compWins <2:
    bot()           #calling the 'bot' function to generate which option it chooses
    #the program asks for the player's choice
    choice = input("\nMake your choice:\n\nRock\nPaper\nScissors\n\n").strip().lower()
    
    #while loop to ensure they pick an appropriate option
    while not(choice == 'rock' or choice == 'paper' or choice == 'scissors'):
        choice = input('Please enter a valid option: ').strip().lower()
        
    #defining their choice as the appropriate object
    if choice == 'rock':
        choice = r
    elif choice == 'paper':
        choice = p
    else:
        choice = s
    #program will compare the choices between the player and the computer and call the
    #appropriate function based on who won or if they tied
    if choice.type == 'rock' and option.type == 'rock':
        tie()
    elif choice.type == 'rock' and option.type == 'paper':
        botWin()
    elif choice.type == 'rock' and option.type == 'scissors':
        playerWin()
    elif choice.type == 'paper' and option.type == 'paper':
        tie()
    elif choice.type == 'paper' and option.type == 'rock':
        playerWin()
    elif choice.type == 'paper' and option.type == 'scissors':
        botWin()
    elif choice.type == 'scissors' and option.type == 'scissors':
        tie()
    elif choice.type == 'scissors' and option.type == 'rock':
        botWin()
    elif choice.type == 'scissors' and option.type == 'paper':
        playerWin()
    
    #ensuring that the round counter goes up
    x += 1
    #adding the win conditions
    if playerWins == 2:
        break
    if compWins == 2:
        break

#if the player beats the computer, it will tell them that they won as well as putting the win into the text file
if playerWins == 2:
    output += '\nYou Won!'
    with open(path, 'w') as file:
        file.write(output)
    print('Congratulations! You Win!')
    print('You can find the results of the match in ' + os.getcwd())

#if the computer wins, the player gets a message saying so and adds the final result into the text file
elif compWins == 2:
    output += '\nOh No! You lost :('
    with open(path, 'w') as file:
        file.write(output)
    print('Tough luck. You Lost :(')
    print('\nYou can find the results of the match in ' + os.getcwd())


