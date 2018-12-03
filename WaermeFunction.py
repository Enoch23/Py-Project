import sys
import os
import numpy as np
import SolverEuler
import matplotlib.pyplot as plt

from Python_Projekt.Room import RoomClass as RC

class Temperature(RC):
    def __init__(self):
        RC.__init__(self)



        self.QDotpp=120 #[W] Schwere Arbeit 300W
        self.TempInlet = 300 #[K]
        self.TempNull = 300 #[k]
        self.Ta = 290 #[K]
        self.Ti = 300 #[K]

        #self.startTime=0            #[s]
        #self.Area=60                #[m^2]
        #self.Hight=3                #[m]
        #self.peopleCount=25          #[]
        #self.airExchangeRate=0.6      #[1/h]

        self.aers = self.airExchangeRate/3600
        self.QDot = self.QDotpp*self.peopleCount
        self.cAir = 1.005
        self.rhoAir = 1.204 #bei 20°
        self.m = self.Area*self.Hight*self.rhoAir # ggf Berechung


        self.kAWall = np.sqrt(self.Area)*2*self.Hight*0.1
        self.kAWindow = np.sqrt(self.Area)*2*self.Hight*0.4
        self.kAFloor =self.Area*0.2
        self.kARoof = self.Area*0.3





        self.C_co2Null=400          #[ppm]
        self.C_co2Inlet=400         #[ppm]
        self.Volume = self.Area * self.Hight

        self.xNull=self.TempNull
    def F(self,t,x):
        T=x
        dTdt = -((self.kAWindow+self.kARoof+self.kAFloor)/(self.m*self.cAir))*(T-self.Ta)-(self.kAWall/self.m*self.cAir)*(T-self.Ti)+self.QDot/(self.m*self.cAir)-self.airExchangeRate*(T-self.TempInlet)

        return dTdt

#if __name__ == "__main__":
foobar = Temperature()
solver = SolverEuler.Euler(foobar)
solver.reInit()
solver.integrate()

plt.plot(solver.t, solver.x)
plt.show()
