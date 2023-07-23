import pygame


class Home():

    def __init__(self, main):
        self.mainClass = main

        self.run = True
        self.fps = main.fps

        self.configureWindow()
        self.activate()


    def configureWindow(self):
        self.width, self.height = self.mainClass.width, self.mainClass.height

        self.window = pygame.Surface(self.mainClass.window.get_size(), pygame.SRCALPHA)


    def activate(self):
        clock = pygame.time.Clock()

        while self.run:
            clock.tick(self.fps)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.run = False
                    self.mainClass.run = False
                    break

            self.mainClass.blitSurface(surface=self.window, color=(255, 255, 255))
            pygame.display.update()
