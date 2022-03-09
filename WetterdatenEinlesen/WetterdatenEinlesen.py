import csv
import matplotlib.pyplot
from datetime import datetime

# https://www.geeksforgeeks.org/how-to-add-title-to-subplots-in-matplotlib/

if __name__ == '__main__':
    dataList = []
    eingabe = 0

    while not (1 <= eingabe <= 3):
        eingabe = int(input("1. Temperatur jedes Monats (arithmetisches Mittel)\n" +
                            "2. Jahresdurchschnittstemperatur\n" +
                            "3. Temperatur immer um 11 Uhr"))

    match eingabe:
        case 1:
            temperaturEinesMonats = 0.0
            monat = 1
            wertanzahl = 0

            # Öffnen der CSV Datei
            with open('C:\\Users\\Karina\\Desktop\\07 Wetter Daten.csv', newline='') as csvfile:
                # Zeilenweises Einlesen der CSV Datei
                reader = csv.DictReader(csvfile)

                for row in reader:
                    timestamp_str = row['utc_timestamp']
                    dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
                    if monat == dt.month:
                        wertanzahl += 1
                        temperaturEinesMonats += float(row['DE_temperature'])
                    else:
                        monat = dt.month
                        if not wertanzahl == 0:
                            temperaturEinesMonats /= wertanzahl
                            dataList.append(float(temperaturEinesMonats))
                            temperaturEinesMonats = 0.0
                            wertanzahl = 0

        case 2:
            temperaturEinesJahres = 0.0
            jahr = 1980
            wertanzahl = 0

            # Öffnen der CSV Datei
            with open('C:\\Users\\Karina\\Desktop\\07 Wetter Daten.csv', newline='') as csvfile:
                # Zeilenweises Einlesen der CSV Datei
                reader = csv.DictReader(csvfile)

                for row in reader:
                    timestamp_str = row['utc_timestamp']
                    dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
                    if jahr == dt.year:
                        wertanzahl += 1
                        temperaturEinesJahres += float(row['DE_temperature'])
                    else:
                        jahr += 1
                        if not wertanzahl == 0:
                            temperaturEinesJahres /= wertanzahl
                            dataList.append(float(temperaturEinesJahres))
                            temperaturEinesJahres = 0.0
                            wertanzahl = 0
        case 3:
            # Öffnen der CSV Datei
            with open('C:\\Users\\Karina\\Desktop\\07 Wetter Daten.csv', newline='') as csvfile:
                # Zeilenweises Einlesen der CSV Datei
                reader = csv.DictReader(csvfile)

                for row in reader:
                    timestamp_str = row['utc_timestamp']
                    dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
                    if dt.hour == 11:
                        dataList.append(float(row['DE_temperature']))

    # Plotten der Daten
    matplotlib.pyplot.plot(dataList)
    match eingabe:
        case 1:
            matplotlib.pyplot.title("1. Temperatur jedes Monats (arithmetisches Mittel)")
            matplotlib.pyplot.xlabel("Monat")
            matplotlib.pyplot.ylabel("Temperatur (Monatsdurchschnitt)")
        case 2:
            matplotlib.pyplot.title("2. Jahresdurchschnittstemperatur")
            matplotlib.pyplot.xlabel("Jahr")
            matplotlib.pyplot.ylabel("Temperatur (Jahresdurchschnitt)")
        case 3:
            matplotlib.pyplot.title("3. Temperatur immer um 11 Uhr")
            matplotlib.pyplot.xlabel("Tag")
            matplotlib.pyplot.ylabel("Temperatur um 11 Uhr")

    matplotlib.pyplot.show()
