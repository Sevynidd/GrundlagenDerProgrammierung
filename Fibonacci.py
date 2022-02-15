def ausgabe(i, endbedingung):
    # "for i in range(endbedingung)"
    if i != endbedingung:
        print(berechnen(i))
        # i++
        i += 1
        return ausgabe(i, endbedingung)


def berechnen(n):
    if n <= 1:
        return n
    else:
        return berechnen(n - 1) + berechnen(n - 2)


def fibonacci():
    zahlen = int(input("Wie viele Zahlen?"))

    if zahlen <= 0:
        print("Keine gültige Zahl")
    else:
        print("Fibonacci: ")
        # "for i in range (zahlen)"
        ausgabe(0, zahlen)
