import pandas as pd
from sys import exc_info
import numpy as np
import csv
from InputOutputFiles import Kopieren
from InputOutputFiles import Schreiben
from InputOutputFiles import Lesen

if __name__ == '__main__':

    auswahl = 0
    while (not auswahl == 1) and (not auswahl == 2):
        auswahl = int(input("1. Schreiben oder 2. Lesen?"))
    match auswahl:
        case 1:
            Schreiben.func_write()
        case 2:
            Pfad = input("In welchem Pfad liegt die Csv-Datei?\n(Format: C:\\Users\\User\\Desktop\\CSV.csv)")
            try:
                df = pd.read_csv(Pfad, delimiter=";")
                print(df)
            except IOError:
                print("Es ist folgender Fehler aufgetreten: ", exc_info()[0])
