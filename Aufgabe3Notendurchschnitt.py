import numpy.core as np
import pandas.core.frame as pd


def erstellen_der_tabelle(noten_der_faecher):
    """ Import Pandas braucht ein Array um daraus eine Tabelle zu machen, doch NotenDerFaecher ist eine Liste.
            Deshalb numpy_data = NotenDerFaecher"""
    numpy_data = np.array([noten_der_faecher])
    #                 Daten            Überschriften    Linker Rand
    df = pd.DataFrame(data=numpy_data, columns=Faecher, index=["Noten"])
    print(df, "\n")


def notendurchschnitt(durchschnitt):
    durchschnitt_der_letzten10_jahre = 2.35

    # Zusätzliche Ausgabe je nachdem wie der Notendurchschnitt ausfällt
    if durchschnitt < durchschnitt_der_letzten10_jahre:
        print(f"{durchschnitt}: Über dem 10 Jahre durchschnitt")
        # Wenn zusätzlich der Notendurchschnitt besser ist als 2.0
        if durchschnitt < 2.0:
            print("Gute Chance auf eine direkte, unbefristete Übernahme")
    elif durchschnitt == durchschnitt_der_letzten10_jahre:
        print(f"{durchschnitt}: Gleich dem 10 Jahre durchschnitt")
    elif durchschnitt > durchschnitt_der_letzten10_jahre:
        print(f"{durchschnitt}: Unter dem 10 Jahre durchschnitt")


def abfrageFächer():
    """Es wird nach der Anzahl der Fächer gefragt, da man im darauffolgenden Schritt den Namen
        und die Note des Fachs eingeben kann """
    anzahlFaecher = int(input("Wie viele Fächer?:"))
    # Durchschnitt der Noten der Azubis der letzen 10 Jahre
    Faecher = []
    NotenDerFaecher = []

    # Einzeln jedes Fach mit der dazugehörigen Note abfragen
    for i in range(anzahlFaecher):
        Faecher.append(input(f"Fachname {i + 1}?:"))
        NotenDerFaecher.append(int(input(f"Note für {Faecher[i]}?: ")))
        print("")

    erstellen_der_tabelle(NotenDerFaecher)

    # Notendurchschnitt der Fächer ausrechnen
    Notendurchschnitt = 0.0
    for i in NotenDerFaecher:
        Notendurchschnitt += i
    Notendurchschnitt /= len(NotenDerFaecher)

    notendurchschnitt(Notendurchschnitt)
