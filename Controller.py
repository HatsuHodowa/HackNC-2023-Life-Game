import time
import Model
import ModelQ
import GameModel
import View
import datetime
from tkinter import filedialog

class Controller:
    def __init__(self):

        # properties
        self.framerate = 5
        self.cell_count = 15
        self.active = False

        # modules
        self.model = GameModel.Model(self.cell_count, self.cell_count)
        self.view = View.View(self, self.cell_count)

        # looping update
        self.last_physics_update = time.time()
        while True:
            self.update()
            
    def updateCellCount(self, toSet):
        self.cell_count = toSet
        self.model.width = toSet
        self.model.height = toSet
        self.view.update_cell_count(toSet)
        self.update()

    def saveConfiguration(self):
        config = self.model.pm.li
        file = filedialog.asksaveasfilename(initialdir="/SaveData", filetypes=[("Text file", "*.txt")])

        with open(file, "w") as f:
            for row in config:
                for value in row:
                    f.write(str(value) + ",")
            f.close()

    def loadConfiguration(self, model, file):
        with open(file, "r") as f:
            values = f.read().split(",")
            current_index = 0

            for x, row in enumerate(model.li):
                for y, value in enumerate(row):
                    model.setCell(y, x, values[current_index])
                    current_index += 1

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