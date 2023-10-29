import numpy as np
import math
import cmath
import Model

class Model(Model.Model):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.li = np.array([[0.0]*height] * width)
        self.wf = np.array([[0.0]*height] * width)
    def bounded(self, x, y, vect):
        if self.valid(x, y):
            return vect[x][y]
        else:
            return 0
    def hamit(self, vect):
        vect2 = np.array([[0.0 +0.0j]*self.height] * self.width)
        i = 1j
        for x in range(self.width):
            for y in range(self.height):
                vect2[x][y] += self.bounded(x-1, y, vect) + self.bounded(x+1, y, vect) -4*self.bounded(x, y, vect) +self.bounded(x, y+1, vect) + self.bounded(x, y-1, vect)
        return vect2 * i * 0.5 - 0.1*vect2**3
    def cellUpdate(self):
        lin = np.array([[0.0]*self.height] * self.width)
        vect = np.array([[0.0]*self.height] * self.width)
        
        for x in range(self.width):
            for y in range(self.height):
                vect[x][y] = math.sqrt(self.li[x][y])
        if sum(sum(self.wf)) != 0:
            vect = self.wf*1.0
        bef = sum(sum(self.li))
        
        vect = vect + 0.05*self.hamit(vect)
        
        for x in range(self.width):
            for y in range(self.height):
                
                lin[x][y] = vect[x][y].real**2+vect[x][y].imag**2

        aft = sum(sum(lin))
        #print(bef, aft)
        k = 1
        if bef != 0:
            k = bef/aft*1.05
        self.li = lin*k
        self.wf = vect*k**0.5
        #print(self.li*255)



