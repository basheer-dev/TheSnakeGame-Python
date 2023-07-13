import pygame


class Snake():

    def __init__(self, main, surface: pygame.Surface):
        self.mainClass = main
        self.surface = surface
        self.vars = main.snakeVars
        self.head = main.snakeVars['head']
        self.tails = main.snakeVars['tails']

        self.setControls()
        self.configureMovement()
        self.show()

    def setControls(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.vars['movement'] = {'x': 10, 'y': 0}

        if keys[pygame.K_LEFT]:
            self.vars['movement'] = {'x': -10, 'y': 0}

        if keys[pygame.K_DOWN]:
            self.vars['movement'] = {'x': 0, 'y': 10}

        if keys[pygame.K_UP]:
            self.vars['movement'] = {'x': 0, 'y': -10}

        # Speed up when the user hits the space button
        if keys[pygame.K_SPACE]:
            self.vars['defaultMRC'] = 2

        else:
            self.vars['defaultMRC'] = 10

    def configureMovement(self):
        if self.vars['movementRateCounter'] == 0:
            self.vars['tails'].insert(0, pygame.Rect(self.head.x, self.head.y, self.head.w, self.head.h))
            self.vars['tails'].pop()

            self.head.x += self.vars['movement']['x']
            self.head.y += self.vars['movement']['y']

        self.vars['movementRateCounter'] = self.vars['movementRateCounter'] - 1 if self.vars['movementRateCounter'] > 0 else self.vars['defaultMRC']

        if self.head.x + self.head.w > self.mainClass.width:
            self.head.x = 0

        if self.head.x < 0:
            self.head.x = self.mainClass.width - self.head.w

        if self.head.y + self.head.h > self.mainClass.height:
            self.head.y = 0

        if self.head.y < 0:
            self.head.y = self.mainClass.height - self.head.h

    def show(self):
        pygame.draw.rect(self.surface, (255, 0, 0), self.head)

        for tail in self.tails:
            pygame.draw.rect(self.surface, (0, 0, 0), tail)