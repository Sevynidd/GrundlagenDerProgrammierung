import csv
import numpy as np

def func_write():
    spalten = int(input("Wie viele Spalten?"))
    zeilen = int(input("Wie viele Zeilen?"))

    arr = [[0 for x in range(spalten)] for y in range(zeilen)]

    for z in range(zeilen):
        for sp in range(spalten):
            if z == 0:
                arr[z][sp] = input(f"Überschrift {sp + 1}: ")
            else:
                arr[z][sp] = input(f"Zeile {z + 1}, Spalte {sp + 1}: ")
    Pfad = input("In welchem Pfad soll die CSV-Datei gespeichert werden?\n(Format: "
                 "C:\\Users\\User\\Desktop\\CSV.csv)")
    try:
        with open(Pfad, 'w', newline='') as file:
            mywriter = csv.writer(file, delimiter=';')
            mywriter.writerows(np.array(arr))
    except IOError:
        print("Es ist folgender Fehler aufgetreten: ", exc_info()[0])
