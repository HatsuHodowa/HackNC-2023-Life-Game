import numpy as np


class Model:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.li = np.array([[0.0]*height] * width)

        # level-specific attributes
        self.cell_limit = None

    def getCell(self, i, j):
        return self.li[i][j]
    def valid(self, i, j):
        return i >= 0 and i < self.width and j >= 0  and j < self.height
    
    def p(self,v ):
        if v < 0:
            return 0
        elif v > 1:
            return 1
        else:
            return v
    def pall(self):
        for i in range(self.width):
            for j in range(self.height):
                self.li[i][j] = self.p(self.li[i][j])
    def alive(self, i, j):
        c = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if (x != i) or (j!= y):
                    
                    if self.valid(x, y):
                        
                        if self.li[x][y] == 1:
                            c += 1
        return c
    def cellUpdate(self):
        lin = np.array([[0]*self.height] * self.width)
        for x in range(self.width):
            for y in range(self.height):
                temp = self.alive(x, y)
                current = self.li[x][y]
                #cases
                #print(x, y, current, temp)
                if current == 1 and temp in [2, 3]:
                    lin[x][y] = 1
                elif current ==0  and temp == 3:
                    lin[x][y] = 1
                else:
                    lin[x][y] = 0
        #print(lin)
        self.li = lin
    def setCell(self, i, j, value):
        if self.valid(i, j):
            self.li[i][j] = value

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
    def printli(self):
        print(self.li)
    def print(self):
        for y in range(self.height):
            for x in range(self.width): 
                
                print(self.li[x][y], end="\t")
            print("")


