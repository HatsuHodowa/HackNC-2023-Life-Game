import time
import pygame
import Model
import View

class Controller:
    def __init__(self):

        # propreties
        self.clock = pygame.time.Clock()
        self.framerate = 2
        self.cell_count = 10

        self.model = Model.Model(self.cell_count, self.cell_count)
        self.view = View.View(self, self.cell_count)

        # setting initial configuration for testing
        self.model.setCell(5, 5, 1)
        self.model.setCell(5, 6, 1)
        self.model.setCell(5, 7, 1)

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

        # updating model
        self.model.cellUpdate()

        # updating view
        self.view.update()
        self.view.window.update()

# creating controller for testing
control = Controller()