from Projekty.TestGame.Library.Enums.Rotation import Rotation
from Projekty.TestGame.Library.helper import *
from Projekty.TestGame.Library.projectile import *
from Enums import *

class Player:
    image = pygame.image.load("R:\\PRG\\Python\\Projekty\\TestGame\\Starship.png")

    xPos = 0
    yPos = 0
    speed = 1

    xScale = 60
    yScale = 60

    angle = 0

    last_pressed_y = 'down'

    projectiles = []


    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        DrawOnScreen(self.screen, pygame.transform.rotate(self.image, self.angle), (self.xPos, self.yPos), (self.xScale, self.yScale))
        self.drawproj()

    def updatepos(self, keys):
        if keys[pygame.K_w]:
            self.yPos -= self.speed

        if keys[pygame.K_s]:
            self.yPos += self.speed

        if keys[pygame.K_d]:
            self.xPos += self.speed

        if keys[pygame.K_a]:
            self.xPos -= self.speed

    def updateposbetter(self, keys):
        # Detect just-pressed keys by comparing current and previous keys
        just_pressed_w = keys[pygame.K_w] and not self.prev_keys[pygame.K_w]
        just_pressed_s = keys[pygame.K_s] and not self.prev_keys[pygame.K_s]
        just_pressed_a = keys[pygame.K_a] and not self.prev_keys[pygame.K_a]
        just_pressed_d = keys[pygame.K_d] and not self.prev_keys[pygame.K_d]

        if keys[pygame.K_SPACE]:
            self.shoot()

        # Update vertical last pressed key
        if just_pressed_w:
            self.last_pressed_y = 'up'
        elif just_pressed_s:
            self.last_pressed_y = 'down'
        # Reset vertical direction if none pressed
        if not keys[pygame.K_w] and not keys[pygame.K_s]:
            self.last_pressed_y = ''

        # Update horizontal last pressed key
        if just_pressed_a:
            self.last_pressed_x = 'left'
        elif just_pressed_d:
            self.last_pressed_x = 'right'
        # Reset horizontal direction if none pressed
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.last_pressed_x = ''

        # Vertical movement
        if keys[pygame.K_w] and keys[pygame.K_s]:
            if self.last_pressed_y == 'down':
                self.yPos += self.speed
                self.angle = Rotation.DOWN
            else:
                self.yPos -= self.speed
                self.angle = 0
        elif keys[pygame.K_w]:
            self.yPos -= self.speed
            self.angle = Rotation.UP
        elif keys[pygame.K_s]:
            self.yPos += self.speed
            self.angle = Rotation.DOWN

        # Horizontal movement
        if keys[pygame.K_a] and keys[pygame.K_d]:
            if self.last_pressed_x == 'right':
                self.xPos += self.speed
                self.angle = Rotation.RIGHT
            else:
                self.xPos -= self.speed
                self.angle = Rotation.LEFT
        elif keys[pygame.K_a]:
            self.xPos -= self.speed
            self.angle = Rotation.RIGHT
        elif keys[pygame.K_d]:
            self.xPos += self.speed
            self.angle = Rotation.LEFT

        # Store current keys for next frame
        self.prev_keys = keys



    def shoot(self):
        proj = Projectile(self.screen, self)

        proj.angle = self.angle

        proj.xPos = self.xPos + proj.xScale/4
        proj.yPos = self.yPos + self.yScale/4

        self.projectiles.append(proj)
        pass

    def drawproj(self):
        for proj in self.projectiles:
            proj.draw()
            proj.updatepos()

    def drawHitbox(self):
        pygame.draw.rect()
