import numpy as np
import Model

class Model(Model.Model):


    
    def cellUpdate(self):
        lin = np.array([[0.0]*self.height] * self.width)
        for x in range(self.width):
            for y in range(self.height):
                temp = self.alive(x, y)
                current = self.li[x][y]
                #cases
                #print(x, y, current, temp)
                if current > 0.5:
                    if 2.0 <= temp and temp <= 3 :
                        lin[x][y] = 1
                    elif 1 <= temp and temp < 2.1 :
                        lin[x][y] = self.p(current - 0.5)
                    else:
                        lin[x][y] = 0
                    '''elif 1 <= temp and temp < 2.1 :
                        lin[x][y] = self.p(current - 0.4)
                    elif 0 < temp and temp < 1 :
                        lin[x][y] = self.p(current - 0.4)
                    elif 3 < temp :
                        lin[x][y] = self.p(current - temp*0.2)'''
                    
                elif current < 0.5:
                    if temp >= 2.5 and temp <= 3.5:
                        lin[x][y] = 1
                    else:
                        lin[x][y] = 0
                    '''elif temp >= 1.5 and temp < 2.5:
                        lin[x][y] = self.p(current + 0.3)
                    elif temp > 3.5 and temp <= 4.5:
                        lin[x][y] = self.p(current + 0.3)'''
                    
                else:
                    lin[x][y] = 0
        #print(lin)
        self.li = lin



