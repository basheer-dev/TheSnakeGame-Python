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
        '''
            * The user can control the snake's movement by the space button (to speed up) and the four arrows keys (to move in all directions).
        '''
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

        '''
            * When the user hits the space button the snake will move at the rate of one block in each two frames that passes.
        '''


    def configureMovement(self):
        '''
            * The snake will only move when the MRC reaches 0.
            * The snake's head will move one block, when it moves a tail part will be inserted in its previous head position and the last tail will be popped.
        '''
        if self.vars['movementRateCounter'] == 0:
            self.vars['tails'].insert(0, pygame.Rect(self.head.x, self.head.y, self.head.w, self.head.h))
            self.vars['tails'].pop()

            self.head.x += self.vars['movement']['x']
            self.head.y += self.vars['movement']['y']

        self.vars['movementRateCounter'] = self.vars['movementRateCounter'] - 1 if self.vars['movementRateCounter'] > 0 else self.vars['defaultMRC']

        # Resetting the snake's coordinates when it exceeds the screen bounds
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