import ModelQ
import NewModel
import numpy as np


class Model:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pm = NewModel.Model(width, height)
        self.om = NewModel.Model(width, height)
        self.c = 0

    def getCellO(self, i, j):
        return self.om.getCell(i, j)
    def getCellP(self, i, j):
        return self.pm.getCell(i, j)
    def valid(self, i, j):
        return i >= 0 and i < self.width and j >= 0  and j < self.height
    def cellUpdate(self):
        self.pm.cellUpdate()
        self.om.cellUpdate()
        temp = self.pm.li.copy()

        k=0.02 + self.c / 1e5
        self.c += 1
        print(k)
        print(sum(sum(self.pm.li)))
        print(sum(sum(self.om.li)))
        self.pm.li = self.pm.li - np.square(self.om.li)*k
        self.om.li = self.om.li - k * np.square(temp)
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



