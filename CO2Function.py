import sys
import os
import numpy as np
import SolverEuler
import matplotlib.pyplot as plt

from Python_Projekt.Room import RoomClass as RC

class CO2Concentration(RC):
    def __init__(self):
        RC.__init__(self)
        #self.startTime=0            #[s]
        #self.Area=60                #[m^2]
        #self.Hight=3                #[m]
        #self.peopleCount=25          #[]

        self.breathingRatePeople=20 #[l/h]
        self.burp = self.breathingRatePeople*1000/3600 * self.peopleCount

        #self.airExchangeRate=0.6      #[1/h]
        self.aers = self.airExchangeRate/3600

        self.C_co2Null=400          #[ppm]
        self.C_co2Inlet=400         #[ppm]
        self.Volume = self.Area * self.Hight

        self.xNull=self.C_co2Null
    def F(self,t,x):
        c=x
        dcdt = -(self.aers*c) + (self.aers*self.C_co2Inlet) + (self.burp/self.Volume)
        return dcdt

if __name__ == "__main__":
    foobar = CO2Concentration()
    solver = SolverEuler.Euler(foobar)
    solver.reInit()
    solver.integrate()
        
    plt.plot(solver.t, solver.x)
    plt.show()
