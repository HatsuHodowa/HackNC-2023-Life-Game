import time
import pygame

# main variables

class Controller:
    def __init__(self):

        # propreties
        self.clock = pygame.time.Clock()
        self.framerate = 5

        # running update loop
        while True:
            self.update()

    def update(self):
        # timing frames per second
        t1 = time.time()
        self.clock.tick(self.framerate)
        t2 = time.time()
        dt = t2 - t1

        # running stuff


# creating controller for testing
control = Controller()