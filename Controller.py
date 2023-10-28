import time
import Model
import ModelQ
import GameModel
import View
import datetime

class Controller:
    def __init__(self):

        # properties
        self.framerate = 5
        self.cell_count = 25
        self.active = False

        # modules
        self.model = GameModel.Model(self.cell_count, self.cell_count)
        self.view = View.View(self, self.cell_count)

        # looping update
        self.last_physics_update = time.time()
        while True:
            self.update()

    def saveConfiguration(self):
        config = self.model.pm.li
        timestamp = str(int(time.time()))
        size_text = str(self.cell_count) + "x" + str(self.cell_count)

        with open(f"SaveData/level_config-{timestamp}-{size_text}.txt", "w") as f:
            for row in config:
                for value in row:
                    f.write(str(value) + ",")
            f.close()

    def loadConfiguration(self, model, file):
        model.clearCells()
        with open(file, "r") as f:
            values = f.readlines()
            print(values)

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