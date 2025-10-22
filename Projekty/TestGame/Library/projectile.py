from Projekty.TestGame.Library.helper import *

class Projectile:
    image = pygame.image.load("R:\\PRG\\Python\\Projekty\\TestGame\\Meteorite.png")

    xPos = 0
    yPos = 0
    speed = 1

    xScale = 30
    yScale = 30

    living = 100

    angle = 0

    last_pressed_y = 'down'

    def __init__(self, screen, base):
        self.screen = screen
        self.base = base

    def draw(self):
        DrawOnScreen(self.screen, pygame.transform.rotate(self.image, self.angle), (self.xPos, self.yPos), (self.xScale, self.yScale))

    def updatepos(self):
        self.living -= 1

        if self.angle == 0:
            self.yPos -= self.speed

        if self.angle == 180:
            self.yPos += self.speed

        if self.angle == 90:
            self.xPos -= self.speed

        if self.angle == 270:
            self.xPos += self.speed

        if self.living <= 0:
            self.base.projectiles.remove(self)