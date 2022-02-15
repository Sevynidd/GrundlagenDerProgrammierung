from Aufgabe1PersoenlicheDaten import abfragePersönlicheDaten as Prog1
from Aufgabe3Notendurchschnitt import abfrageFächer as Prog2
from Fibonacci import fibonacci as Prog4
from Taschenrechner import taschenrechner as Prog3
from SiebDesEratosthenes import siebDesEratosthenes as Prog5

if __name__ == "__main__":

    while True:
        print("\n1. Persönliche Daten\n2. Notendurchschnitt\n3. Taschenrechner\n4. Fibonacci\n5. Sieb des "
              "Eratosthenes\n6. Exit\n")
        Eingabe = int(input("Geben Sie die Zahl des auszuführenden Punktes an: \n"))

        match Eingabe:
            case 1: Prog1()
            case 2: Prog2()
            case 3: Prog3()
            case 4: Prog4()
            case 5: Prog5()
            case 6: exit()
