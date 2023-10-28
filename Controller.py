import time
import Model
import ModelQ
import GameModel
import View

class Controller:
    def __init__(self):

        # properties
        self.framerate = 5
        self.cell_count = 25
        self.active = False

        # modules
        self.model = GameModel.Model(self.cell_count, self.cell_count)
        self.view = View.View(self, self.cell_count)
        self.model.setCellO(4, 5, 1)
        self.model.setCellO(4, 6, 1)
        self.model.setCellO(4, 7, 1)
        # looping update
        self.last_physics_update = time.time()
        while True:
            self.update()

    def start(self):
        self.active = True

    def stop(self):
        self.active = False

    def clearCells(self):
        for i, row in enumerate(self.model.pm.li):
            for j, row in enumerate(row):
                self.model.setCellO(i, j, 0)
                self.model.setCellP(i, j, 0)

    def update(self):

        # updating model
        current_time = time.time()
        dt = time.time() - self.last_physics_update
        frameTime = 1 / self.framerate

        if self.active == True and dt >= 1 / self.framerate:
            self.model.cellUpdate()
            self.last_physics_update = current_time

        # updating display
        self.view.update()
        self.view.window.update()

# creating controller for testing
control = Controller()