#Implementation of Tic-Tac-Toe using the Minimax algortihm without alpha beta pruning

import math
import numpy as np

BIGNUMBER =1000
global move_x
global move_y
global depth


def BoardEval(board):
    for i in range(0,3):#check for all rows
        if((board[i][0]==board[i][1]) and (board[i][0]==board[i][2])):
            if((board[i][0])=='X'):
                return 10
            elif ((board[i][0])=='O'):
                return -10

    for j in range(0,3):#check for all columns
        if((board[0][j]==board[1][j]) and (board[0][j]==board[2][j])):
            if((board[0][j])=='X'):
                return 10
            elif ((board[0][j])=='O'):
                return -10
                

    if((board[0][0]==board[1][1]) and (board[0][0]==board[2][2])): #Check for Diagonals
            if((board[0][0])=='X'):
                return 10
            elif ((board[0][0])=='O'):
                return -10
    
    if((board[2][0]==board[1][1]) and (board[2][0]==board[0][2])):
            if((board[2][0])=='X'):
                return 10
            elif ((board[2][0])=='O'):
                return -10

    if(MovesLeft==False):
        return 0   
  
 
def MovesLeft(board):
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]=='_'):
                return True
    return False            

def Minmax(board,depth,Maximiser):
    score=BoardEval(board)
    
    if (score == 10):
        return score
    if (score == -10):
        return score
    if (MovesLeft(board)==False): 
        return 0;   
    if(Maximiser==True): #Maximiser
        best_score=-BIGNUMBER
        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j]=='_'):
                    board[i][j] = 'X'; 
                    best_score=max(Minmax(board, depth+1,False),best_score)
                    board[i][j] = '_'; # check to see what happens
        return best_score

    elif(Maximiser==False): #minimiser
        best_score=BIGNUMBER
        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j]=='_'):
                    board[i][j] = 'O'; 
                    best_score=min(Minmax(board, depth+1,True),best_score) #check to see if this should be true
                    board[i][j] = '_'; # check to see what happens
        return best_score    

def optimalmove(): #to be made by Comp. Maxmiser
    best_score=-BIGNUMBER
    if(MovesLeft(board)):
        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j]=='_'):
                    board[i][j]='X'
                    '''
                    best_score=max(Minmax(board,0,False),best_score)
                    board[i][j]='_'
                    move_x=i
                    move_y=j
                    
                    '''
                    score=Minmax(board,0,False)
                    board[i][j]='_'
                    if(score>best_score):
                        best_score=score
                        move_x=i
                        move_y=j
                    
                        

        board[move_x][move_y]='X'
        print("after comp played \n")
        printboard(board)

    #update player stste?                
 
def printboard(board):
    matrix = np.array(board)
    print(matrix)
     
if __name__ == "__main__":  
   
    board = [['_', '_', '_'],  
             ['_', '_', '_'],  
             ['_', '_', '_']] 

    demo_board=[['1', '2', '3'],  
                ['4', '5', '6'],  
                ['7', '8', '9']]   

    print("You are 'O' computer is 'X' choose your position as per the table")
    printboard(demo_board)
    while(MovesLeft(board)):       
        if(BoardEval(board)==10):
            print("X has won")
            break
        elif(BoardEval(board)==-10):
            print("O has won")
            break
        read_val=input()
        if(read_val==1 and board[0][0]=='_'):
            board[0][0]='O'
            printboard(board)
            optimalmove()
        elif(read_val==2 and board[0][1]=='_'):
            board[0][1]='O'
            printboard(board)
            optimalmove()
        elif(read_val==3 and board[0][2]=='_'):
            board[0][2]='O'
            printboard(board)
            optimalmove()     
        elif(read_val==4 and board[1][0]=='_'):
            board[1][0]='O'
            printboard(board)
            optimalmove() 
        elif(read_val==5 and board[1][1]=='_'):
            board[1][1]='O'
            printboard(board)
            optimalmove()
        elif(read_val==6 and board[1][2]=='_'):
            board[1][2]='O'
            printboard(board)
            optimalmove()
        elif(read_val==7 and board[2][0]=='_'):
            board[2][0]='O'
            printboard(board)
            optimalmove()
        elif(read_val==8 and board[2][1]=='_'):
            board[2][1]='O'
            printboard(board)
            optimalmove()
        elif(read_val==9 and board[2][2]=='_'):
            board[2][2]='O'
            printboard(board)
            optimalmove()
        elif(read_val>=10):
            break
    
        

                 
