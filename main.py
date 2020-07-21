# import pygame
import pygame

# initialize game engine
pygame.init()


clock_tick_rate=20

# Open a window
size = (800, 600)
screen = pygame.display.set_mode(size)

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("Space.jpg").convert()


playerimg = pygame.image.load("A Spaceship.png")
playerx = 400
playery = 300

def player():
  screen.blit(playerimg,(playerx,playery))

while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])
    player()

    pygame.display.flip()
    clock.tick(clock_tick_rate)
