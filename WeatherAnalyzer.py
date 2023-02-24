class WeatherAnalyzer():
    def __init__(self, tempDataList):
        self.tempDataList = tempDataList

    def minTemp(self):
        minreturner = []
        i = 0
        j = 0
        while i < 359 and j < 359:
            if self.tempDataList[i].getMin() <= self.tempDataList[j].getMin():
                j += 1 
            else:
                i += 1
        if j == 359:
            minreturner.append(int(self.tempDataList[i].getDate().getYear()))
            minreturner.append(int(self.tempDataList[i].getDate().getMonth()))
            minreturner.append(self.tempDataList[i].getMin())
            return minreturner
        else:
            minreturner.append(int(self.tempDataList[j].getDate().getYear()))
            minreturner.append(int(self.tempDataList[j].getDate().getMonth()))
            minreturner.append(self.tempDataList[j].getMin())
            return minreturner
        
    def maxTemp(self):
        maxreturner = []
        i = 0
        j = 0
        while i < 359 and j < 359:
            if self.tempDataList[i].getMax() <= self.tempDataList[j].getMax():
                i += 1
            else:
                j += 1
        if j == 359:
            maxreturner.append(int(self.tempDataList[i].getDate().getYear()))
            maxreturner.append(int(self.tempDataList[i].getDate().getMonth()))
            maxreturner.append(self.tempDataList[i].getMax())
            return maxreturner
        else:
            maxreturner.append(int(self.tempDataList[j].getDate().getYear()))
            maxreturner.append(int(self.tempDataList[j].getDate().getMonth()))
            maxreturner.append(self.tempDataList[j].getMax())
            return maxreturner

    def minTempAnnual(self):
        minAnnual = []
        for y in range(29):
            i = (12 * y)
            j = (12 * y)
            while i < (12 + (12 * y)) and j < (12 + (12 * y)):
                if self.tempDataList[i].getMin() <= self.tempDataList[j].getMin():
                    j += 1 
                else:
                    i += 1
            if j == (12 + 12 * y):
                minAnnual.append(int(self.tempDataList[i].getDate().getYear()))
                minAnnual.append(int(self.tempDataList[i].getDate().getMonth()))
                minAnnual.append(self.tempDataList[i].getMin())
            else:
                minAnnual.append(int(self.tempDataList[j].getDate().getYear()))
                minAnnual.append(int(self.tempDataList[j].getDate().getMonth()))
                minAnnual.append(self.tempDataList[j].getMin())
        i = 348
        j = 348
        while i < 359 and j < 359:
            if self.tempDataList[i].getMin() <= self.tempDataList[j].getMin():
                j += 1
            else:
                i += 1
        minAnnual.append(int(self.tempDataList[i].getDate().getYear()))
        minAnnual.append(int(self.tempDataList[i].getDate().getMonth()))
        minAnnual.append(self.tempDataList[i].getMin())
        return minAnnual

    def maxTempAnnual(self):
        maxAnnual = []
        for y in range(29):
            i = (12 * y)
            j = (12 * y)
            while i < (12 + (12 * y)) and j < (12 + (12 * y)):
                if self.tempDataList[i].getMax() <= self.tempDataList[j].getMax():
                    i += 1
                else:
                    j += 1
            maxAnnual.append(int(self.tempDataList[j].getDate().getYear()))
            maxAnnual.append(int(self.tempDataList[j].getDate().getMonth()))
            maxAnnual.append(self.tempDataList[j].getMax())
        i = 348
        j = 348
        while i < 359 and j < 359:
            if self.tempDataList[i].getMax() <= self.tempDataList[j].getMax():
                i += 1
            else:
                j += 1
        maxAnnual.append(int(self.tempDataList[j].getDate().getYear()))
        maxAnnual.append(int(self.tempDataList[j].getDate().getMonth()))
        maxAnnual.append(self.tempDataList[j].getMax())
        return maxAnnual
 
    def avgSnowAnnual(self):
        avgSnow = []
        for y in range(29):
            sum = 0
            i = 12 * y
            while i < 12 + 12 * y:
                sum += self.tempDataList[i].getSnow()
                i += 1
            avg = sum / 12
            avgSnow.append(int(self.tempDataList[i - 1].getDate().getYear()))
            avgSnow.append(avg)
        sum = 0
        for x in range(348, 359):
            sum += self.tempDataList[x].getSnow()
        avg = sum / 11
        avgSnow.append(int(self.tempDataList[355].getDate().getYear()))
        avgSnow.append(avg)
        return avgSnow

    def avgTempAnnual(self):
        avgTemp = []
        for y in range(29):
            m1sum = 0
            m2sum = 0
            for m1 in range(12):
                m1sum += self.tempDataList[m1 + y * 12].getMax()
            for m2 in range(12):
                m2sum += self.tempDataList[m2 + y * 12].getMin()
            m1avg = m1sum / 12
            m2avg = m2sum / 12
            avg = (m1avg + m2avg) / 2
            avgTemp.append(int(self.tempDataList[m1 + y * 12 -1].getDate().getYear()))
            avgTemp.append(avg)
        m1 = 348
        m2 = 348
        m1sum = 0
        m2sum = 0
        while m1 < 359:
            m1sum += self.tempDataList[m1].getMax()
            m1 += 1
        while m2 < 359:
            m2sum += self.tempDataList[m2].getMin()
            m2 += 1
        m1avg = m1sum / 11
        m2avg = m2sum / 11
        avg = ((m1avg + m2avg) / 2)
        avgTemp.append(int(self.tempDataList[m1-1].getDate().getYear()))
        avgTemp.append(avg)
        return avgTemp




        