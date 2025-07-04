import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    # if collision return true
    def check_collision(self, other):
        
        our_position = self.position
        asteroid_position = other.position

        our_radius = self.radius
        asteroid_radius = other.radius

        distance_to_asteroid = our_position.distance_to(asteroid_position)

        # check our distance to the other object.
        if distance_to_asteroid <= (our_radius + asteroid_radius):
            return True
        return False