import ModelQ
import numpy as np


class Model:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pm = ModelQ(width, height)
        self.om = ModelQ(width, height)

    def getCellO(self, i, j):
        return self.om.getCell(i, j)
    def getCellP(self, i, j):
        return self.pm.getCell(i, j)
    def valid(self, i, j):
        return i >= 0 and i < self.width and j >= 0  and j < self.height
    def cellUpdate(self):
        self.pm.cellUpdate()
        self.om.cellUpdate()
        temp = self.pm.li * 1
        self.pm.li = temp - self.om.li*0.5
        self.om.li = self.om.li - 0.5 * temp
        self.pm.pall()
        self.om.pall()
    def setCellO(self, i, j, value):
        if self.valid(i, j):
            self.om.setCell(i, j, value)
    def setCellP(self, i, j, value):
        if self.valid(i, j):
            self.pm.setCell(i, j, value)
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height



