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
        self.simulation_active = True
        self.menu = menu

        # modules
        self.setModules()

        # looping update
        self.last_physics_update = time.time()
        while self.simulation_active:
            self.update()

    def close(self):
        self.simulation_active = False
        self.clearCells()
        self.stop()
        self.view.window.destroy()

    def setModules(self):
        self.model = GameModel.Model(self.cell_count, self.cell_count)
        self.view = SimulationView.SimulationView(self, self.cell_count)
            
    def updateCellCount(self, toSet):
        self.view.update_cell_count(toSet)
        self.update()

    def saveConfiguration(self):
        config = self.model.pm.li
        file = filedialog.asksaveasfilename(initialdir="/LevelData", filetypes=[("Text file", "*.txt")])

        with open(file, "w") as f:
            for row in config:
                for value in row:
                    f.write(str(value) + ",")
            f.close()

    def loadConfiguration(self, model, file):
        with open(file, "r") as f:
            lines = f.readlines()
            values = lines[0].split(",")
            current_index = 0

            # setting cell values
            for x, row in enumerate(model.li):
                for y, value in enumerate(row):
                    model.setCell(x, y, values[current_index])
                    current_index += 1

            # adding model attributes from load data
            for i, line in enumerate(lines):
                if i != 0:
                    args = line.split("=")
                    if len(args) == 2:
                        name = args[0]
                        value = args[1]
                        setattr(model, name, int(value))

    def start(self):
        self.active = True

    def stop(self):
        self.active = False

    def clearCells(self):
        for i, row in enumerate(self.model.pm.li):
            for j, row in enumerate(row):
                self.model.setCellO(i, j, 0)
                self.model.setCellP(i, j, 0)

    def onCellUpdate(self):
        pass

    def update(self):

        # updating model
        current_time = time.time()
        dt = time.time() - self.last_physics_update
        frameTime = 1 / self.framerate

        if self.active == True and dt >= 1 / self.framerate:
            self.model.cellUpdate()
            self.onCellUpdate()
            self.last_physics_update = current_time

        # updating display
        self.view.update()
        self.view.window.update()