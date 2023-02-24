import numpy as np
import matplotlib.pyplot as pyplot

class Chart:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def LineChartMin(self):
        pyplot.title("Minimum Temperature in Calgary between 1990-2019")
        pyplot.ylabel("Temperature")
        pyplot.xlabel("Year")
        pyplot.plot(self.x, self.y, marker='o')
        pyplot.show()
        return pyplot

    def LineChartMax(self):
        pyplot.title("Maximum Temperature in Calgary between 1990-2019")
        pyplot.ylabel("Temperature")
        pyplot.xlabel("Year")
        pyplot.plot(self.x, self.y, marker='o')
        pyplot.show()
        return pyplot

    def BarChartSnow(self):
        pyplot.bar(self.x, self.y)
        pyplot.title("Average Snowfall Annually in Calgary between 1990-2019")
        pyplot.ylabel("Snowfall")
        pyplot.xlabel("Year")
        pyplot.show()
        return pyplot

    def BarChartAvg(self):
        pyplot.bar(self.x, self.y)
        pyplot.title("Average Temperature Annually in Calgary between 1990-2019")
        pyplot.ylabel("Temperature")
        pyplot.xlabel("Year")
        pyplot.show()
        return pyplot

