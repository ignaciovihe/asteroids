from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()  # Remove the current asteroid from the game
        if self.radius <= ASTEROID_MIN_RADIUS:  # Stop if the asteroid is too small to split
            return
        log_event("asteroid_split")  # Log a split event for tracking or testing
        new_angle = random.uniform(20.0, 50.0)  # Generate a random angle between 20 and 50 degrees
        new_asteroid_1_velocity = self.velocity.rotate(new_angle)  # Rotate original velocity for first new asteroid
        new_asteroid_2_velocity = self.velocity.rotate(-new_angle)  # Rotate original velocity in opposite direction for second asteroid
        new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS  # Determine the radius for the new asteroids
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroids_radius)  # Create first new asteroid at same position
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroids_radius)  # Create second new asteroid at same position
        new_asteroid_1.velocity = new_asteroid_1_velocity * 1.2  # Assign velocity to first asteroid, slightly faster
        new_asteroid_2.velocity = new_asteroid_2_velocity * 1.2  # Assign velocity to second asteroid, slightly faster
