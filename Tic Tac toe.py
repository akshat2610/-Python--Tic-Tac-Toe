# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:45:08 2018

@author: X_Reaper_X
"""

from IPython.display import clear_output

board = [[1,2,3],[4,5,6],[7,8,9]]
userChoice = ""
Player1 = {"name": "", "mark": "", "move": 0}
Player2 = {"name": "", "mark": "", "move": 0}

def printBoard():    
    clear_output()
    for i in range (0,3) :
        print(board[i][0], board[i][1], board[i][2])

def movePlayer1(): 
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j] == Player1["move"]):
                board[i][j] = Player1["mark"]
                return 1
                
def movePlayer2():
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j] == Player2["move"]):
                board[i][j] = Player2["mark"] 
                return 1
                
def win():  
    for j in range (0,3):
        if(board[j][0] == board[j][1] == board[j][2]):
            return 1
        
        if(board[0][j] == board[1][j] == board[2][j]):
            return 1
        
        if(board[0][0] == board[1][1] == board[2][2]):
            return 1
        
        if(board[0][2] == board[1][1] == board[2][0]):
            return 1
        else:
            return 0
        
def checkMark(): #USED IN mainMenu() function
    
    if (Player1["mark"].upper() == 'X' or Player1["mark"].upper() == 'O') :
        return 1
    
    else :
        return 0
       
def mainMenu():
    
    print("Welcome to TIC-TAC-TOE.\n")
    userChoice = input("Would you like to play? Yes or No\n")
    
    if (userChoice.upper() == "NO"):
        print("Thank You")
    
    else :
        
        Player1["name"] = input("What is your name? Player 1 \n")
        Player2["name"] = input("What is your name? Player 2 \n")
        Player1["mark"] = input("%s, choose X or O" %(Player1["name"]))
    
        while (checkMark()==0) :
        
            print("Invalid Choice\n")
            Player1["mark"] = input("%s, choose X or O" %(Player1["name"]))
    
        if (Player1["mark"].upper() == 'X') :
            Player2["mark"] = "O"
    
        if (Player1["mark"].upper() == 'O') :
            Player2["mark"] = "X"        
        print("INSTRUCTIONS: Enter the number you want to mark")
        print("%s, goes first" %(Player1["name"]))

def play():

    win()
    while(win()==0):
        
        printBoard()
        Player1["move"] = int(input("Choose your move %s" %(Player1["name"])))
        
        while (movePlayer1()!=1):
            
            print("Invalid move\n")
            Player1["move"] = int(input("Choose your move %s" %(Player1["name"])))
        
        printBoard()
        
        if (win()==1):
            print("Congratulations %s, you won the game" %(Player1["name"]))
            break
            
        Player2["move"] = int(input("Your turn, %s" %(Player2["name"])))
        
        while (movePlayer2()!=1):
            
            print("Invalid move\n")
            Player2["move"] = int(input("Your turn, %s" %(Player2["name"])))
            
        if (win()==1):
            print("Congratulations %s, you won the game" %(Player2["name"]))
            
            
mainMenu()
play()