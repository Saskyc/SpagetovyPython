import pygame

def DrawOnScreen(self, image, pos, scale):
    self.blit(pygame.transform.scale(image, scale), pos)