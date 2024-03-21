import pygame
import check_checkmate_draw as vc

def roque(selected_piece,board,castling_short_white,castling_long_white,castling_short_black,castling_long_black,possible_moves):
    piece, x, y = selected_piece

    # roque grande brancas
    if(piece[1] == 'king' and piece[0] == 'white'):
        if (castling_long_white == True):
            if(board[7][1] == None and board[7][2] == None and board[7][3] == None):
                if (vc.is_check_next_move('white',board,7,2,selected_piece) == False and vc.is_check_next_move('white',board,7,3,selected_piece) == False):
                    possible_moves.append((7,2))
                    return possible_moves

    # roque grande pretas
    if(piece[1] == 'king' and piece[0] == 'black'):
        if(castling_long_black == True):
            if(board[0][1] == None and board[0][2] == None and board[0][3] == None):
                 if (vc.is_check_next_move('black',board,0,2,selected_piece) == False and vc.is_check_next_move('black',board,0,3,selected_piece) == False):
                    possible_moves.append((0,2))
                    return possible_moves

    # roque curto brancas
    if(piece[1] == 'king' and piece[0] == 'white'):
        if(castling_short_white == True):
            if(board[7][5] == None and board[7][6] == None ):
                if (vc.is_check_next_move('white',board,7,5,selected_piece) == False and vc.is_check_next_move('white',board,7,6,selected_piece) == False):
                    possible_moves.append((7,6))
                    return possible_moves
    
    # roque curto pretas
    if(piece[1] == 'king' and piece[0] == 'black'):
        if(castling_short_black == True):
            if(board[0][5] == None and board[0][6] == None ):
                if (vc.is_check_next_move('black',board,0,5,selected_piece) == False and vc.is_check_next_move('black',board,0,6,selected_piece) == False):
                    possible_moves.append((0,6))
                    return possible_moves


    return possible_moves