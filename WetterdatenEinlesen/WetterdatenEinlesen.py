import csv
import matplotlib.pyplot

#Author of the Basis File: Daniel Katzberg

#Liste, in der die gewünschten Daten abgespeichert werden.
dataList = []
#Öffnen der CSV Datei
with open('C:\\Users\\EinsSchueler\\Documents\\Schule\\Berufsschule\\SuD\\Jahr 1\\07 Grundlagen der '
          'Programmierung\\07 Wetter Daten.csv', newline='') as csvfile:
    #Zeilenweises Einlesen der CSV Datei
    reader = csv.DictReader(csvfile)
    for row in reader:
        #'DE_temperature' ist der Name einer Spalte, wie diese in der 1. Zeile notiert ist.
        dataList.append(float(row['DE_temperature']))

    #Plotten der Daten
    matplotlib.pyplot.plot(dataList)
    matplotlib.pyplot.show()

    print(len(dataList))