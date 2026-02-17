import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    # Initialize Pygame (loads internal modules and prepares everything)
    pygame.init()

    # Create the game window with defined width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # Print initial information to the console for debugging
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Variable to control the main game loop
    running = True

    # Main game loop (each iteration = 1 frame)
    while running:
        # Call a function to log or display the current game state
        log_state()

        # Check all events that have happened since the last frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill the entire screen with black
        screen.fill("black")

        # Update the display to show everything we just drew
        pygame.display.flip()


if __name__ == "__main__":
    main()
