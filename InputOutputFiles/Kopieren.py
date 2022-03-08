import shutil
from shutil import copy2


def func_copy():
    PfadOriginal = input("In welchem Pfad liegt die zu kopierende CSV-Datei?\n(Format: "
                         "C:\\Users\\User\\Desktop\\CSV.csv)")

    PfadNew = input("In welchen Pfad soll die neue CSV-Datei kopiert werden?\n(Format: "
                    "C:\\Users\\User\\Desktop)")
    try:
        copy2(PfadOriginal, PfadNew)
    except shutil.SameFileError:
        umbenennen = input("Die Datei existiert so bereits\nWollen Sie die Datei umbenennen?")

        match umbenennen.lower():
            case "ja":
                nameNeu = input("Welcher Name? (Bitte ohne '.csv' am Ende)")
                try:
                    copy2(PfadOriginal, PfadNew + "\\" + nameNeu + ".csv")
                except shutil.SameFileError:
                    print("Auch beim 2ten Versuch kann die Datei nicht in den Pfad kopiert werden")
            case "nein":
                print("Datei kann nicht kopiert werden")
