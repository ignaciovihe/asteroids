import pygame
import sys
from ui import *
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score_manager import ScoreManager
from game_state import GameState

def handle_game_over(event, name, state):
    
    if event.type != pygame.KEYDOWN:
        return name, state
    if event.key == pygame.K_RETURN:
        state = GameState.ENTER_NAME
    return name, state

def handle_enter_name(event, name, state, score_manager): 

    if event.type != pygame.KEYDOWN:
        return name, state
    
    if event.unicode.isprintable():
        name += event.unicode
    elif event.key == pygame.K_BACKSPACE:
        if name:
            name = name[0:-1]
    elif event.key == pygame.K_RETURN:
        score_manager.save(name)
        state = GameState.DISPLAY_SCORE
        sys.exit()
    return name, state


def main():
    # Initialize Pygame (loads internal modules and prepares everything)
    pygame.init()

    # Create the game window with defined width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # Create a Clock object to track time and control FPS
    clock = pygame.time.Clock()

    # Delta time (time since last frame), initialized to 0
    dt = 0

    # Create groups of sprites
    updatable = pygame.sprite.Group()   #this will hold all the objects that can be updated
    drawable = pygame.sprite.Group()    #this will hold all the objects that can be drawn
    asteroids = pygame.sprite.Group()   #this will hold all the objects asteoids
    shots = pygame.sprite.Group()       #this will hold all the objects shots

    Player.containers = (updatable, drawable) # Create a class attribute with the two groups the Player will be added to
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Create the player sprite at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Create the asteroid field sprite
    asteroids_field = AsteroidField()

    #Create the ScoreManager
    score_manager = ScoreManager()


    # Print initial information to the console for debugging
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    

    # Variable to control the main game loop
    running = True

    # Variable to control the state of the game
    state = GameState.PLAYING

    # The name of the player
    name = ""

    # Main game loop (each iteration = 1 frame)
    while running:
        # Call a function to log or display the current game state
        log_state()

        # 1. Handle events (keyboard, mouse, window close, etc.)
        # Check all events that have happened since the last frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if state == GameState.GAME_OVER:
                name, state = handle_game_over(event, name, state)

            elif state == GameState.ENTER_NAME:
                name, state = handle_enter_name(event, name, state, score_manager)
            

        
        # 2. Update game logic (move player, update asteroids, check collisions, etc.)
        #pass
        #player.update(dt) <-- Previous step withot groups
        updatable.update(dt)


        if state == GameState.PLAYING:
            for object in asteroids: # check collisions between player and asteroids
                if player.collides_with(object):
                    log_event("player_hit")
                    state = GameState.GAME_OVER

        if state == GameState.PLAYING:
            for object in asteroids: # check collisions between shots and asteroids
                for shot in shots:
                    if shot.collides_with(object):
                        log_event("asteroid_shot")
                        score_manager.sum_points(object)
                        shot.kill() #It removes the "killed" object from all of its groups so that the engine stops updating and drawing it.
                        object.split()

        # 3. Draw everything on the screen (background, player, asteroids, etc.)
        # Fill the entire screen with black
        screen.fill("black")

        if state == GameState.PLAYING:
            #Draw de player as a triangle.
            #player.draw(screen) <-- Previous step withot groups
            for sprite in drawable: # we call draw() for every sprite within the group drawable.
                sprite.draw(screen)  
                                    # We cannot use drawable.draw() because Group.draw() does not call each sprite's draw() method.
            draw_text(screen, f"SCORE: {score_manager.get_score()}", "topright", SCREEN_WIDTH - 10, 10, 27, pygame.Color("blue"))

        if state == GameState.GAME_OVER:
            score = f"SCORE: {score_manager.get_score()}"
            draw_text(screen, "GAME OVER", "center", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 10, 37, pygame.Color("blue"))
            draw_text(screen, score, "center",SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10, 27, pygame.Color("blue"))
            draw_text(screen, "Press ENTER to continue", "center",SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30, 27, pygame.Color("blue"))

        if state == GameState.ENTER_NAME:
            draw_text(screen, "ENTER YOUR NAME:", "center", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 10, 37, pygame.Color("blue"))
            draw_text(screen, name, "center",SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10, 27, pygame.Color("blue"))

            

        # Update the display to show everything we just drew
        pygame.display.flip()

        # if state == GameState.GAME_OVER:
        #     name = input("Enter your name:")
        #     score_manager.save(name)
        #     sys.exit()

        # 4. Control FPS
        miliseconds = clock.tick(60) # Time (in ms) of the last frame; limits the game to 60 FPS
        dt = miliseconds / 1000 # Delta time in seconds since the last frame



if __name__ == "__main__":
    main()
