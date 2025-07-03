from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
from player import Player

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

    # Assign groups
    Player.containers = (updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
       
        # Lock the FPS to 60, the game will loop until 1/60th of a second has passed. 
        # Clock.tick gives us a result in ms we are converting to seconds

        updatable.update(dt)
        
        for drawable_element in drawable:
            drawable_element.draw(screen)
        
        # player.update(dt) refactored
        # player.draw(screen)
        
        dt = Clock.tick(60) / 1000

        pygame.display.flip()
 
if __name__ == "__main__":
    main()
