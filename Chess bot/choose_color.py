import pygame

def choose_side(screen,clock):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    img = font.render('PRESS W TO PLAY WITH THE WHITE', True, pygame.Color('BLUE'))
    screen.blit(img, (120, 300))
    font2 = pygame.font.SysFont('Comic Sans MS', 30)
    img2 = font.render('PRESS B TO PLAY WITH THE BLACK', True, pygame.Color('BLUE'))
    screen.blit(img2, (120, 350))
    pygame.display.flip()
    clock.tick(60)