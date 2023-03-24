from turtle import color
import pandas as panda
import math
import matplotlib.pyplot as plt
import numpy as np
correctYears = []
for i in range(2010, 2022):
    correctYears.append(i)

def chooseOneYear():
    chooseYear = 1
    chooseYear = int(input("Podaj rok: "))
    return chooseYear
    
def preparePlotXaxisData(data):
    dates = []
    for i in range (len(data["Rok"])):
        dates.append(str(data["Dzień"][i])+"-"+str(data["Miesiąc"][i])+"-"+str(data["Rok"][i]))
    return dates
    
def showTemperatureInOneYear():
    chooseYear = chooseOneYear()
    if chooseYear not in correctYears:
        return
    data = panda.read_csv("Dane_roczne/s_d_495_"+str(chooseYear)+".csv")
    dates = preparePlotXaxisData(data)
    for i in range(len(data["Rok"])-1):
        if(data["Miesiąc"][i] != data["Miesiąc"][i+1]):
           plt.axvline(x = i, color = 'red', ls = "--", lw = 1)
    plt.xlim(0, len(data["Rok"]))
    plt.axhline(y = 0, color = 'black', lw = 2)
    plt.axhline(y = -10, color = 'black', lw = 1, ls = "--")
    plt.axhline(y = 10, color = 'black', lw = 1, ls = "--")
    plt.axhline(y = 20, color = 'black', lw = 1, ls = "--")
    plt.axhline(y = 30, color = 'black', lw = 1, ls = "--")
    plt.xticks([])
    plt.plot(dates, data["Maksymalna temperatura dobowa"], color = "red")
    plt.plot(data["Minimalna temperatura dobowa"], color = "blue")
    plt.show()

def showTemperatureInTwoYears():
    year1 = chooseOneYear()
    year2 = chooseOneYear()
    if (year1 not in correctYears or year2 not in correctYears):
        return
    data = panda.read_csv("Dane_roczne/s_d_495_"+str(year1)+".csv")
    data2 = panda.read_csv("Dane_roczne/s_d_495_"+str(year2)+".csv")
    dates = preparePlotXaxisData(data)
    for i in range(len(dates)):
        dates[i] = dates[i][:-5]
    for i in range(len(data["Rok"])-1):
        if(data["Miesiąc"][i] != data["Miesiąc"][i+1]):
           plt.axvline(x = i, color = 'red', ls = "--", lw = 1)
    plt.xlim(0, len(data["Rok"]))
    plt.axhline(y = 0, color = 'black', lw = 2)
    plt.axhline(y = -10, color = 'black', lw = 1, ls = "--")
    plt.axhline(y = 10, color = 'black', lw = 1, ls = "--")
    plt.axhline(y = 20, color = 'black', lw = 1, ls = "--")
    plt.axhline(y = 30, color = 'black', lw = 1, ls = "--")
    plt.xticks([])
    plt.plot(dates, data["Średnia temperatura dobowa"], label = str(year1))
    plt.plot(data2["Średnia temperatura dobowa"], label = str(year2))
    plt.legend(loc = "upper right")
    plt.show()

def showSnowCoverHeight():
    year = chooseOneYear()
    if year not in correctYears:
        return
    data = panda.read_csv("Dane_roczne/s_d_495_"+str(year)+".csv")
    dates = preparePlotXaxisData(data)
    for i in range(len(data["Rok"])-1):
        if(data["Miesiąc"][i] != data["Miesiąc"][i+1]):
           plt.axvline(x = i, color = 'red', ls = "--", lw = 1)
    plt.xlim(0, len(data["Rok"]))
    plt.xticks([])
    plt.bar(dates, data["Wysokość pokrywy śnieżnej"])
    plt.show()

def showPrecip():
    year = chooseOneYear()
    if year not in correctYears:
        return
    data = panda.read_csv("Dane_roczne/s_d_495_"+str(year)+".csv")
    dates = preparePlotXaxisData(data)
    precipType = []
    precipSum = []
    for i in range(len(data["Rok"])):
        precipType.append(data["Rodzaj opadu"][i])
        precipSum.append(data["Suma dobowa opadu"][i])
        if(precipType[i] == "S"):
            plt.bar(dates[i], precipSum[i], color = "blue")
        elif(precipType[i] == "W"):
            plt.bar(dates[i], precipSum[i], color = "green")
        else:
            plt.bar(dates[i], 0)
        if(i != len(data['Rok'])-1):
            if(data["Miesiąc"][i] != data["Miesiąc"][i+1]):
                plt.axvline(x = i, color = 'red', ls = "--", lw = 1)
    plt.xlim(0, len(data["Rok"]))
    plt.xticks([])
    plt.show()
   
def getMonthsTempAverage(i, data):
    sum = 0
    counter = 0
    for k in range(len(data["Rok"])):
        if(data["Miesiąc"][k] == i):
            sum += data["Średnia temperatura dobowa"][k]
            counter += 1
    return round(sum/counter, 1)

def getMonthTempAverageInOneYear(year, data):
    sum = 0
    counter = 0
    avgInMyYear = []
    for k in range(len(data["Rok"])-1):
        if(data["Rok"][k] == year):
            sum += data["Średnia temperatura dobowa"][k]
            counter += 1
            if(data["Miesiąc"][k] != data["Miesiąc"][k+1]):
                avgInMyYear.append(round(sum/counter, 1))
                sum = 0
                counter = 0
    return avgInMyYear
                
def showAverageTempComparision():
    year = chooseOneYear()
    if year not in correctYears:
        return
    avgInAllMonths = []
    data =  panda.read_csv("Dane_roczne/dane_pogodowe.csv") 
    for i in range (1, 13): #Liczymy średnią dla miesięcy z całego kresu
        avgInAllMonths.append(getMonthsTempAverage(i, data))
    avgInMyYear = getMonthTempAverageInOneYear(year, data) 
    dates = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"] 
    fig, ax = plt.subplots()
    width = 0.3
    x = np.arange(len(dates)) #[0, 1, 2, ..., 11]
    rects1 = ax.bar(x-width/2, avgInMyYear, width, label='Średnia w '+str(year))
    rects2 = ax.bar(x+width/2, avgInAllMonths, width, label='Średnia okresowa 2010-2021')
    ax.set_ylabel('Średnia miesięczna temperatura')
    ax.set_title('Porównanie średnich miesięcznych temperatur')
    ax.legend()
    ax.set_xticks(x, dates)
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    fig.tight_layout()
    plt.axhline(y = 0, color = 'black', lw = 2)
    plt.show()
           
def choosePanelMethod(panel):
    if(panel == 1):
        showTemperatureInOneYear()
    elif(panel == 2):
        showTemperatureInTwoYears()
    elif(panel == 3):
        showSnowCoverHeight()
    elif(panel == 4):
        showPrecip()
    elif(panel == 5):
        showAverageTempComparision()
   
choosePanel = -1    
while(choosePanel != 0) :
    print("LISTA FUNKCJI")
    print("1. Temperatura w danym roku")
    print("2. Porównanie temperatur w dwóch latach")
    print("3. Wysokość pokrywy śnieżnej w danym roku")
    print("4. Opady w danym roku")
    print("5. Porównanie miesięcznej średniej temperatury w danym roku ze średnią miesięczną okresową")
    print("0. Wyjście z programu")
    choosePanel = int(input("Twój wybór: "))
    if(choosePanel != 0):
        choosePanelMethod(choosePanel)