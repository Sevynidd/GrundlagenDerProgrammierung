import csv
# Plots
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
# File Dialog (GUI)
import tkinter
from tkinter import filedialog

dataTempJedesMonats = []
dataJahresDurchschnitt = []
dataTemp11Uhr = []

Pfad = ''


def plot1():
    temperatur_eines_monats = 0.0
    monat = 1
    wertanzahl_plot1 = 0
    # Öffnen der CSV Datei
    with open(Pfad, newline='') as csvfile:
        # Zeilenweises Einlesen der CSV Datei
        reader = csv.DictReader(csvfile)

        for row in reader:
            timestamp_str = row['utc_timestamp']
            dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
            if monat == dt.month:
                wertanzahl_plot1 += 1
                temperatur_eines_monats += float(row['DE_temperature'])
            else:
                monat = dt.month
                if not wertanzahl_plot1 == 0:
                    temperatur_eines_monats /= wertanzahl_plot1
                    dataTempJedesMonats.append(float(temperatur_eines_monats))
                    temperatur_eines_monats = 0.0
                    wertanzahl_plot1 = 0


def plot2():
    temperatur_eines_jahres = 0.0
    jahr = 1980
    wertanzahl_plot2 = 0
    # Öffnen der CSV Datei
    with open(Pfad, newline='') as csvfile:
        # Zeilenweises Einlesen der CSV Datei
        reader = csv.DictReader(csvfile)

        for row in reader:
            timestamp_str = row['utc_timestamp']
            dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
            if jahr == dt.year:
                wertanzahl_plot2 += 1
                temperatur_eines_jahres += float(row['DE_temperature'])
            else:
                jahr += 1
                if not wertanzahl_plot2 == 0:
                    temperatur_eines_jahres /= wertanzahl_plot2
                    dataJahresDurchschnitt.append(float(temperatur_eines_jahres))
                    temperatur_eines_jahres = 0.0
                    wertanzahl_plot2 = 0


def plot3():
    # Öffnen der CSV Datei
    with open(Pfad, newline='') as csvfile:
        # Zeilenweises Einlesen der CSV Datei
        reader = csv.DictReader(csvfile)

        for row in reader:
            timestamp_str = row['utc_timestamp']
            dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
            if dt.hour == 11:
                dataTemp11Uhr.append(float(row['DE_temperature']))


if __name__ == '__main__':
    tkinter.Tk().withdraw()
    Pfad = filedialog.askdirectory()

    Pfad += "\\07 Wetter Daten.csv"

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
