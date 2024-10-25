from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)
    
    def update(self,dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            randnum = random.uniform(20,50)
            newradius = self.radius - ASTEROID_MIN_RADIUS
            newAsteroid1 = Asteroid(self.position.x,self.position.y,newradius)
            newAsteroid2 = Asteroid(self.position.x,self.position.y,newradius)
            newAsteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, randnum) * 1.2
            newAsteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -randnum) * 1.2
        
