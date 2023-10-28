


class Model:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.li = [[0]*height] * width

    def getCell(self, i, j):
        return self.li[i][j]
    def valid(self, i, j):
        return i > 0 and i < self.width and j > 0  and j < self.height
    def alive(self, i, j):
        c = 0
        for x in range(i-1, 1+2):
            for y in range(j-1, j+2):
                if (x != i) or (j!= y):
                    if self.valid(x, y) and self.li[x][y] == 1:
                        c += 1
        return c
    def cellUpdate(self):
        lin = [[0]*self.height] * self.width
        for x in range(self.width):
            for y in range(self.height):
                temp = self.alive(x, y)
                current = self.li[x][y]
                #cases
                if current == 1 and temp in [2, 3]:
                    lin[x][y] = 1
                if current ==0  and temp == 3:
                    lin[x][y] = 1
                else:
                    lin[x][y] = 0
        self.li = lin[:]
    def setCell(self, i, j, value):
        self.li[i][j] = value

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

