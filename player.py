from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape
import pygame

#Base class for the player
class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
 
    def triangle(self):
        """
        Calculate the three vertices of a triangular sprite (e.g., a ship) 
        based on its current position, rotation, and radius.
        
        Returns:
            list of pygame.Vector2: [tip, base_left, base_right]
        """
        
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)


    def rotate(self, dt):
        """
        Rotates the player based on elapsed time.

        Args:
            dt (float): Time passed since the last frame (in seconds).

        Returns:
            None: This method updates the player's rotation in place.
        """
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt):
        """
        Move the player based on elapsed time.

        Args:
            dt (float): Time passed since the last frame (in seconds).

        Returns:
            None: This method updates the player's position in place.
        """
        unit_vector = pygame.Vector2(0,1)                               # Start with a unit vector
        rotated_vector = unit_vector.rotate(self.rotation)              # Rotate the init vecto to de currect rotation of the player.
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt  # Add the speed to de rotated vector
        self.position += rotated_with_speed_vector                      # Update the player's position with the vector


    def update(self, dt):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)# I reverse dt to rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)# I reverse dt to move backwards
        if keys[pygame.K_w]:
            self.move(dt)