import math
BIGNUMBER =1000


def Minmax(board,depth,Maximiser)
    
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

def whosturn(board):
    Xno=0
    Yno=0
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]=='X'):
                Xno+=1
            elif(board[i][j]=='O'):
                Yno+=1
            
    if(Xno>Yno):
        print("O to play next")
    else:
        print("X to play next")

def isMovesLeft(board):
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]=='_'):
                return True
    return False            

if __name__ == "__main__":  
   
    board = [['X', 'O', 'X'],  
             ['O', '_', 'O'],  
             ['O', 'O', 'X']] 
       
    value = BoardEval(board) 
    whosturn(board) 
    print(isMovesLeft(board))
    print(board)
    print("The value of this board is", value)             