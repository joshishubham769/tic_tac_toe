"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

lst_k=[]
lst_boards=[]

i=0

#file=None
class InvalidMove(Exception):
    print("The move is invalid")
    #pass

def open_file():
    file = open(r"test.txt","w")
    
def close_file():
    file.close()
def get_key(board):
    key=0
    for row in board:
        for cell in row:
            if cell==X:
                key=key+1
            elif cell==O:
                key=key+2
            key=key*10
    return key

        
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    o=0;x=0;
    
    for i in board:
        for j in i:
            if j==O:
                o=o+1
            elif j==X:
                x=x+1
    #print(o,x)
    if o<x:
        return O
    else:
        return X


def actions(board):#barabar
    s=set()
    
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==EMPTY:
                s.add((i,j))

    return s
            
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError


def result(board, action):
    #m=board
    #print('Player',player(board))
    #print('Action',action)
    if board[action[0]][action[1]]!=EMPTY:
        raise InvalidMove
    t_board=copy.deepcopy(board)
    if board[action[0]][action[1]]==EMPTY:
        t_board[action[0]][action[1]]=player(t_board)
        return t_board
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    s=utility(board)
    #print('utility',s)
    if s==1:
        return X
    elif s==-1:
        return O
    else:
        return None
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError

def if_winner(board):

    for i in range(0,3):
        flag=True
        e=board[i][0]
        for j in range(0,3):
            if board[i][j]!=e:
                flag=False
        if flag:
            return e
            
    for i in range(0,3):
        flag=True
        e=board[0][i]
        for j in range(0,3):
            if board[j][i]!=e:
                flag=False
        if flag:
            return e
            
    if board[0][0]==board[1][1]==board[2][2]:
        return board[1][1]
        
    if board[2][0]==board[1][1]==board[0][2]:
        return board[1][1]
        
    return None
    
def terminal(board):
    
    if if_winner(board)!=None:
        return True
        
    flag=True
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==EMPTY:
                flag=False
                
    return flag
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError


def utility(board):
    
    e=if_winner(board)
    
    if e==O:
        return -1
    elif e==X:
        return 1
    else:
        return 0

    
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError


def minimax(board):
    
    
    if terminal(board):
        return utility(board),None

    else:
        
        pl=player(board)
        actns=actions(board)
        
        mn=1000
        mx=-1000
        tpx=None
        tpn=None
        #print(board)
        #print(actns)
        
        for actn in actns:
            #print('Board ',board)
            t_board=result(board,actn)
            lst=[]
            k=0
            
            if terminal(t_board):
                return utility(t_board),actn
                
            
            k=minimax(t_board)[0]
            
            #print(lst,"LAYERS-",layer)
            if k>mx:
                mx=k
                tpx=actn
                
            if k<mn:
                mn=k
                tpn=actn

        #print('tpx',tpx,'tpn',tpn)
    
        if pl==X:
            return mx,tpx
        elif pl==O:
            return mn,tpn
            










        
    
