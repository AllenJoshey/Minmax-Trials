import numpy as np

board=[['_','X','_'],['_','O','_'],['_','_','_']]
inputval=-10;
while(inputval!=10):
    read_val=input()
    if(read_val==0):
        board[0][0]='O'
        print(board)
    elif(read_val==1):
        board[0][1]='O'
        print(board)
    elif(read_val==2):
        board[0][2]='O'
        print(board)     
    elif(read_val==3):
        board[1][0]='O'
        print(board) 
    elif(read_val==4):
        board[1][1]='O'
        print(board)
    elif(read_val==5):
        board[1][2]='O'
        print(board)
    elif(read_val==6):
        board[2][0]='O'
        print(board)
    elif(read_val==7):
        board[2][1]='O'
        print(board)
    elif(read_val==8):
        board[2][2]='O'
        print(board)
    elif(read_val>=9): 
        break;

def printboard(board):
    matrix = np.array(board)
    print(matrix)
     
     

printboard(board)     

          
