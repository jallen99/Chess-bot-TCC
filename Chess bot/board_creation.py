import pygame
from pygame import color
from pygame.constants import NOFRAME
import count_piece as cp

TILESIZE = 100
BOARD_POS = (0, 0)

def create_board_surf():
    board_surf = pygame.Surface((TILESIZE*8, TILESIZE*8))
    dark = False
    for y in range(8):
        for x in range(8):
            rect = pygame.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(board_surf, pygame.Color('darkgrey' if dark else 'beige'), rect)
            dark = not dark
        dark = not dark
    return board_surf

def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - BOARD_POS
    x, y = [int(v // TILESIZE) for v in mouse_pos]
    try: 
        if x >= 0 and y >= 0: return (board[y][x], x, y)
    except IndexError: pass
    return None, None, None

def create_board():
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(None)
    
    for x in range(0, 8):
        board[1][x] = ('black', 'pawn',r"Images\Pawn_B.png",x)
    for x in range(0, 8):
        board[6][x] = ('white', 'pawn', r"Images\Pawn_W.png",x+7)
        
    board[7][0] = ('white', 'tower', r"Images\Tower_W.png",16)
    board[7][7] = ('white', 'tower', r"Images\Tower_W.png",17)
    board[7][1] = ('white', 'knight', r"Images\Knight_W.png",18)
    board[7][6] = ('white', 'knight', r"Images\Knight_W.png",19)
    board[7][2] = ('white', 'bishop', r"Images\Bishop_W.png",20)
    board[7][5] = ('white', 'bishop', r"Images\Bishop_W.png",21)
    board[7][3] = ('white', 'queen', r"Images\Queen_W.png",22)
    board[7][4] = ('white', 'king', r"Images\King_W.png",23)
    
    board[0][0] = ('black', 'tower', r"Images\Tower_B.png",24)
    board[0][7] = ('black', 'tower', r"Images\Tower_B.png",25)
    board[0][1] = ('black', 'knight', r"Images\Knight_B.png",26)
    board[0][6] = ('black', 'knight', r"Images\Knight_B.png",27)
    board[0][2] = ('black', 'bishop', r"Images\Bishop_B.png",28)
    board[0][5] = ('black', 'bishop', r"Images\Bishop_B.png",29)
    board[0][3] = ('black', 'queen', r"Images\Queen_B.png",30)
    board[0][4] = ('black', 'king', r"Images\King_B.png",31)
    cp.count_piece(board)
    
    #Promoção do peão
    '''
    board[1][1] = ('white', 'pawn', r"Images\Pawn_W.png",0)
    board[7][4] = ('white', 'king', r"Images\King_W.png",0)
    board[0][4] = ('black', 'king', r"Images\King_B.png",0)
    '''

    #Empate Afogamento
    '''
    board[3][7] = ('white', 'tower', r"Images\Tower_W.png",0)
    board[5][1] = ('white', 'tower', r"Images\Tower_W.png",0)
    board[7][4] = ('white', 'king', r"Images\King_W.png",0)
    board[4][0] = ('black', 'king', r"Images\King_B.png",0)
    '''
    
    #Empate 
    '''
    board[2][3] = ('black', 'pawn',r"Images\Pawn_B.png",0)
    board[3][4] = ('white', 'pawn',r"Images\Pawn_W.png",1)
    board[7][4] = ('white', 'king', r"Images\King_W.png",2)
    board[0][4] = ('black', 'king', r"Images\King_B.png",3)
    '''

    return board

def draw_pieces(screen, board, font, selected_piece):
    sx, sy = None, None
    if selected_piece:
        piece, sx, sy = selected_piece

    for y in range(8):
        for x in range(8): 
            piece = board[y][x]
            if piece:
                s1 = None
                selected = x == sx and y == sy
                color, type, image, id = piece
                s1 = pygame.image.load(image)
                pos = pygame.Rect(BOARD_POS[0] + x * TILESIZE+1, BOARD_POS[1] + y * TILESIZE + 1, TILESIZE, TILESIZE)
                screen.blit(s1, s1.get_rect(center=pos.center))

def draw_selector(screen, piece, x, y):
    if piece != None:
        rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
        pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)

def draw_drag(screen, board, selected_piece, font):
    if selected_piece:
        if selected_piece[0] != 0:
            piece, x, y = get_square_under_mouse(board)
            if x != None:
                rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
                pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)
            color, type, image, id = selected_piece[0]
            s1 = pygame.image.load(image)
            pos = pygame.Vector2(pygame.mouse.get_pos())
            screen.blit(s1, s1.get_rect(center=pos))
            selected_rect = pygame.Rect(BOARD_POS[0] + selected_piece[1] * TILESIZE, BOARD_POS[1] + selected_piece[2] * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.line(screen, pygame.Color('red'), selected_rect.center, pos)
            return (x, y)    