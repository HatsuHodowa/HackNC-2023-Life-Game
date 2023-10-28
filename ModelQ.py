import numpy as np


class Model:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.li = np.array([[0.0]*height] * width)

    def getCell(self, i, j):
        return self.li[i][j]
    def valid(self, i, j):
        return i >= 0 and i < self.width and j >= 0  and j < self.height
    def alive(self, i, j):
        c = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if self.valid(x, y):
                    
                    if (x != i) or (j!= y):
                        c += self.li[x][y]
                        
        return c
    def p(self,v ):
        if v < 0:
            return 0
        elif v > 1:
            return 1
        else:
            return v
    def cellUpdate(self):
        lin = np.array([[0.0]*self.height] * self.width)
        for x in range(self.width):
            for y in range(self.height):
                temp = self.alive(x, y)
                current = self.li[x][y]
                #cases
                #print(x, y, current, temp)
                if current > 0.5:
                    if 2.3 <= temp and temp <= 2.8 :
                        lin[x][y] = 1
                    elif 1 <= temp and temp < 2.3 :
                        lin[x][y] = self.p(current - 0.2)
                    elif 0 < temp and temp < 1 :
                        lin[x][y] = self.p(current - 0.3)
                    elif 2.8 < temp :
                        lin[x][y] = self.p(current - temp*0.2000)
                    else:
                        lin[x][y] = 0
                elif current < 0.5:
                    if temp >= 2.5 and temp <= 3.5:
                        lin[x][y] = self.p(current + 0.4)
                    elif temp >= 1.5 and temp < 2.5:
                        lin[x][y] = self.p(current + 0.15)
                    elif temp > 3.5 and temp <= 4.5:
                        lin[x][y] = self.p(current + 0.1)
                    else:
                        lin[x][y] = 0
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
                
                print(round(self.li[x][y], 1), end="\t")
            print("")


