
class TemperatureData():
    def __init__ (self, Date, Max, Min, Snow):
        self.date = Date
        self.max = Max
        self.min = Min
        self.snow = Snow
    
    def getDate(self):
        return self.date
    
    def getMax(self):
        return self.max

    def getMin(self):
        return self.min

    def getSnow(self):
        return self.snow