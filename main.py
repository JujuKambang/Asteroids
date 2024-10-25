import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable,drawable)
    Player.containers = (updatable,drawable)
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield1 = AsteroidField()
    print("AsteroidField created")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick()/100
        for asteroid in asteroids:
            if player1.collisioncheck(asteroid) == True:
                print("Game over!")
                pygame.quit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collisioncheck(asteroid) == True:
                    shot.kill()
                    asteroid.split()
        for thing in updatable:
            thing.update(dt)
        for drawablething in drawable:
            drawablething.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        print(f"Number of asteroids: {len(asteroids)}")
        print(f"Asteroid positions: {[a.position for a in asteroids]}")
        print(f"Asteroid velocities: {[a.velocity for a in asteroids]}")

if __name__ == "__main__":
    main()