from FileIO import fileIO
from Chart import Chart
from Date import Date
from TemperatureData import TemperatureData
from WeatherAnalyzer import WeatherAnalyzer
import numpy as np

RawData = fileIO('Term Project\Milestone 1\CalgaryWeather.csv')
data = RawData.FormatData()
TempDataList = []

for i in range(359):
   Dates = Date(data[i, 0], data[i, 1])
   TempData = TemperatureData(Dates, data[i, 2], data[i, 3], data[i, 4])
   TempDataList.append(TempData)
analyzer = WeatherAnalyzer(TempDataList)

while True: 
   loop = True
   while loop == True:
      print("Enter a number: \n 1 - Get Minimum Temperature of 1990 - 2019 \n 2 - Get Maximum Temperature of 1990 - 2019 \n 3 - Get Minimum Temperature of 1990 - 2019 Annually \n 4 - Get Maximum Temperature of 1990 - 2019 Annually \n 5 - Get Average Snowfall between 1990 - 2019 Annually \n 6 - Get Average Temperature between 1990-2019 Annually \n 7 - LineChart Minimum Temperature of 1990-2019 Annually \n 8 - LineChart Maximum Temperature of 1990-2019 Annually \n 9 - BarChart Average Snowfall between 1990-2019 Annually \n 10 - BarChart Average Temperature between 1990-2019 Anually \n")
      inputer = input()
      inputer = int(inputer)
      if inputer > 0 and inputer < 11:
         loop = False
      else:
         print('Input Valid Number')
         del inputer

   analyzer = WeatherAnalyzer(TempDataList)
   if inputer == 1:
      getMin = analyzer.minTemp()
      print(f"Minimum Temperature (Year/Month/Temp): {getMin}")

   if inputer == 2:
      getMax = analyzer.maxTemp()
      print(f"Maximum Temperature (Year/Month/Temp): {getMax}")

   if inputer == 3:
      print('\nMinimum Annual Temperatures: \nYear \nMonth \nTemp\n')
      getMinAnnual = analyzer.minTempAnnual()
      count = 1
      for entry in getMinAnnual:
         print(entry)
         if count % 3 == 0:
            print()
         count += 1

   if inputer == 4:
      print('\nMaximim Annual Temperatures: \nYear \nMonth \nTemp\n')
      getMaxAnnual = analyzer.maxTempAnnual()
      count = 1
      for entry in getMaxAnnual:   
         print(entry)
         if count % 3 == 0:
            print()
         count += 1

   if inputer == 5:
      print('\nAverage Snowfall Annually: \nYear \nSnowfall\n')
      getAvgSnow = analyzer.avgSnowAnnual()
      counter = 1
      for entry in getAvgSnow:
         print (entry)
         if counter % 2 == 0:
            print()
         counter += 1

   if inputer == 6: 
      print('\nAverage Temperature Anually: \nYear \nTemperature\n')
      getAvgTemp = analyzer.avgTempAnnual()
      counter = 1
      for entry in getAvgTemp:
         print(entry)
         if counter % 2 == 0:
            print()
         counter += 1
   
   if inputer  == 7:
      TempMin = []
      YearMin = []
      chartMinAnnual = analyzer.minTempAnnual()
      for x in chartMinAnnual:
         if x < 2020 and x > 1989:
            YearMin.append(x)
         if x < 1990 and x != 1:
            TempMin.append(x)
      LineMin = Chart(YearMin, TempMin)
      DisplayChart = LineMin.LineChartMin()

   
   if inputer == 8:
      TempMax = []
      YearMax = []
      chartMaxAnnual = analyzer.maxTempAnnual()
      for x in chartMaxAnnual:
         if x < 2020 and x > 1989:
            YearMax.append(x)
         if x < 1990 and x != 7:
            TempMax.append(x)
      LineMax = Chart(YearMax, TempMax)
      DisplayChart = LineMax.LineChartMax()
      
      

   if inputer == 9:
      Snow = []
      Year = []
      chartAvgSnow = analyzer.avgSnowAnnual()
      for x in chartAvgSnow:
         if x < 2020 and x > 1989:
            Year.append(x)
         if x < 1990:
            Snow.append(x)
      BarSnow = Chart(Year, Snow)
      DisplayChart = BarSnow.BarChartSnow()


   if inputer == 10:
      Temp = []
      Year = []
      chartAvgTemp = analyzer.avgTempAnnual()
      for x in chartAvgTemp:
         if x < 2020 and x > 1989:
            Year.append(x)
         if x < 1990:
            Temp.append(x)
      BarTemp = Chart(Year, Temp)
      DisplayChart = BarTemp.BarChartAvg()
      

   print("Do you wish to continue? (y/n): ")
   doContinue = input()
   if doContinue == 'y':
      continue
   else:
      break

print("Thank you for using this program.")
