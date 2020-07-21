# import pygame
import pygame

# initialize game engine
pygame.init()


clock_tick_rate=60

# Open a window
size = (800, 600)
screen = pygame.display.set_mode(size)

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("Space.jpg").convert()


playerimg = pygame.image.load("A Spaceship.png")
playerx = 400
playery = 300

playerx_change = 0
playery_change = 0

def player(x,y):
  screen.blit(playerimg,(x,y))

while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])
    playerx -= 1
    playerx += playerx_change

    player(playerx, playery)

    pygame.display.flip()
    clock.tick(clock_tick_rate)
