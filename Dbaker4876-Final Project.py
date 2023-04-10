#Name:                  Dbaker4876-Final Project.py
#Author:                Derek Baker
#Date Created:          05-04-2023
#Date Last Modified:    05-04-2023
#
#Purpose:
#This program is a game of rock, paper, scissors between a player and the computer. 
#The game will be best two out of three, and the results will be added to a text file

import random

import os

playerWins = 0
compWins = 0



path = 'Results.txt'

class Game:
    
    def __init__(self, type):
        self.type = type

r = Game('rock')
s = Game('scissors')
p = Game('paper')

def bot():
    global option
    option = random.randint(1, 3)
    if option == 1:
        option = r
    if option == 2:
        option = s
    if option == 3:
        option = p
        
def tie():
    global output
    print('\nRound {} is a Tie!'.format(x))
    output += '\nRound {}: Tie'.format(x)
    
    
def playerWin():
    global output, playerWins
    print('\n{} wins round {}'.format(player, x))
    output += '\nRound {}: {} wins'.format(x, player)
    playerWins += 1
    
def botWin():
    global output, compWins
    print('\nComputer wins round {}'.format(x))
    output += '\nRound {}: Computer wins'.format(x)
    compWins += 1
        
print("Welcome to Rock, Paper, Scissors!\n")

player = input("Please enter your name: ").strip().capitalize()

print("Hi {}, you will be playing against the computer. Good luck!\n".format(player))


output = 'Game between the computer and {}'.format(player)



x = 1
while playerWins < 2 or compWins <2:
    bot()
    choice = input("\nMake your choice:\n\nRock\nPaper\nScissors\n\n").strip().lower()
    while not(choice == 'rock' or choice == 'paper' or choice == 'scissors'):
        choice = input('Please enter a valid option: ').strip().lower()
    if choice == 'rock':
        choice = r
    elif choice == 'paper':
        choice = p
    else:
        choice = s
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
        
    x += 1
    if playerWins == 2:
        break
    if compWins == 2:
        break

if playerWins == 2:
    output += '\nYou Won!'
    with open(path, 'w') as file:
        file.write(output)
    print('Congratulations! You Win!')
    print('You can find the results of the match in ' + os.getcwd())
elif compWins == 2:
    output += '\nOh No! You lost :('
    with open(path, 'w') as file:
        file.write(output)
    print('Tough luck. You Lost :(')
    print('\nYou can find the results of the match in ' + os.getcwd())


