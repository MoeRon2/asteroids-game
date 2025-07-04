import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0

    


    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable) 
    Shot.containers = (updatable, drawable, shots)

    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField() 

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
       
        # Lock the FPS to 60, the game will loop until 1/60th of a second has passed. 
        # Clock.tick gives us a result in ms we are converting to seconds

        updatable.update(dt)
        
        # drawable.draw(screen) for this player needs to have an attribute of image
         
        for drawable_element in drawable:
            drawable_element.draw(screen)
        
        # Asteroid check for collision
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                sys.exit("Game over!")
            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.split()


        # player.update(dt) refactored
        # player.draw(screen)
        
        dt = Clock.tick(60) / 1000

        pygame.display.flip()
 
if __name__ == "__main__":
    main()
