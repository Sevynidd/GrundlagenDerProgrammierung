def Addition(Zahl1, Zahl2):
    return Zahl1 + Zahl2


def Subtraktion(Zahl1, Zahl2):
    return Zahl1 - Zahl2


def Multiplikation(Zahl1, Zahl2):
    return Zahl1 * Zahl2


def Division(Zahl1, Zahl2):
    return Zahl1 / Zahl2


def Hoch(Zahl1, Zahl2):
    return Zahl1 ** Zahl2


def Rest(Zahl1, Zahl2):
    Rest = Zahl1 % Zahl2
    return Zahl1 - Rest


def taschenrechner():
    Zahl1 = int(input("Geben Sie die erste Zahl ein: "))

    Rechenoperation = input("Addition (+), Subtraktion (-), Multiplikation (*), Division (/), Hoch(**), Rest(%)?\n"
                            "Geben Sie das Symbol an: ")

    Zahl2 = int(input("Geben Sie die zweite Zahl ein: "))

    match Rechenoperation.strip():
        case "+":
            Ergebnis = Addition(Zahl1, Zahl2)
        case "-":
            Ergebnis = Subtraktion(Zahl1, Zahl2)
        case "*":
            Ergebnis = Multiplikation(Zahl1, Zahl2)
        case "/":
            Ergebnis = Division(Zahl1, Zahl2)
        case "**":
            Ergebnis = Hoch(Zahl1, Zahl2)
        case "%":
            Ergebnis = Rest(Zahl1, Zahl2)

    if Rechenoperation.strip() != "%":
        print(f"{Zahl1}{Rechenoperation}{Zahl2} = {Ergebnis}")
    else:
        temp = Zahl1 % Zahl2
        print(f"{Zahl1}{Rechenoperation}{Zahl2} = {Ergebnis} Rest {temp}")
