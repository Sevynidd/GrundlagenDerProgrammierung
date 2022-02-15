import sys


def eingabe_wichtige_daten():
    # Eingabe aller wichtigen Daten
    daten_temp = [input("Vorname?: "), input("Nachname?: "), "", ""]

    while type(daten_temp[2]) != int:
        try:
            daten_temp[2] = (int(input("Alter?: ")))
            break
        except ValueError:
            print("Die Eingabe ist kein Integer")

    daten_temp[3] = (input("Wohnort?: "))

    return daten_temp


def abfragePersönlicheDaten():
    firmaCodingStar = ""
    AGB = ""

    AlleDaten = eingabe_wichtige_daten()

    # Ist egal ob groß oder klein
    if AlleDaten[3].lower() == "löhne":
        # Fragen nur stellen, wenn man in Löhne wohnt
        firmaCodingStar = input("Kennen Sie die Firma Coding Star?: ")
        if firmaCodingStar.lower() == "ja":
            firmaCodingStar = True
        elif firmaCodingStar.lower() == "nein":
            firmaCodingStar = False
        else:
            print("Keine gültige Eingabe")
            sys.exit(0)

        AGB = input("Waren Sie auf dem August-Griese-Berufskolleg?: ")
        if AGB.lower() == "ja":
            AGB = True
        elif AGB.lower() == "nein":
            AGB = False
        else:
            print("Keine gültige Eingabe")
            sys.exit(0)

    # Ausgabe abhängig von der Antwort oben
    print(f"\n{AlleDaten[0]} {AlleDaten[1]} wohnt in {AlleDaten[3]} und ist {AlleDaten[2]} Jahre alt")
    if AlleDaten[3].lower() == "löhne":
        if firmaCodingStar:
            firmaCodingStar = "Ja"
        elif not firmaCodingStar:
            firmaCodingStar = "Nein"
        if AGB:
            AGB = "Ja"
        elif not AGB:
            AGB = "Nein"

        print(f"Kennt Coding Star?: {firmaCodingStar}")
        print(f"War auf dem AGB?: {AGB}")
