import pandas as pd
from sys import exc_info


def func_read():
    Pfad = input("In welchem Pfad liegt die Csv-Datei?\n(Format: C:\\Users\\User\\Desktop\\CSV.csv)")
    try:
        df = pd.read_csv(Pfad, delimiter=";")
        print(df)
    except FileNotFoundError:
        func_read()
    except IOError:
        print("Es ist folgender Fehler aufgetreten: ", exc_info()[0])
