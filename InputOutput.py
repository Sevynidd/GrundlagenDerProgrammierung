import pandas as pd
import numpy as np
import csv
from InputOutputFiles import Kopieren
from InputOutputFiles import Schreiben
from InputOutputFiles import Lesen

if __name__ == '__main__':

    auswahl = 0
    while (auswahl < 1) or (auswahl > 3):
        auswahl = int(input("1. Schreiben, 2. Lesen oder 3. Kopieren?"))
    match auswahl:
        case 1:
            Schreiben.func_write()
        case 2:
            Lesen.func_read()
        case 3:
            Kopieren.func_copy()
