import pandas as pd
import numpy as np
import csv
from InputOutputFiles import Kopieren
from InputOutputFiles import Schreiben
from InputOutputFiles import Lesen

if __name__ == '__main__':

    auswahl = 0
    while (not auswahl == 1) and (not auswahl == 2):
        auswahl = int(input("1. Schreiben oder 2. Lesen?"))
    match auswahl:
        case 1:
            Schreiben.func_write()
        case 2:
            Lesen.func_read()
