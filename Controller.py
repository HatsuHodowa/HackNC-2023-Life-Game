import time
import pygame
import Model

# main variables

class Controller:
    def __init__(self):

        # propreties
        self.clock = pygame.time.Clock()
        self.framerate = 5
        self.model = Model.Model(10, 10)

        # running update loop
        while True:

            # timing frames per second
            t1 = time.time()
            self.clock.tick(self.framerate)
            t2 = time.time()
            dt = t2 - t1

            # updating
            self.update(dt)

    def update(self, dt):
        print("-----------")
        print("Frame start")

        # updating model
        self.model.cellUpdate()

        print("Frame finish")

# creating controller for testing
control = Controller()