import pygame
import check_checkmate_draw as vc

TILESIZE = 100
BOARD_POS = (0, 0)

def paint_board(selected_piece,possible_moves,board_surf,mousedown):

    rect = pygame.Rect(selected_piece[1]*TILESIZE, selected_piece[2]*TILESIZE, TILESIZE, TILESIZE)
    #Pintar quadrados para movimentação
    if mousedown:
        pygame.draw.rect(board_surf, pygame.Color('Green'),rect)
        for pos in possible_moves:
            rect_possible_moves = pygame.Rect(pos[1]*TILESIZE, pos[0]*TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(board_surf, pygame.Color('LIGHTGREEN'),rect_possible_moves)
            
    #Voltar a cor original de cada quadrado        
    else:
        if (selected_piece[1] % 2 == 0 and selected_piece[2] % 2 == 0) or (selected_piece[1] % 2 != 0 and selected_piece[2] % 2 != 0):
            pygame.draw.rect(board_surf, pygame.Color('beige'),rect)
        else: 
            pygame.draw.rect(board_surf, pygame.Color('darkgrey'),rect)

        for pos in possible_moves:
            rect_possible_moves = pygame.Rect(pos[1]*TILESIZE, pos[0]*TILESIZE, TILESIZE, TILESIZE)
            if (pos[1] % 2 == 0 and pos[0] % 2 == 0) or (pos[1] % 2 != 0 and pos[0] % 2 != 0):
                pygame.draw.rect(board_surf, pygame.Color('beige'),rect_possible_moves)
            else: 
                pygame.draw.rect(board_surf, pygame.Color('darkgrey'),rect_possible_moves)

def paint_check(turno,board,board_surf):
    for i in range(7):
            for j in range(7):
                rect = pygame.Rect(i*TILESIZE, j*TILESIZE, TILESIZE, TILESIZE)
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    pygame.draw.rect(board_surf, pygame.Color('beige'),rect)
                else: 
                    pygame.draw.rect(board_surf, pygame.Color('darkgrey'),rect)

    king = vc.find_king(turno,board)
    if vc.is_check(turno,board) != False:
        rect = pygame.Rect(king[1]*TILESIZE, king[2]*TILESIZE, TILESIZE, TILESIZE)
        pygame.draw.rect(board_surf, pygame.Color('Red'),rect)
        

def game_over_screen(screen,clock):
    font = pygame.font.SysFont('Comic Sans MS', 70)
    font2 = pygame.font.SysFont('Comic Sans MS', 35)
    img = font.render('CHECK MATE', True, pygame.Color('RED'))
    screen.blit(img, (200, 300))
    img2 = font2.render('PRESS R TO RESTART OR Q TO QUIT', True, pygame.Color('RED'))
    screen.blit(img2, (90, 400))
    pygame.display.flip()
    clock.tick(60)

def draw_screen(screen,clock):
    font = pygame.font.SysFont('Comic Sans MS', 70)
    font2 = pygame.font.SysFont('Comic Sans MS', 35)
    img = font.render('DRAW', True, pygame.Color('RED'))
    screen.blit(img, (290, 300))
    img2 = font2.render('PRESS R TO RESTART OR Q TO QUIT', True, pygame.Color('RED'))
    screen.blit(img2, (80, 400))
    pygame.display.flip()
    clock.tick(60)

def pawn_promotion_screen(screen,clock):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    img = font.render('PRESS K FOR KNIGHT, Q FOR QUEEN,', True, pygame.Color('BLUE'))
    screen.blit(img, (100, 300))
    font2 = pygame.font.SysFont('Comic Sans MS', 30)
    img2 = font.render('PRESS B FOR BISHOP OR T FOR TOWER', True, pygame.Color('BLUE'))
    screen.blit(img2, (100, 350))
    pygame.display.flip()
    clock.tick(60)