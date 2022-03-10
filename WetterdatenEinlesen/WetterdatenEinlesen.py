import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

dataTempJedesMonats = []
dataJahresDurchschnitt = []
dataTemp11Uhr = []


def plot1():
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
                    dataTempJedesMonats.append(float(temperaturEinesMonats))
                    temperaturEinesMonats = 0.0
                    wertanzahl = 0


def plot2():
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
                    dataJahresDurchschnitt.append(float(temperaturEinesJahres))
                    temperaturEinesJahres = 0.0
                    wertanzahl = 0


def plot3():
    # Öffnen der CSV Datei
    with open('C:\\Users\\Karina\\Desktop\\07 Wetter Daten.csv', newline='') as csvfile:
        # Zeilenweises Einlesen der CSV Datei
        reader = csv.DictReader(csvfile)

        for row in reader:
            timestamp_str = row['utc_timestamp']
            dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
            if dt.hour == 11:
                dataTemp11Uhr.append(float(row['DE_temperature']))


if __name__ == '__main__':

    fig, ax = plt.subplots(1, 3)

    plot1()

    wertanzahl = 0

    plot2()

    plot3()

    ax[0].plot(dataTempJedesMonats)
    ax[1].plot(dataJahresDurchschnitt)
    ax[2].plot(dataTemp11Uhr)

    ax[0].set_title("1. Temperatur jedes Monats (arithmetisches Mittel)")
    ax[0].set_xlabel("Monat")
    ax[0].set_ylabel("Temperatur (Monatsdurchschnitt)")

    ax[1].set_title("2. Jahresdurchschnittstemperatur")
    ax[1].set_xlabel("Jahr")
    ax[1].set_ylabel("Temperatur (Jahresdurchschnitt)")

    ax[2].set_title("3. Temperatur immer um 11 Uhr")
    ax[2].set_xlabel("Tag")
    ax[2].set_ylabel("Temperatur um 11 Uhr")

    fig.tight_layout()

    figure = plt.gcf()
    figure.set_size_inches(14, 5, forward=True)
    figure.set_dpi(100)

    plt.get_current_fig_manager().set_window_title("Wetterdaten auslesen")

    plt.show()

    exit(0)
