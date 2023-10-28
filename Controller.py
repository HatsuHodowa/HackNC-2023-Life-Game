import time
import pygame
import Model
import ModelQ
import View

class Controller:
    def __init__(self):

        # properties
        self.clock = pygame.time.Clock()
        self.framerate = 0
        self.cell_count = 50
        self.active = False

        self.model = ModelQ.Model(self.cell_count, self.cell_count)
        self.view = View.View(self, self.cell_count)

        # setting initial configuration for testing
        self.model.setCell(5, 5, 1)
        self.model.setCell(5, 6, 1)
        self.model.setCell(5, 7, 1)
        self.model.setCell(6, 7, 1)
        self.model.setCell(7, 6, 1)

        # looping
        #self.start()
        while True:

            # timing frames per second
            t1 = time.time()
            self.clock.tick(self.framerate)
            t2 = time.time()
            dt = t2 - t1

            # updating
            self.update(dt)

    def start(self):
        self.active = True

    def stop(self):
        self.active = False

    def update(self, dt):

        # updating model
        if self.active == True:
            self.model.cellUpdate()

        # updating display
        self.view.update()
        self.view.window.update()

# creating controller for testing
control = Controller()