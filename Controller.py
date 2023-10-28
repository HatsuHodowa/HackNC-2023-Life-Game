import time
import pygame
import Model

pygame.init()

class Controller:
    def __init__(self):

        # propreties
        self.clock = pygame.time.Clock()
        self.framerate = 2
        self.height = 10
        self.width = 10
        self.model = Model.Model(self.width, self.height)

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
        #print(self.model.li)

        print("Frame finish")

# creating controller for testing
control = Controller()