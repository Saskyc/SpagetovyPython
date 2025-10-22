# Example file showing a basic pygame "game loop"
import pygame
import Library
from Projekty.TestGame.Library.helper import *
from Projekty.TestGame.Library.player import *
from Projekty.TestGame.Library.projectile import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

image = pygame.image.load("R:\\PRG\\Python\\Projekty\\TestGame\\Apple.png")

player = Player(screen)

x = 50
y = 500
speed = 10

last_pressed_y = ''
last_pressed_x = ''


pygame.display.flip()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    # fill screen with purple.



    screen.fill("purple")
    DrawOnScreen(screen, image, (x, y), (60, 60))
    #screen.blit(pygame.transform.scale(imp, (50, 50)), (x, 20))

    # Keyboard
    keys = pygame.key.get_pressed()  # This will give us a dictionary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

    player.draw()
    player.updateposbetter(pygame.key.get_pressed())

    #new controls




    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()