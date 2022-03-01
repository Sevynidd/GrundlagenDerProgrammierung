import pandas as pd
from sys import exc_info
import numpy as np

if __name__ == '__main__':

    auswahl = 0
    while (not auswahl == 1) and (not auswahl == 2):
        auswahl = int(input("1. Schreiben oder 2. Lesen?"))
    match auswahl:
        case 1:
            spalten = int(input("Wie viele Spalten?"))
            zeilen = int(input("Wie viele Zeilen?"))



            for z in range(zeilen):
                for sp in range(spalten):
                    if z == 0:
                        arr[z][sp] = input("Überschrift ", sp+1, ": ")
                    else:
                        arr[z][sp] = input("Zeile ", z + 1, ", Spalte ", sp+1, ": ")
            Pfad = input("In welchem Pfad soll die CSV-Datei gespeichert werden?")
            try:
                np.savetxt(Pfad, arr, delimiter=";")
            except IOError:
                print("Es ist folgender Fehler aufgetreten: ", exc_info()[0])
        case 2:
            Pfad = input("In welchem Pfad liegt die Csv-Datei?")
            try:
                df = pd.read_csv(Pfad, index_col=0)
                print(df)
            except IOError:
                print("Es ist folgender Fehler aufgetreten: ", exc_info()[0])
