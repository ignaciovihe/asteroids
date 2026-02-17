import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    # Initialize Pygame (loads internal modules and prepares everything)
    pygame.init()

    # Create the game window with defined width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # Create a Clock object to track time and control FPS
    clock = pygame.time.Clock()

    # Delta time (time since last frame), initialized to 0
    dt = 0

    # Create the player sprite at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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

        # 1. Handle events (keyboard, mouse, window close, etc.)
        # Check all events that have happened since the last frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # 2. Update game logic (move player, update asteroids, check collisions, etc.)
        #pass

        # 3. Draw everything on the screen (background, player, asteroids, etc.)
        # Fill the entire screen with black
        screen.fill("black")

        #Draw de player as a triangle.
        player.draw(screen)

        # Update the display to show everything we just drew
        pygame.display.flip()


        # 4. Control FPS
        miliseconds = clock.tick(60) # Time (in ms) of the last frame; limits the game to 60 FPS
        dt = miliseconds / 1000 # Delta time in seconds since the last frame



if __name__ == "__main__":
    main()
