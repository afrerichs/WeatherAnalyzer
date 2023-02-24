import numpy as np
class fileIO:
    def __init__(self, filePath):
        self.filePath = filePath

    def FormatData (self):
        data = np.loadtxt(self.filePath, delimiter=',', skiprows=1, usecols=(0,1,2,3,4), dtype=np.float)
        return data