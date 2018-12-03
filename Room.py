import numpy as np
import SolverEuler
import matplotlib.pyplot as plt

class RoomClass():
    def __init__(self):
        self.startTime=0            #[s]
        self.Area=60                #[m^2]
        self.Hight=3                #[m]
        self.peopleCount=25          #[]
        self.airExchangeRate=0.6      #[1/h]
