import pygame
import move_piece as mp
import paint_board as pb


def is_check_next_move(color,board,piece_row,piece_column,king):

    king_pos = (piece_row,piece_column)
    board[king[2]][king[1]] = None
    other_piece = board[piece_row][piece_column]
    board[piece_row][piece_column] = None

    #Verifica todo o tabuleiro por peças inimigas
    for y in range(8):
        for x in range(8): 
            piece = board[y][x]
            selected_piece = piece, x, y
            try:
                if (color != selected_piece[0][0]) and (selected_piece[0] != None) and (selected_piece[0][1] != 'king'):
                    if (selected_piece[0][1] == 'pawn'):
                        if king_pos in pawn_check(color,selected_piece):
                            board[piece_row][piece_column]=other_piece
                            board[king[2]][king[1]] = king[0]
                            return True
                    elif king_pos in mp.move_piece(selected_piece,board):
                        board[piece_row][piece_column]=other_piece
                        board[king[2]][king[1]] = king[0]
                        return True     
            except:
                pass
    board[piece_row][piece_column]=other_piece
    board[king[2]][king[1]] = king[0]
    return False

def find_king(color,board):
    king = None
    for y in range(8):
        for x in range(8): 
            piece = board[y][x]
            selected_piece = piece, x, y
            if (selected_piece[0] != None):
                if (selected_piece[0][0] == color) and (selected_piece[0][1] == 'king') :
                    king = selected_piece
    return king

def is_check(color,board):
    king = find_king(color,board)
    try:
        if is_check_next_move(color,board,king[2],king[1],king):
            return king
    except:
        pass
    return False

def verify_check_mate(color,board):
    possible_moves = []
    check_mate = True

    for y in range(8):
        for x in range(8): 
            piece = board[y][x]
            selected_piece = piece, x, y

            if (selected_piece[0] != None) and (selected_piece[0][0] == color):
                possible_moves = mp.move_piece(selected_piece,board)
                real_possible_moves = []
                for pm in possible_moves:
                    if pm[0] >= 0:
                        real_possible_moves.append(pm)
            
                for pm in real_possible_moves:
                    board[y][x] = None
                    other_piece = board[pm[0]][pm[1]]
                    board[pm[0]][pm[1]] = piece

                    if is_check(color,board) == False:
                        board[pm[0]][pm[1]] = other_piece
                        board[y][x] = piece
                        check_mate = False
                    board[pm[0]][pm[1]] = other_piece
                    board[y][x] = piece
    if check_mate:
        return True


def verify_draw(color,board):
    possible_moves = []
    draw = True
    no_more_pieces = 0

    for y in range(8):
        for x in range(8): 
            piece = board[y][x]
            selected_piece = piece, x, y

            if piece != None:
                if piece[1] != 'king' :
                    no_more_pieces += 1

            if (selected_piece[0] != None) and (selected_piece[0][0] == color):
                possible_moves = mp.move_piece(selected_piece,board)

                for pm in possible_moves:
                    board[y][x] = None
                    other_piece = board[pm[0]][pm[1]]
                    board[pm[0]][pm[1]] = piece

                    if possible_moves != []:
                        board[pm[0]][pm[1]] = other_piece
                        board[y][x] = piece
                        draw = False
                    board[pm[0]][pm[1]] = other_piece
                    board[y][x] = piece
    if draw:
        return True
    if no_more_pieces == 0:
        return True


def pawn_check(color,pawn):
    possible_moves = []
    
    if color == 'white':
        if pawn[1] > 0:
            if pawn[0][0] != color:
                possible_moves.append((pawn[2]+1,pawn[1]-1))

        if pawn[1] < 7:
            if pawn[0][0] != color:
                possible_moves.append((pawn[2]+1,pawn[1]+1))

    if color == 'black':
        if pawn[1] > 0:
            if pawn[0][0] != color:
                possible_moves.append((pawn[2]-1,pawn[1]-1))

        if pawn[1] < 7:
            if pawn[0][0] != color:
                possible_moves.append((pawn[2]-1,pawn[1]+1))

    return possible_moves

def king_verify(selected_piece, board):

            piece_column = selected_piece[1]
            piece_row = selected_piece[2]
            color, type, image, id = selected_piece[0]
            possible_moves_king = []

            #Cima
            try:
                if piece_row > 0:
                    final_pos = board[piece_row-1][piece_column]
                    possible_moves_king.append((piece_row-1,piece_column))
            except:
                pass

            #Cima direita
            try:
                if piece_row > 0 and piece_column < 7:
                    final_pos = board[piece_row-1][piece_column+1]
                    possible_moves_king.append((piece_row-1,piece_column+1))
            except:
                pass

            #Cima esquerda
            try:
                if piece_row > 0  and piece_column > 0:
                    final_pos = board[piece_row-1][piece_column-1]
                    possible_moves_king.append((piece_row-1,piece_column-1))
            except:
                pass
            
            #Esquerda
            try:
                if piece_column > 0:
                    final_pos = board[piece_row][piece_column-1]
                    possible_moves_king.append((piece_row,piece_column-1))
            except:
                pass

            #Direita
            try:
                if piece_column < 7:
                    final_pos = board[piece_row][piece_column+1]
                    possible_moves_king.append((piece_row,piece_column+1))
            except:
                pass

            #Baixo
            try:
                if piece_row < 7:
                    final_pos = board[piece_row+1][piece_column]
                    possible_moves_king.append((piece_row+1,piece_column))
            except:
                pass

            #Baixo direita
            try:
                if piece_row < 7 and piece_column < 7:
                    final_pos = board[piece_row+1][piece_column+1]
                    possible_moves_king.append((piece_row+1,piece_column+1))
            except:
                pass

            #Baixo esquerda
            try:
                if piece_row < 7 and piece_column > 0:
                    final_pos = board[piece_row+1][piece_column-1]
                    possible_moves_king.append((piece_row+1,piece_column-1))
            except:
                pass

            return possible_moves_king