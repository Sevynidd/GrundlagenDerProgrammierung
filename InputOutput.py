import pandas as pd
from sys import exc_info
import numpy as np
import csv

if __name__ == '__main__':

    auswahl = 0
    while (not auswahl == 1) and (not auswahl == 2):
        auswahl = int(input("1. Schreiben oder 2. Lesen?"))
    match auswahl:
        case 1:
            spalten = int(input("Wie viele Spalten?"))
            zeilen = int(input("Wie viele Zeilen?"))

            arr = [[0 for x in range(spalten)] for y in range(zeilen)]

            for z in range(zeilen):
                for sp in range(spalten):
                    if z == 0:
                        arr[z][sp] = input(f"Überschrift {sp+1}: ")
                    else:
                        arr[z][sp] = input(f"Zeile {z+1}, Spalte {sp+1}: ")
            Pfad = input("In welchem Pfad soll die CSV-Datei gespeichert werden?")
            try:
                with open(Pfad, 'w', newline='') as file:
                    mywriter = csv.writer(file, delimiter=';')
                    mywriter.writerows(np.array(arr))
            except IOError:
                print("Es ist folgender Fehler aufgetreten: ", exc_info()[0])


        case 2:
            Pfad = input("In welchem Pfad liegt die Csv-Datei?")
            try:
                df = pd.read_csv(Pfad, delimiter=";")
                print(df)
            except IOError:
                print("Es ist folgender Fehler aufgetreten: ", exc_info()[0])
