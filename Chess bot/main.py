import math 
import pygame
import board_creation as bc
import move_piece as mp
import paint_board as pb
import check_checkmate_draw as vc
import pawn_promotion as pp
import roque as r
import time
import minimax
import copy
import choose_color
import Find_piece_by_id as fpbi
import board_checkmoves
from datetime import datetime

def main():
    pygame.init()
    font = pygame.font.SysFont('Comic Sans MS', 32)
    screen = pygame.display.set_mode((800, 800))
    board = bc.create_board()
    board_surf = bc.create_board_surf()
    clock = pygame.time.Clock()
    selected_piece = None
    drop_pos = None
    running = False
    choose_piece = False
    turno = 'white'
    turno_bot = None
    game_over = False
    enpassant = None
    castling_short_white = True 
    castling_long_white = True 
    castling_short_black = True 
    castling_long_black = True 
    choose_color_screen = True

    while True:
        piece, x, y = bc.get_square_under_mouse(board)
        
        for e in pygame.event.get():
            
            if e.type == pygame.QUIT:
                return

            elif e.type == pygame.MOUSEBUTTONDOWN and running == True and turno == turno_player:
                if piece != None:
                    selected_piece = piece, x, y
                    if piece[0] == turno:
                        #possible_moves = mp.move_piece(selected_piece, board)
                        possible_moves = board_checkmoves.getMoves(board, turno,x,y,0)
                        # adicionando roque nos movimentos 
                        possible_moves = r.roque(selected_piece,board,castling_short_white,castling_long_white,castling_short_black,castling_long_black, possible_moves)
                        
                        #En passant add to paint board
                        if(enpassant != None):
                            en_y, en_x = enpassant
                            if((y-1,x-1) == (en_y,en_x) or (y-1,x+1) == (en_y,en_x)):
                                possible_moves.append(enpassant)
                            if((y+1,x-1) == (en_y,en_x) or (y+1,x+1) == (en_y,en_x)):
                                possible_moves.append(enpassant)

                        pb.paint_board(selected_piece,possible_moves,board_surf,True)
                        
                    else:
                        selected_piece = None
                    
                    
            elif e.type == pygame.MOUSEBUTTONUP and running == True and turno == turno_player:
                pb.paint_check(turno,board,board_surf)
                if selected_piece != None:
                    pb.paint_board(selected_piece,possible_moves,board_surf,False)
                    if drop_pos:
                        new_x, new_y = drop_pos

                        if (drop_pos[1],drop_pos[0]) in possible_moves:
                            piece, old_x, old_y = selected_piece
                            other_piece = board[new_y][new_x]
                            board[old_y][old_x] = None
                            board[new_y][new_x] = piece

                            if(enpassant != None):
                                if((new_y, new_x) == (en_y,en_x)):
                                    if(turno == 'black'):
                                        board[en_y-1][en_x] = None
                                    else:
                                        board[en_y+1][en_x] = None

                            #Permitir en passant
                            enpassant = None
                            try:
                                if(((new_y - old_y) == 2 or (new_y - old_y) == -2) and piece[1] == 'pawn'):
                                    if(board[new_y][new_x+1] != None):
                                        if(board[new_y][new_x+1][1] == 'pawn' and board[new_y][new_x+1][0] != turno):
                                            #permitir en passant
                                            if(turno == 'black'):
                                                enpassant = (new_y-1,new_x)
                                            else:
                                                enpassant = (new_y+1,new_x)
                                if(((new_y - old_y) == 2 or (new_y - old_y) == -2) and piece[1] == 'pawn' and enpassant == None):
                                    if(board[new_y][new_x-1] != None):
                                        if(board[new_y][new_x-1][1] == 'pawn' and board[new_y][new_x-1][0] != turno):
                                            #permitir en passant
                                            if(turno == 'black'):
                                                enpassant = (new_y-1,new_x)
                                            else:
                                                enpassant = (new_y+1,new_x)
                            except:
                                pass
  
                            if vc.is_check(turno,board):
                                board[new_y][new_x] = other_piece
                                board[old_y][old_x] = piece
                                selected_piece = None
                                drop_pos = None
                                break
                             
                            pb.paint_check(turno,board,board_surf)

                            if pp.pawn_promotion(turno,new_y,piece):
                                choose_piece = True
                                running = False 

                            if turno == 'white':
                                turno = 'black'
                            else:
                                turno = 'white'

                            # fazendo o roque
                            if(piece[1] == 'king' and (old_x - new_x) == 2 and piece[0] == 'white'):
                                board[7][3] = board[7][0]
                                board[7][0] = None

                            if(piece[1] == 'king' and (old_x - new_x) == -2 and piece[0] == 'white'):
                                board[7][5] = board[7][7]
                                board[7][7] = None

                            if(piece[1] == 'king' and (old_x - new_x) == 2 and piece[0] == 'black'):
                                board[0][3] = board[0][0]
                                board[0][0] = None

                            if(piece[1] == 'king' and (old_x - new_x) == -2 and piece[0] == 'black'):
                                board[0][5] = board[0][7]
                                board[0][7] = None

                            # logica para permitir o roque
                            if(piece[1] == 'king' and piece[0] == 'white'):
                                castling_short_white = False
                                castling_long_white = False
                            if(piece[1] == 'tower' and (old_y,old_x) == (7,0) and piece[0] == 'white'):
                                castling_long_white = False
                            if(piece[1] == 'tower' and (old_y,old_x) == (7,7) and piece[0] == 'white'):
                                castling_short_white = False

                            if(piece[1] == 'king' and piece[0] == 'black'):
                                castling_short_black = False
                                castling_long_black = False
                            if(piece[1] == 'tower' and (old_y,old_x) == (0,0) and piece[0] == 'black'):
                                castling_long_black = False
                            if(piece[1] == 'tower' and (old_y,old_x) == (0,7) and piece[0] == 'black'):
                                castling_short_black = False
                        

                    selected_piece = None
                    drop_pos = None
                    pb.paint_check(turno,board,board_surf)

            # jogo parado
            elif e.type == pygame.KEYDOWN and running == False:
                if game_over:
                    if e.key == pygame.K_r:
                        main()
                        return  
                    if e.key == pygame.K_q:
                        exit()

                if choose_piece == True:
                    if e.key == pygame.K_k:
                        choose_piece = pp.choose_piece(turno,'k',board,new_y,new_x)
                        pb.paint_check(turno,board,board_surf)
                        running = True 
                    if e.key == pygame.K_q:
                        choose_piece = pp.choose_piece(turno,'q',board,new_y,new_x)
                        pb.paint_check(turno,board,board_surf)
                        running = True 
                    if e.key == pygame.K_b:
                        choose_piece = pp.choose_piece(turno,'b',board,new_y,new_x)
                        pb.paint_check(turno,board,board_surf)
                        running = True 
                    if e.key == pygame.K_t:
                        choose_piece = pp.choose_piece(turno,'t',board,new_y,new_x)
                        pb.paint_check(turno,board,board_surf)
                        running = True 

                if choose_color_screen:
                    if e.key == pygame.K_w:
                        turno_player = 'white'
                        turno_bot = 'black'
                        choose_color_screen = False
                        running = True 
                    if e.key == pygame.K_b:
                        turno_player = 'black'
                        turno_bot = 'white'
                        choose_color_screen = False
                        running = True 

        #bot move        
        if turno == turno_bot and running:
            pb.paint_check(turno,board,board_surf)
            if turno == 'black':
                bot_color = True
                player_color = 'white'
            else:
                bot_color = False
                player_color = 'black'
            board_aux = board_checkmoves.generateBoard(board,turno)

            start = datetime.now()
            best_move, eval = minimax.minimax(board_aux,4,-math.inf,math.inf,bot_color)
            print("Tempo de execução do minimax: ", datetime.now()-start)
            print("Movimento: ", best_move)
            print("Pontuação", eval)
            '''
            start = datetime.now()
            best_move, eval = minimax.minimax(board_aux,4,-math.inf,math.inf,bot_color)
            print("Tempo de execução do minimax: ", datetime.now()-start)
            print("Movimento: ", best_move)
            print("Pontuação", eval)
            '''

            old_position, bt_move = board_checkmoves.generateMove(best_move)
            print (best_move)
            if old_position==None and bt_move==None:
                running = False   
                game_over = True     
                pb.game_over_screen(screen,clock)
                continue
                #return

            old_y = old_position[0]
            old_x = old_position[1]
            new_y = bt_move[0]
            new_x = bt_move[1]

            piece = board[old_y][old_x]
            '''
            other_piece = board[new_y][new_x]
            

            if vc.is_check(turno,board):
                board[new_y][new_x] = other_piece
                board[old_y][old_x] = piece
                selected_piece = None
                drop_pos = None
            '''
            board[old_y][old_x] = None
            board[new_y][new_x] = piece

            pp.pawn_promotion_bot(turno,piece,board,new_x,new_y)
            if turno == 'white':
                turno = 'black'
            else:
                  turno = 'white'
            
            selected_piece = None
            drop_pos = None
            pb.paint_check(turno,board,board_surf)
            
        screen.fill(pygame.Color('grey'))
        screen.blit(board_surf, bc.BOARD_POS)
        bc.draw_pieces(screen, board, font, selected_piece)
        bc.draw_selector(screen, piece, x, y)
        drop_pos = bc.draw_drag(screen, board, selected_piece, font)

        if choose_piece:
            pb.pawn_promotion_screen(screen,clock)
        if choose_color_screen:
            choose_color.choose_side(screen,clock)
                
        if vc.verify_check_mate(turno,board):
            if vc.is_check(turno,board):
                running = False   
                game_over = True     
                pb.game_over_screen(screen,clock)

        if vc.verify_draw(turno,board):
            if vc.is_check(turno,board) == False:
                running = False
                game_over = True 
                pb.draw_screen(screen,clock)

        
        pygame.display.flip()
        clock.tick(60)
    
if __name__ == '__main__':
    main()
