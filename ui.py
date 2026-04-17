
import pygame
import score_manager

def draw_text(screen, text, x, y, size, color):
    font = pygame.font.SysFont("Rog Fonts", size, bold=False, italic=False) # Create a font and set it up.
    surface = font.render(text, True, color) # create new surface with the font created
    screen.blit(surface,(x,y))


def show_ranking(screen, score_manager):
    pass
