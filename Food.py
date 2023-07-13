import pygame
from random import randrange


class Food():

    def __init__(self, main, surface: pygame.Surface, snakeHead: pygame.Rect):
        self.mainClass = main
        self.surface = surface
        self.snakeHead = snakeHead
        self.vars = main.foodVars
        self.rect = main.foodVars['rect']

        self.getsEaten()
        self.show()

    def getsEaten(self):
        if self.rect.colliderect(self.snakeHead):
            self.rect.x = randrange(0, self.mainClass.width - self.rect.w, 10)
            self.rect.y = randrange(0, self.mainClass.height - self.rect.h, 10)

    def show(self):
        center = (self.rect.x + self.rect.w/2, self.rect.y + self.rect.h/2)
        pygame.draw.circle(self.surface, (0, 0, 255), center, self.rect.w/2)