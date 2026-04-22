
import pygame
import score_manager
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def draw_text(screen, text, align, x, y, size, color):
    # Create font object used to render text
    font = pygame.font.SysFont("Rog Fonts", size)

    # Convert text into a drawable surface
    surface = font.render(text, True, color)

    # Get rectangle that defines size and position of the text surface
    rect = surface.get_rect()

    # Position the text based on alignment type
    if align == "topright":
        rect.topright = (x, y)   # anchor top-right corner at (x, y)
    elif align == "center":
        rect.center = (x, y)     # anchor center of text at (x, y)

    # Draw the text surface onto the screen
    screen.blit(surface, rect)


def show_ranking(screen, score_manager):
    pass
