import time
import Model
import ModelQ
import GameModel
import SimulationView
import datetime
from tkinter import filedialog

class SimulationController:
    def __init__(self, menu):

        # properties
        self.framerate = 5
        self.cell_count = 15
        self.active = False
        self.menu = menu

        # modules
        self.setModules(self)

        # looping update
        self.last_physics_update = time.time()
        while True:
            self.update()

    def setModules(self):
        self.model = GameModel.Model(self.cell_count, self.cell_count)
        self.view = SimulationView(self, self.cell_count)
            
    def updateCellCount(self, toSet):
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
                    model.setCell(x, y, values[current_index])
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