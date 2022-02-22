from math import sqrt as wurzel

# Boolean
arrPrimzahlen = []


def arrayFuellen(i, limit):
    if i != limit:
        arrPrimzahlen.append(True)
        i += 1
        arrayFuellen(i, limit)
    else:
        return 0


def sieb(limit):
    # i ist die zu testende Zahl
    for i in range(1, int(wurzel(limit)+1), 1):
        if arrPrimzahlen[i-1]:
            for j in range(i * i, limit+1, i):
                arrPrimzahlen[j-1] = False


def siebDesEratosthenes():
    limit = int(input("Obergrenze: "))

    arrayFuellen(0, limit)

    arrPrimzahlen[0] = False

    sieb(limit)

    counter = 0
    for zahl in range(limit):
        if arrPrimzahlen[zahl]:
            counter += 1
            print(counter, ": ", zahl+1)

