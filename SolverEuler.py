import numpy as np

class Euler:
    def __init__(self, model):
        self.dt = 1
        #self.n = 10

        #self.t = np.zeros(self.n)
        #self.x = np.zeros(self.n)

        self.tEnd = 60
        #self.t[0]=0

        self.F = model.F
        self.xNull = model.xNull

        self.reInit()

    def reInit(self):
        self.n = int(self.tEnd/self.dt)

        self.t = np.linspace(0,self.tEnd,self.n)
        self.x = np.zeros((self.n,1), dtype=float)

        self.t[0] = 0
        self.x[0] = self.xNull

    def integrate(self):
        for i in range(0, self.n - 1):
            # dTdt = -(kA/(m*c))*(T-Ta)
            self.t[i + 1] = self.t[i] + self.dt
            self.x[i + 1] = self.x[i] + self.F(self.t[i], self.x[i]) * self.dt
