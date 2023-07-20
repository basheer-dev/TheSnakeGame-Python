import pygame
from random import randrange
from Snake import Snake
from Food import Food

pygame.init()


class Main():


    def __init__(self):
        self.run = True
        self.fps = 60

        self.configureWindow()
        self.setSnakeVars()
        self.setFoodVars()


    def configureWindow(self):
        self.width, self.height = 500, 500

        pygame.display.set_caption("TheSnakeGame")
        self.window = pygame.display.set_mode((self.width, self.height))

        # Surfaces
        self.mainSurface = pygame.Surface(self.window.get_size(), pygame.SRCALPHA)


    def setSnakeVars(self):
        self.snakeVars = {
            'head': pygame.Rect(100, 100, 10, 10),
            'tails': [],
            'movement': {'x': 10, 'y': 0},
            'movementRateCounter': 10,
            'defaultMRC': 10
        }

        head = self.snakeVars['head']
        for i in range(1, 10):
            self.snakeVars['tails'].append(pygame.Rect(head.x - (head.w * i), head.y, head.w, head.h))

        '''
            * The movementRateCounter variable defines how many frames has to pass before the snake moves one block.
            * In this case the snake moves at the rate of one block each 10 frames.
        '''


    def setFoodVars(self):
        self.foodVars = {
            'rect': pygame.Rect(randrange(0, self.width - 10, 10), randrange(0, self.height - 10), 10, 10)
        }


    def main(self):
        self.showWindowGrid()

        self.snake = Snake(main=self, surface=self.mainSurface)
        self.food = Food(main=self, surface=self.mainSurface, snakeHead=self.snake.head)


    def showWindowGrid(self):
        for i in range(0, self.width, 10):
            pygame.draw.line(self.window, (230, 230, 230), (i, 0), (i, self.height))

        for j in range(0, self.height, 10):
            pygame.draw.line(self.window, (230, 230, 230), (0, j), (self.width, j))


    def activate(self):
        clock = pygame.time.Clock()

        while self.run:
            clock.tick(self.fps)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.run = False

            self.window.fill((255, 255, 255))

            self.window.blit(self.mainSurface, (0, 0))
            self.mainSurface.fill((0, 0, 0, 0))

            self.main()
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    main = Main()
    main.activate()