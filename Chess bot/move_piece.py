import pygame
import check_checkmate_draw as vc

def move_piece(selected_piece, board):
        piece_column = selected_piece[1]
        piece_row = selected_piece[2]
        color, type, image, id = selected_piece[0]
        possible_moves = []
        
        if type == 'tower' or type == 'queen':       
            #esquerda pra direita
            for coluna in range(piece_column+1,8):
                if board[piece_row][coluna] == None:
                    possible_moves.append((piece_row,coluna))
                elif board[piece_row][coluna][0] != color:
                    possible_moves.append((piece_row,coluna))
                    break
                elif board[piece_row][coluna][0] == color:
                    break
                
            #direita pra esquerda
            for coluna in range(piece_column-1,-1,-1):
                if board[piece_row][coluna] == None:
                    possible_moves.append((piece_row,coluna))
                elif board[piece_row][coluna][0] != color:
                    possible_moves.append((piece_row,coluna))
                    break
                elif board[piece_row][coluna][0] == color:
                    break
            #pra baixo
            for linha in range(piece_row+1,8):
              if board[linha][piece_column] == None:
                  possible_moves.append((linha,piece_column))
              elif board[linha][piece_column][0] != color:
                  possible_moves.append((linha,piece_column))
                  break
              elif board[linha][piece_column][0] == color:
                  break
            #pra cima
            for linha in range(piece_row-1,-1,-1):              
              if board[linha][piece_column] == None:
                  possible_moves.append((linha,piece_column))
              elif board[linha][piece_column][0] != color:
                  possible_moves.append((linha,piece_column))
                  break
              elif board[linha][piece_column][0] == color: 
                  break
                
        if type == 'bishop' or type == 'queen':
            for column in range(piece_column+1,8):
                if piece_row+(column-piece_column) <= 7:
                    if board[piece_row+(column-piece_column)][column] == None:
                        possible_moves.append((piece_row+(column-piece_column),column))
                    elif board[piece_row+(column-piece_column)][column][0] != color:
                        possible_moves.append((piece_row+(column-piece_column),column))
                        break
                    elif board[piece_row+(column-piece_column)][column][0] == color:
                        break


            for column in range(piece_column+1,8):
                if piece_row-(column-piece_column) <= 7:
                    if board[piece_row-(column-piece_column)][column] == None:
                        possible_moves.append((piece_row-(column-piece_column),column))
                    elif board[piece_row-(column-piece_column)][column][0] != color:
                        possible_moves.append((piece_row-(column-piece_column),column))
                        break
                    elif board[piece_row-(column-piece_column)][column][0] == color:
                        break

            for column in range(piece_column-1,-1,-1):
                if piece_row-(piece_column-column) >= 0:
                    if board[piece_row+(column-piece_column)][column] == None:
                        possible_moves.append((piece_row+(column-piece_column),column))
                    elif board[piece_row+(column-piece_column)][column][0] !=color:
                        possible_moves.append((piece_row+(column-piece_column),column))
                        break
                    elif board[piece_row+(column-piece_column)][column][0] ==color:
                        break

            for column in range(piece_column-1,-1,-1):
                if piece_row+(piece_column-column) <= 7:
                    if board[piece_row-(column-piece_column)][column] == None:
                        possible_moves.append((piece_row-(column-piece_column),column))
                    elif board[piece_row-(column-piece_column)][column][0] !=color:
                        possible_moves.append((piece_row-(column-piece_column),column))
                        break
                    elif board[piece_row-(column-piece_column)][column][0] ==color:
                        break

        
        if type == 'pawn' and color == 'black':
            # Primeira movimentação
            if piece_row == 1:
                if board[piece_row+1][piece_column] == None:
                    possible_moves.append((piece_row+1,piece_column))
                    if board[piece_row+2][piece_column] == None:
                        possible_moves.append((piece_row+2,piece_column))
            else:
                try:
                    # Movimentação padrão
                    if board[piece_row+1][piece_column] == None:
                        possible_moves.append((piece_row+1,piece_column))
                    if piece_column > 0:
                        capture_left = board[piece_row+1][piece_column-1]
                        if capture_left != None:
                            if capture_left[0] == 'white':
                                possible_moves.append((piece_row+1,piece_column-1))

                    if piece_column < 7:
                        capture_right = board[piece_row+1][piece_column+1]
                        if capture_right != None:
                            if capture_right[0] == 'white':
                                possible_moves.append((piece_row+1,piece_column+1))
                except:
                    pass


        if type == 'pawn' and color == 'white':
            # Primeira movimentação
            if piece_row == 6:
                if board[piece_row-1][piece_column] == None:
                    possible_moves.append((piece_row-1,piece_column))
                    if board[piece_row-2][piece_column] == None:
                        possible_moves.append((piece_row-2,piece_column))
                        
            else:
                # Movimentação padrão
                if board[piece_row-1][piece_column] == None:
                    possible_moves.append((piece_row-1,piece_column))

            if piece_column > 0:
                capture_left = board[piece_row-1][piece_column-1]
                if capture_left != None:
                    if capture_left[0] == 'black':
                        possible_moves.append((piece_row-1,piece_column-1))
            if piece_column < 7:
                capture_right = board[piece_row-1][piece_column+1]
                if capture_right != None:
                    if capture_right[0] == 'black':
                        possible_moves.append((piece_row-1,piece_column+1))

        # Movimento do cavalo                    
        if type == 'knight' : 
            #Cima direita
            if color == 'white':
                try:
                    final_pos = board[piece_row-2][piece_column+1]
                    if final_pos == None or final_pos[0] == 'black':
                        possible_moves.append((piece_row-2,piece_column+1))
                except:
                    pass
            if color == 'black':
                try:
                    final_pos = board[piece_row-2][piece_column+1]
                    if final_pos == None or final_pos[0] == 'white':
                        possible_moves.append((piece_row-2,piece_column+1))
                except:
                    pass

            #Cima esquerda
            if color == 'white':
                try:
                    final_pos = board[piece_row-2][piece_column-1]
                    if final_pos == None or final_pos[0] == 'black':
                        possible_moves.append((piece_row-2,piece_column-1))
                except:
                    pass
            if color == 'black':
                try:
                    final_pos = board[piece_row-2][piece_column-1]
                    if final_pos == None or final_pos[0] == 'white':
                        possible_moves.append((piece_row-2,piece_column-1))
                except:
                    pass

            #Direita cima
            if color == 'white':
                try:
                    final_pos = board[piece_row-1][piece_column+2]
                    if final_pos == None or final_pos[0] == 'black':
                        possible_moves.append((piece_row-1,piece_column+2))
                except:
                    pass
            if color == 'black':
                try:
                    final_pos = board[piece_row-1][piece_column+2]
                    if final_pos == None or final_pos[0] == 'white':
                        possible_moves.append((piece_row-1,piece_column+2))
                except:
                    pass
                
            #Direita baixo
            if color == 'white':
                try:
                    final_pos = board[piece_row+1][piece_column+2]
                    if final_pos == None or final_pos[0] == 'black':
                        possible_moves.append((piece_row+1,piece_column+2))
                except:
                    pass
            if color == 'black':
                try:
                    final_pos = board[piece_row+1][piece_column+2]
                    if final_pos == None or final_pos[0] == 'white':
                        possible_moves.append((piece_row+1,piece_column+2))
                except:
                    pass

            #Esquerda cima
            if color == 'white':
                try:
                    final_pos = board[piece_row-1][piece_column-2]
                    if final_pos == None or final_pos[0] == 'black':
                        possible_moves.append((piece_row-1,piece_column-2))
                except:
                    pass
            if color == 'black':
                try:
                    final_pos = board[piece_row-1][piece_column-2]
                    if final_pos == None or final_pos[0] == 'white':
                        possible_moves.append((piece_row-1,piece_column-2))
                except:
                    pass

            #Esquerda baixo
            if color == 'white':
                try:
                    final_pos = board[piece_row+1][piece_column-2]
                    if final_pos == None or final_pos[0] == 'black':
                        possible_moves.append((piece_row+1,piece_column-2))
                except:
                    pass
            if color == 'black':
                try:
                    final_pos = board[piece_row+1][piece_column-2]
                    if final_pos == None or final_pos[0] == 'white':
                        possible_moves.append((piece_row+1,piece_column-2))
                except:
                    pass

            #Baixo direita
            if color == 'white':
                try:
                    final_pos = board[piece_row+2][piece_column+1]
                    if final_pos == None or final_pos[0] == 'black':
                        possible_moves.append((piece_row+2,piece_column+1))
                except:
                    pass
            if color == 'black':
                try:
                    final_pos = board[piece_row+2][piece_column+1]
                    if final_pos == None or final_pos[0] == 'white':
                        possible_moves.append((piece_row+2,piece_column+1))
                except:
                    pass

            #Baixo esquerda
            if color == 'white':
                try:
                    final_pos = board[piece_row+2][piece_column-1]
                    if final_pos == None or final_pos[0] == 'black':
                        possible_moves.append((piece_row+2,piece_column-1))
                except:
                    pass
            if color == 'black':
                try:
                    final_pos = board[piece_row+2][piece_column-1]
                    if final_pos == None or final_pos[0] == 'white':
                        possible_moves.append((piece_row+2,piece_column-1))
                except:
                    pass

        #Movimentação do Rei
        if type == 'king':

            #Cima
            try:
                if piece_row > 0:
                    final_pos = board[piece_row-1][piece_column]
                    if final_pos == None or (color == 'black' and final_pos[0] == 'white') or (color == 'white' and final_pos[0] == 'black'):
                        if vc.is_check_next_move(color,board,piece_row-1,piece_column,selected_piece) == False: 
                            possible_moves.append((piece_row-1,piece_column))
            except:
                pass
                
            #Cima esquerda
            try:
                if piece_row > 0  and piece_column > 0:
                    final_pos = board[piece_row-1][piece_column-1]
                    if final_pos == None or (color == 'black' and final_pos[0] == 'white') or (color == 'white' and final_pos[0] == 'black'):
                        if vc.is_check_next_move(color,board,piece_row-1,piece_column-1,selected_piece) == False:
                            possible_moves.append((piece_row-1,piece_column-1))
            except:
                pass

            #Cima direita
            try:
                if piece_row > 0 and piece_column < 7:
                    final_pos = board[piece_row-1][piece_column+1]
                    if final_pos == None or (color == 'black' and final_pos[0] == 'white') or (color == 'white' and final_pos[0] == 'black'):
                        if vc.is_check_next_move(color,board,piece_row-1,piece_column+1,selected_piece) == False:
                            possible_moves.append((piece_row-1,piece_column+1))
            except:
                pass

            #Esquerda
            try:
                if piece_column > 0:
                    final_pos = board[piece_row][piece_column-1]
                    if final_pos == None or (color == 'black' and final_pos[0] == 'white') or (color == 'white' and final_pos[0] == 'black'):
                        if vc.is_check_next_move(color,board,piece_row,piece_column-1,selected_piece) == False:
                            possible_moves.append((piece_row,piece_column-1))
            except:
                pass

            #Direita
            try:
                if piece_column < 7:
                    final_pos = board[piece_row][piece_column+1]
                    if final_pos == None or (color == 'black' and final_pos[0] == 'white') or (color == 'white' and final_pos[0] == 'black'):
                        if vc.is_check_next_move(color,board,piece_row,piece_column+1,selected_piece) == False:
                            possible_moves.append((piece_row,piece_column+1))
            except:
                pass

            #Baixo
            try:
                if piece_row < 7:
                    final_pos = board[piece_row+1][piece_column]
                    if final_pos == None or (color == 'black' and final_pos[0] == 'white') or (color == 'white' and final_pos[0] == 'black'):
                        if vc.is_check_next_move(color,board,piece_row+1,piece_column,selected_piece) == False:
                            possible_moves.append((piece_row+1,piece_column))
            except:
                pass

            #Baixo direita
            try:
                if piece_row < 7 and piece_column < 7:
                    final_pos = board[piece_row+1][piece_column+1]
                    if final_pos == None or (color == 'black' and final_pos[0] == 'white') or (color == 'white' and final_pos[0] == 'black'):
                        if vc.is_check_next_move(color,board,piece_row+1,piece_column+1,selected_piece) == False:
                            possible_moves.append((piece_row+1,piece_column+1))
            except:
                pass

            #Baixo esquerda
            try:
                if piece_row < 7 and piece_column > 0:
                    final_pos = board[piece_row+1][piece_column-1]
                    if final_pos == None or (color == 'black' and final_pos[0] == 'white') or (color == 'white' and final_pos[0] == 'black'):
                        if vc.is_check_next_move(color,board,piece_row+1,piece_column-1,selected_piece) == False:
                            possible_moves.append((piece_row+1,piece_column-1))
            except:
                pass

            for y in range(selected_piece[1]-2,selected_piece[1]+6):
                for x in range(selected_piece[2]-2,selected_piece[2]+3):
                    try:
                        if x >= 0 and y >= 0:
                            if board[x][y][1] == 'king' and board[x][y][0] != color:
                                king_2 = board[x][y],y,x
                                king_2_move = vc.king_verify(king_2,board)
                                for king_mv in king_2_move:
                                    if king_mv in possible_moves:
                                        possible_moves.remove(king_mv)
                    except:
                        continue

        return possible_moves
