#Name:                  Dbaker4876-Final Project.py
#Author:                Derek Baker
#Date Created:          05-04-2023
#Date Last Modified:    05-04-2023
#
#Purpose:
#This program is a game of rock, paper, scissors between a player and the computer. 
#The game will be best two out of three, and the results will be added to a text file

import random

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
        
print("Welcome to Rock, Paper, Scissors!\n")

player = input("Please enter your name: ")

print("Hi {}, you will be playing against the computer. Good luck!".format(player))

playerWins = 0
compWins = 0

while playerWins < 2 or compWins <2:
    choice = input("Make your choice:\nRock\nPaper\nScissors").strip().lower()
    while not(choice == 'rock' or choice == 'paper' or choice == 'scissors'):
        choice = input('Please enter a valid option: ').strip().lower()
    if choice == 'rock':
        choice = r
    elif choice == 'paper':
        choice = p
    else:
        choice = s
    


