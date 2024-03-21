import pygame

def pawn_promotion(turno,new_y,piece):

    if piece[1] == 'pawn':

        if turno == 'white' and new_y == 0:
            return True
        elif turno == 'black' and new_y == 7:
            return True

    return False

def choose_piece(turno,key,board,new_y,new_x):
    
    if key == 'k':
        if turno == 'black':
            board[new_y][new_x] = None
            board[new_y][new_x] = ('white', 'knight', r"Images\Knight_W.png",8)
        else:
            board[new_y][new_x] = None
            board[new_y][new_x] = ('black', 'knight', r"Images\Knight_B.png",8)

    elif key == 'q':
        if turno == 'black':
            board[new_y][new_x] = None
            board[new_y][new_x] = ('white', 'queen', r"Images\Queen_W.png",8)
        else:
            board[new_y][new_x] = None
            board[new_y][new_x] = ('black', 'queen', r"Images\Queen_B.png",8)
            
    elif key == 'b':
        if turno == 'black':
            board[new_y][new_x] = None
            board[new_y][new_x] = ('white', 'bishop', r"Images\Bishop_W.png",8)
        else:
            board[new_y][new_x] = None
            board[new_y][new_x] = ('black', 'bishop', r"Images\Bishop_B.png",8)
    elif key == 't':
        if turno == 'black':
            board[new_y][new_x] = None
            board[new_y][new_x] = ('white', 'tower', r"Images\Tower_W.png",8)
        else:
            board[new_y][new_x] = None
            board[new_y][new_x] = ('black', 'tower', r"Images\Tower_B.png",8)
    return False

def pawn_promotion_bot(turno,piece,board,new_x,new_y):
    if piece==None: return False
    aux = 0
    if piece[1] == 'pawn':
        if board[new_y][new_x] != None and board[new_y][new_x][1]!='pawn':
            aux = new_x
            new_x = new_y
            new_y = aux            
        if turno == 'white' and new_y == 0:
            board[new_y][new_x] = None
            board[new_y][new_x] = ('white', 'queen', r"Images\Queen_W.png",8)
            return True
            
        elif turno == 'black' and new_y == 7:
            board[new_y][new_x] = None
            board[new_y][new_x] = ('black', 'queen', r"Images\Queen_B.png",8)
            return True

    return False